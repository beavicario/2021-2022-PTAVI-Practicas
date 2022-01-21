#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class ChistesHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.calificacion = ""
        self.pregunta = ""
        self.inPregunta = False
        self.respuesta = ""
        self.inRespuesta = False

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'chiste':
            self.calificacion = attrs.get('calificacion', "")
            print(self.calificacion)
        elif name == 'pregunta':
            self.pregunta = ""
            self.inPregunta = True
        elif name == 'respuesta':
            self.respuesta = ""
            self.inRespuesta = True

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            self.inPregunta = False
            print(self.pregunta)
        elif name == 'respuesta':
            self.inRespuesta = False
            print(self.respuesta)

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = self.pregunta + char
        elif self.inRespuesta:
            self.respuesta += char


def main():
    """Programa principal"""
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes.xml'))


if __name__ == "__main__":
    main()
