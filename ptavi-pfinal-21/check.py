#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script de comprobación de entrega de práctica. Atención: este script realiza sólo
algunas comprobaciones. Puede ser que todas sean correctas, y aún así la práctica tenga
errores o le falten cosas.

Para comprobar un directorio en tu ordenador, desde el terminal,
en el directorio a comprobar:
 python3 check.py

Para comprobar tu repositorio en GitLab, desde el terminal:
 python check.py login_laboratorio
"""

import argparse
import os
import subprocess
import sys
import tempfile

dirs_to_ignore = ['.git', '.mypy_cache', '.idea', '__pycache__']
python_files = [
    'client.py',
    'serversip.py',
    'serverrtp.py'
]

test_dir = 'tests'

test_files = [
    'run_tests.py',
    '__init__.py'
]

test_paths = [os.path.join(test_dir, p) for p in test_files]

other_files = [
    'README.md',
    'LICENSE',
    '.gitignore',
    '.gitlab-ci.yml',
    'check.py',
    'simplertp.py',
    'bitstring.py',
    'cancion.mp3',
    'received.mp3',
    'capture.libpcap',
    'received2a.mp3',
    'received2b.mp3',
    'capture2.libpcap',
]

expected_files = python_files + other_files + test_paths


def get_files(dir):
    files_found = []
    dir_length = len(dir)
    for root, dirs, files in os.walk(dir):
        for d in dirs_to_ignore:
            if d in dirs:
                dirs.remove(d)
        for file in files:
            path = os.path.join(root, file)
            path = path[dir_length:].lstrip('/')
            files_found.append(path)
    return files_found


def compare_files(found, expected):
    notfound = []
    extra = []
    yesfound = []
    for file in found:
        if file not in expected:
            extra.append(file)
    for file in expected:
        if file in found:
            yesfound.append(file)
        else:
            notfound.append(file)
    if (len(extra) == 0) and (len(notfound) == 0):
        correct = True
        print("  Files ok")
    else:
        correct = False
    if len(extra) != 0:
        print("  Not needed:", ', '.join(extra))
    if len(notfound) != 0:
        print("  Missing:", ', '.join(notfound))
    return correct, yesfound


def get_git_files(dir):
    result = subprocess.run(['git', '-C', dir, 'ls-tree', '-r', 'HEAD',
                             '--name-only', '--full-name'],
                            stdout=subprocess.PIPE, text=True)
    files = []
    for line in result.stdout.splitlines():
        files.append(line)
    return files


def check_pep8(dir, files):
    success = True
    for file in files:
        result = subprocess.run(['pycodestyle', file],
                                cwd=dir, stdout=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Checking PEP8 OK: {file}")
        else:
            print(f"Checking PEP8 Error: {file}")
            print(result.stdout)
            success = False
    return success


def run_tests(dir, files):
    success = True
    result = subprocess.run(['python3', os.path.join('tests', 'run_tests.py'),
                             '--json'],
                            cwd=dir, stdout=subprocess.PIPE, text=True)
    print("Tests:", result.stdout)
    if result.returncode == 0:
        print(f"Running tests OK: {dir}")
    else:
        print(f"Running tests Error: {dir}")
        success = False
    return success


def check_dir(dir='.'):
    if not os.path.isdir(dir):
        sys.exit(f"Directory {dir} does not exist, or is not a directory")
    print(f"Checking directory {dir}...")
    found_files = get_files(dir)
    success_files, files = compare_files(found_files, expected_files)
    print("Checking files known to git...")
    git_files = get_git_files(dir)
    success_git, files2 = compare_files(git_files, expected_files)
    pep8_files = [f for f in files if f in python_files]
    success_pep8 = check_pep8(dir, pep8_files)
    tests = [f for f in files if f in test_paths]
    success_tests = run_tests(dir, tests)
    if False in (success_files, success_git, success_pep8, success_tests):
        return False
    else:
        return True

def check_repo(repo):
    with tempfile.TemporaryDirectory() as dir:
        result = subprocess.run(['git', 'clone', repo, dir],
                                stdout=subprocess.PIPE, text=True)
        if result.returncode != 0:
            sys.exit(f"Error cloning repository {repo}")
        check_dir(dir)


def parse_args():
    parser = argparse.ArgumentParser(description='Check practice.')
    parser.add_argument('--dir', default='.',
                        help="silent output, only summary is written")
    parser.add_argument('--silent', action='store_true',
                        help="silent output, only summary is written")
    args = parser.parse_args()
    return (args)


if __name__ == "__main__":
    args = parse_args()
    correct = check_dir(args.dir)
    if correct:
        print("Final result: OK")
        sys.exit(0)
    else:
        print("Final result: Error (check above)")
        sys.exit(-1)
