#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Playlist - Ejecute "ayuda" para más información
"""
from lista import Lista
from estante import Estante
from repl import REPL
from repl import strip


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": self.salir
        }
        archivo = "datos.db"
        introduccion = strip(__doc__)
        self.lista = Estante(archivo)
        if not self.lista.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, cancion, artista, album, anho, genero):
        """
        Agrega un registro a la lista.

        cancion   -- nombre de la cancion. Se usará como clave.
        artista  -- nombre del artista.
        album    -- nombre del album donde se encuentra la cancion
        anho     -- anho en el cual se lazo el album
        genero   -- estilo musical
        """
        self.lista[cancion] = Lista(cancion, artista, album, anho, genero)

    def borrar(self, cancion):
        """
        Borra un registro de la agenda.

        nombre -- Nombre del contacto que se desea borrar de la agenda.
        """
        del self.lista[cancion]

    def mostrar(self, cancion):
        """
        Retorna un registro de la agenda.

        nombre -- Nombre del contacto que se desea mostrar.
        """
        return self.lista[cancion]

    def listar(self):
        """
        Retorna un generador con todos los registros de la agenda.

        Este comando no requiere de parámetros.
        """
        return (self.lista[cancion]
                for cancion in sorted(self.lista))

    def buscar(self, cadena):
        """
        Retorna un generador con los registros que contienen una cadena.

        cadena -- Nombre o parte del nombre que se desea buscar en la agenda.
        """
        return (self.lista[cancion]
                for cancion in sorted(self.lista)
                if cadena in cancion)

    def ayuda(self, comando=None):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [..]\n" + \
                     "Comandos: " + \
                     ", ".join(sorted(self.comandos.keys()))
        return salida

    def salir(self):
        """
        Sale de la aplicación.

        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()
