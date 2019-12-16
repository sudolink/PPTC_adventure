import pathlib

path_to_rooms = pathlib.Path("./assets/rooms/")

class room():
    def __init__(self,bg):
        self.bg = bg
        self.rect = self.bg.get_rect()
