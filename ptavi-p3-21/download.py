#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlretrieve
from xml.sax import make_parser

from smil import SMILHandler


def main():
    parser = make_parser()
    cHandler = SMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))

    tags = cHandler.get_tags()
    i = 0
    for tag in tags:
        for att in tag['attrs']:
            if 'http://' in att[1] or 'https://' in att[1]:
                ext = att[1].split('.')[-1]
                filename = 'fichero-' + str(i) + '.' + ext
                i += 1
                urlretrieve(att[1], filename)


if __name__ == "__main__":
    main()
