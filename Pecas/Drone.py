from .Peca import Peca


class Drone(Peca):
    def __init__(self) -> None:
        super().__init__(2,2,'drone')
        self.__img_path1 = "images\Drone_Q1.png"
        self.__img_path2 = "images\Drone_Q2.png"

    def peca(self):
        return '2'