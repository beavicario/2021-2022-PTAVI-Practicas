#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SMILHandler(ContentHandler):

    def __init__(self):
        self.list = []
        self.tags = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur', 'end'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region', 'fill']
        }

    def startElement(self, name, attrs):
        if name in self.tags:
            dic = {'attrs': [], 'name': name}
            for att in self.tags[name]:
                value = attrs.get(att, "")
                if value != "":
                    dic['attrs'].append((att, value))
            self.list.append(dic)

    def get_tags(self):
        return self.list


def main():
    parser = make_parser()
    cHandler = SMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())


if __name__ == "__main__":
    main()
