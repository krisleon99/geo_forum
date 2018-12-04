#!/usr/bin/env python
# -*- coding: latin-1 -*-

from datetime import datetime, timedelta
from threading import Thread
from time import sleep
"""
 Esta clase Es un hilo que se ejecuta a cierta hora y ejecuta cierta función:
 En este caso es para enviar los emails de los avisos de los usuarios.
 El constructor recibe como parámetros:
 hora = en un string con formato hh:mm:ss y es la hora a la que queremos que se ejecute la función.
 delay = tiempo de espera entre comprobaciones en segundos.
 funcion = función a ejecutar.
"""
class Temporizador(Thread):
    def __init__(self, hora, delay, funcion):
        super(Temporizador, self).__init__()
        self._estado = True
        self.hora = hora
        self.delay = delay
        self.funcion = funcion

    def stop(self):
        self._estado = False

    def run(self):
        aux = datetime.strptime(self.hora, '%H:%M:%S')
        hora = datetime.now()
        hora = hora.replace(hour = aux.hour, minute=aux.minute, second=aux.second, microsecond = 0)
        if hora <= datetime.now():
            hora += timedelta(days=1)

        while self._estado:
            if hora <= datetime.now():
                self.funcion()
                hora += timedelta(days=1)
            sleep(self.delay)
