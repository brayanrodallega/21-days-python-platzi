'''
En este ejercicio, se solicita implementar una playlist utilizando un stack en Python.

Se debe crear la clase Playlist con las siguientes propiedades: top, bottom y length, para representar el tope, la base y la longitud de la pila, respectivamente.

La clase Playlist debe tener los siguientes métodos:

    addSong(song): Este método permite agregar una canción a la pila. La canción se agrega en el tope de la pila.
    playSong(): Este método permite reproducir la canción que se encuentra en el tope de la pila y luego eliminarla. Si la pila está vacía, se debe lanzar un error con el mensaje "No hay canciones en la lista".
    getPlaylist(): Este método transforma la pila en una lista (array) que contiene todas las canciones en orden de reproducción, desde la última agregada hasta la primera.

Ejemplo 1: ```txt Input:

playlist = Playlist()

playlist.addSong("Bohemian Rhapsody") playlist.addSong("Stairway to Heaven") playlist.addSong("Hotel California")

Output: print(playlist.playSong()) # Output: "Hotel California" print(playlist.playSong()) # Output: "Stairway to Heaven" print(playlist.playSong()) # Output: "Bohemian Rhapsody" print(playlist.playSong()) # Output: Error: No hay canciones en la lista ``` Ejemplo 2:

Input:

playlist = Playlist()

playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")

print(playlist.getPlaylist())

Output: ["Hotel California", "Stairway to Heaven", "Bohemian Rhapsody"]
'''

# Solución:

from node import Node

class Playlist:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def addSong(self, song):
        new_node = Node(song)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def playSong(self):
        if not self.top:
            raise Exception("No hay canciones en la lista")
        if self.top == self.bottom:
            self.bottom = None
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node.value

    def getPlaylist(self):
        play_list = []
        current_node = self.top
        while current_node:
            play_list.append(current_node.value)
            current_node = current_node.next
        return play_list


# playlist = Playlist()
#
# playlist.addSong("Bohemian Rhapsody")
# playlist.addSong("Stairway to Heaven")
# playlist.addSong("Hotel California")
#
# print(playlist.playSong())
# print(playlist.playSong())
# print(playlist.playSong())
# print(playlist.playSong())


playlist = Playlist()

playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")

print(playlist.getPlaylist())