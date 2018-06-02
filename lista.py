#!/usr/bin/env python3
"""
Módulo Lista: Clase principal (modelo).


"""


class Lista(dict):
    """detalle la informacion de la cancion."""

    def __init__(self, cancion, artista, album, anho, genero):
        """Constructor: Inicializa propiedades de instancia."""
        self.cancion = cancion
        self.artista = artista
        self.album = album
        self.anho = anho
        self.genero = genero

    def __str__(self):
        """Cadena de representación."""
        return "{}-{}-{}-{}-{}".format(self.cancion, self.artista,
                                       self.album, self.anho,
                                       self.genero)


def main():
    """Función principal (ejemplo de uso)."""
    lista = {}

    lista["7 years old"] = Lista("7 years old", "lukas graham",
                                 "lukas graham", "2017", "alternativo")
    lista["a veces vuelvo"] = Lista("a veces vuelvo", "catupecu machu",
                                    "el numero imperfecto", "2004",
                                    "rock")
    lista["angela"] = Lista("angela", "the lumineers", "cleopatra",
                            "2016", "folk")

    for clave in lista:
        print(lista[clave])


if __name__ == "__main__":
    main()
