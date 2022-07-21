from .Peca import Peca


class Rainha(Peca):
    def __init__(self) -> None:
        super().__init__(3,0,'rainha')
        self.__img1_path = "images\Rainha_Q1.png"
        self.__img2_path = "images\Rainha_Q2.png"

    def peca(self):
        return '3'