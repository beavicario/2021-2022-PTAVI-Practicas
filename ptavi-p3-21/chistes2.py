#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class ChistesHandler(ContentHandler):

    def __init__(self):
        self.calificacion = ""
        self.pregunta = ""
        self.inPregunta = False
        self.respuesta = ""
        self.inRespuesta = False
        self.count = 0

    def startElement(self, name, attrs):
        if name == 'chiste':
            self.count += 1
            self.calificacion = attrs.get('calificacion', "")
        elif name == 'pregunta':
            self.pregunta = ""
            self.inPregunta = True
        elif name == 'respuesta':
            self.respuesta = ""
            self.inRespuesta = True

    def endElement(self, name):
        if name == 'pregunta':
            self.inPregunta = False
        elif name == 'respuesta':
            self.inRespuesta = False
        elif name == 'chiste':
            print("Chiste número:", " ", self.count, " ", "(", self.calificacion, ")", sep="")
            print("Pregunta:", self.pregunta)
            print("Respuesta:", " ", self.respuesta, "\n", sep="")

    def characters(self, char):
        if self.inPregunta:
            self.pregunta = self.pregunta + char
        elif self.inRespuesta:
            self.respuesta = self.respuesta + char


def main():
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes.xml'))


if __name__ == "__main__":
    main()
