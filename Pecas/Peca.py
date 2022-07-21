from abc import ABC, abstractmethod

class Peca(ABC):
    def __init__(self, pontos, mov, peca) -> None:
        self.__pontos = pontos
        self.__casas_de_movimentacao = mov
        self.__restricao_de_movimento = peca
    
    def pontos(self):
        return self.__pontos

    def casas_de_movimentacao(self):
        return self.__casas_de_movimentacao

    def restricao_de_movimento(self):
        return self.__restricao_de_movimento

