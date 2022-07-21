from Posicao import Posicao

class Quadrante():
    def __init__(self) -> None:
        self.__posicoes = [[Posicao(), Posicao(), Posicao(), Posicao()],
                           [Posicao(), Posicao(), Posicao(), Posicao()],
                           [Posicao(), Posicao(), Posicao(), Posicao()],
                           [Posicao(), Posicao(), Posicao(), Posicao()]]
        self.__pecas = 0
        self.__pontuacao = 0
        self.__turno = False

    def iniciar_quadrante(self, lista_posicao_peca:list):
        for i in range(len(lista_posicao_peca)):
            self.__posicoes[lista_posicao_peca[i][0]][lista_posicao_peca[i][1]].definir_ocupante(lista_posicao_peca[i][2])
    
    def estado_atual(self):
        estado_atual_do_quadrante = []
        for i in range(4):
            linha = []
            for j in range(4):
                linha.append(self.__posicoes[i][j].pegar_atual_ocupante())
            
            estado_atual_do_quadrante.append(linha)
        
        return estado_atual_do_quadrante


    def print_quadrante(self):
        print("{}, {}, {}, {}".format(self.__posicoes[0][0].pegar_atual_ocupante(), self.__posicoes[0][1].pegar_atual_ocupante(), self.__posicoes[0][2].pegar_atual_ocupante(), self.__posicoes[0][3].pegar_atual_ocupante()))
        print("{}, {}, {}, {}".format(self.__posicoes[1][0].pegar_atual_ocupante(), self.__posicoes[1][1].pegar_atual_ocupante(), self.__posicoes[1][2].pegar_atual_ocupante(), self.__posicoes[1][3].pegar_atual_ocupante()))
        print("{}, {}, {}, {}".format(self.__posicoes[2][0].pegar_atual_ocupante(), self.__posicoes[2][1].pegar_atual_ocupante(), self.__posicoes[2][2].pegar_atual_ocupante(), self.__posicoes[2][3].pegar_atual_ocupante()))
        print("{}, {}, {}, {}".format(self.__posicoes[3][0].pegar_atual_ocupante(), self.__posicoes[3][1].pegar_atual_ocupante(), self.__posicoes[3][2].pegar_atual_ocupante(), self.__posicoes[3][3].pegar_atual_ocupante()))

"""

    def selecionar_posicao_peca(linha:int, coluna:int):
        return None

    def obter_posicao(linha:int, coluna:int):
        return #Posicao

    def selecionar_posicao_alvo(linhha:int, coluna:int):
        return None

    def comparar_pecas(p1: Peca, p2: Peca):
        return #bool

    def combinar_pecas(posicao_peca: Posicao, posicao_alvo: Posicao, ocupante1: Peca, ocupante2: Peca):
        return #Peca

    def mover_peca(posicao_peca:Posicao, posicao_alvo:Posicao, ocupante1:Peca):
        return None

    def capturar_peca(posicao_peca:Posicao, posicao_alvo:Posicao, ocupante1:Peca, ocupante2:Peca):
        return None

    def somar_pontos(pontos:int):
        return None

    def zerar_pontuacao():
        return None

    def desativar_turno():
        return None

    def habilitar_turno():
        return None

    def desabilitar_turno():
        return None

    def selecionar_peca(linha:int, coluna:int):
        return #Peca

    def excluir_pecas_combinadas(linha_peca:int, coluna_peca:int, linha_alvo:int, coluna_alvo:int, peca_selecionada:Peca, peca_alvo:Peca):
        return None

    def mover_peca(peca:Peca, linha_peca:int, coluna_peca:int, linha_alvo:int, coluna_alvo:int):
        return None

    def incrementar_pontuacao(peca_alvo:Peca, linha_alvo:int, coluna_alvo:int):
        return None

    def pegar_pontuacao():
        return #int

    def quadrante_vazio():
        return #bool

    def pegar_posicoes():
        return #list
"""