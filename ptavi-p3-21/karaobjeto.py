#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import sys
from urllib.request import urlretrieve
from xml.sax import make_parser

from smil import SMILHandler


class Karaoke:

    def __init__(self, filesmil):
        parser = make_parser()
        cHandler = SMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(filesmil))

        self.tags = cHandler.get_tags()

    def __str__(self):
        line = ''
        for tag in self.tags:
            if line != '':
                line += '\n'
            attrs = tag['attrs']
            name = tag['name']
            line += name
            for att in attrs:
                att_name = att[0]
                att_value = att[1]
                line += '\t' + att_name + '="' + att_value + '"'
        return line

    def to_json(self):
        list = []
        for tag in self.tags:
            tag_dic = {'name': tag['name'], 'attrs': {}}
            for att in tag['attrs']:
                tag_dic['attrs'][att[0]] = att[1]
            list.append(tag_dic)
        return json.dumps(list, indent=3)

    def download(self):
        i = 0
        for tag in self.tags:
            for att in tag['attrs']:
                if 'http://' in att[1] or 'https://' in att[1]:
                    ext = att[1].split('.')[-1]
                    filename = 'fichero-' + str(i) + '.' + ext
                    i += 1
                    urlretrieve(att[1], filename)


def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        sys.exit('Usage: python3 karaobjeto.py [--json] <file>')
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
            sys.exit('Usage: python3 karaobjeto.py [--json] <file>')

    karaoke = Karaoke(filename)
    print(karaoke)

    if filejson:
        print(karaoke.to_json())

    karaoke.download()


if __name__ == "__main__":
    main()
