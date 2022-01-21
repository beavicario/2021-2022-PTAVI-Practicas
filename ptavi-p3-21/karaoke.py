#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os
import sys
from xml.sax import make_parser

from smil import SMILHandler


def to_string(tags):
    line = ''
    for tag in tags:
        if line != '':
            line += '\n'
        attrs = tag['attrs']
        name = tag['name']
        line += name
        for att in attrs:
            att_name = att[0]
            att_value = att[1]
            line += '\t' + att_name + '="' + att_value + '"'
    line += '\n'
    return line


def to_json(tags):
    list = []
    for tag in tags:
        tag_dic = {'name': tag['name'], 'attrs': {}}
        for att in tag['attrs']:
            tag_dic['attrs'][att[0]] = att[1]
        list.append(tag_dic)
    return json.dumps(list, indent=3)


def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        sys.exit('Usage: python3 karaoke.py [--json] <file>')
    else:
        if sys.argv[1] == '--json' and len(sys.argv) == 3:
            filename = sys.argv[2]
            filejson = True
            if not os.path.exists(filename):
                sys.exit('File not found')
        elif len(sys.argv) == 2:
            filename = sys.argv[1]
            filejson = False
            if not os.path.exists(filename):
                sys.exit('File not found')
        else:
            sys.exit('Usage: python3 karaoke.py [--json] <file>')

    parser = make_parser()
    cHandler = SMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(filename))

    tags = cHandler.get_tags()
    print(to_string(tags), end='')
    if filejson:
        print(to_json(tags))


if __name__ == "__main__":
    main()
