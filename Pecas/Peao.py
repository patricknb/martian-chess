from .Peca import Peca


class Peao(Peca):
    def __init__(self) -> None:
        super().__init__(1,1,'peao')
        self.__img_path1 = "images\Peao_Q1.png"
        self.__img_path2 = "images\Peao_Q2.png"

    def peca(self) -> str:
        return '1'
