#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script de comprobación de entrega de práctica

Para ejecutarlo, desde la shell:
 $ python3 check-p5.py login_gitlab

"""

import os
import random
import sys


files = ['README.md',
         'LICENSE',
         'respuesta.md',
         'linphone-call.pcapng',
         'linphone-call-total.pcapng',
         'sip.libpcap.gz',
         'p5.pcapng',
	     'check-p5.py',
         '.git',
         '.gitlab-ci.yml']

if len(sys.argv) != 2:
    sys.exit("Usage : $ python3 check-p5.py --local | login_gitlab")

if sys.argv[1] == '--local':
    repo_git = "."
else:
    repo_git = "http://gitlab.etsit.urjc.es/" + sys.argv[1] + "/ptavi-p5"

aleatorio = str(int(random.random() * 1000000))

error = 0

if sys.argv[1] != '--local':
    print("Clonando el repositorio " + repo_git)
    os.system('git clone ' + repo_git + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
    try:
        student_file_list = os.listdir('/tmp/' + aleatorio)
    except OSError:
        error = 1
        sys.exit("Error: No se ha creado el repositorio git correctamente.")
else:
    student_file_list = os.listdir('.')

if len(student_file_list) != len(files):
    error = 1
    print("Error en el número de ficheros encontrados en el repositorio")

for filename in files:
    if filename not in student_file_list:
        error = 1
        print("Error: " + filename + " no encontrado. Tienes que subirlo al repositorio.")

if error:
    sys.exit("Ojo, hubo errores")
else:
    print("Parece que la entrega se ha realizado bien.")
    print("Recuerda que también tienes que realizar un test en Moodle.")
    print()
