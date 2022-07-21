from Quadrante import Quadrante
from Pecas.Peao import Peao
from Pecas.Drone import Drone
from Pecas.Rainha import Rainha


class Tabuleiro:
    def __init__(self) -> None:
        self.__peao = Peao()
        self.__drone = Drone()
        self.__rainha = Rainha()
        self.__quadrante_a = Quadrante()
        self.__quadrante_b = Quadrante()
        self.__deadlock = False
        self.__partida_em_andamento = False
        self.__estado = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
        self.__tabuleiro_inicial = list
        self.__captura = False
        self.__turnos_deadlock = 0

    def tabuleiro_inicial(self):
        estado_inicial_quadrante_a = [
            [1, 2, self.__peao.peca()],
            [2, 2, self.__peao.peca()],
            [2, 1, self.__peao.peca()],
            [0, 2, self.__drone.peca()],
            [1, 1, self.__drone.peca()],
            [2, 0, self.__drone.peca()],
            [0, 1, self.__rainha.peca()],
            [0, 0, self.__rainha.peca()],
            [1, 0, self.__rainha.peca()]
        ]
        estado_inicial_quadrante_b = [
            [1, 2, self.__peao.peca()],
            [1, 1, self.__peao.peca()],
            [2, 1, self.__peao.peca()],
            [1, 3, self.__drone.peca()],
            [2, 2, self.__drone.peca()],
            [3, 1, self.__drone.peca()],
            [2, 3, self.__rainha.peca()],
            [3, 3, self.__rainha.peca()],
            [3, 2, self.__rainha.peca()]
        ]

        self.__quadrante_a.iniciar_quadrante(estado_inicial_quadrante_a)
        self.__quadrante_b.iniciar_quadrante(estado_inicial_quadrante_b)

    def atualizar_tabuleiro(self):
        estado = []
        estado.append(self.__quadrante_a.estado_atual())
        estado.append(self.__quadrante_b.estado_atual())
        self.__estado = estado

    def print_tabuleiro(self):
        print(self.__estado)
        print(self.__drone.pontos())

    def realizar_jogada(self, posicao_peca:list, posicao_alvo:list):
        return None

    def pedir_deadlock(self):
        self.__deadlock = True

'''
    def selecionar_peca(linha:int, coluna:int):
        return None

    def criar_peca(tipo:int):
        return #Peca

    def tabuleiro_posicao_inicial():
        return None

    def atualizar_estado(estado_quadrante_1:list, estado_quadrante_2:list):
        return None

    def checar_vencedor():
        return None
    
    def alterar_turno():
        return None

    def jogada_valida(posicao_peca:Posicao, posicao_alvo:Posicao, peca:Peca):
        return #boolean

    def estado_inicial():
        return #list

    def restaurar_tabuleiro():
        return #list

    def zerar_deadlock():
        return None

    def desabilitar_deadlock():
        return None

    def incrementar_deadlock():
        return None
    
    def captura_confirmada():
        return None
    
    def checar_captura():
        return #bool

    def zerar_contador_deadlock():
        return None

    def incrementar_contador_deadlock():
        return None

    def pedir_deadlock():
        return None

    def pegar_turno():
        return None

    def incrementar_turno():
        return None

    def alterar_valor_deadlock():
        return None

    def iniciar_partida():
        return None

    def selecionar_peca(linha:int, coluna:int):
        return None

    def selecionar_alvo(linha_alvo:int, coluna_alvo:int, linha_peca:int, coluna_peca:int, peca:Peca):
        return None

    def existe_peca():
        return #bool

    def minha_peca():
        return #bool

    def ocupante_anterior(peca_selecionada:Peca, peca_alvo:Peca):
        return #bool

    def movimento_valido(linha_alvo:int, coluna_alvo:int, linha_peca:int, coluna_peca:int, restricao:str):
        return #bool

    def peca_mesmo_tipo(peca:Peca, peca_alvo:Peca):
        return #[bool, string]

    def criar_nova_peca(grau_peca:str):
        return #Peca

    def notificar_combinacao_invalida():
        return None

    def capturar_peca(peca_selecionada:Peca, peca_alvo:Peca, linha_alvo:int, coluna_alvo:int, linha_peca:int, coluna_peca:int):
        return None

    def sinalizar_captura():
        return None

    def notificar_movimento_invalido():
        return None

    def notificar_peca_pertencente_ao_inimigo():
        return None

    def notificar_peca_deve_ser_selecionada():
        return None

    def incrementar_contador_deadlock():
        return None

    def checar_contador_deadlock():
        return #bool

    def notificar_fim_de_partida_por_deadlock(pontuacao_q1:int, pontuacao_q2:int):
        return None

    def notificar_fim_de_partida(pontuacao_q1:int, pontuacao_q2:int):
        return None

    def proximo_turno():
        return None

    def passar_vez():
        return None

    def mover_peca(peca:Peca, linha_alvo:int, coluna_alvo:int):
        return None

    def esquecer_peca(peca:Peca):
        return None

    def definir_ocupante(ocupante:Peca):
        return None
        '''


T = Tabuleiro()
T.tabuleiro_inicial()
T.print_tabuleiro()
T.atualizar_tabuleiro()
T.print_tabuleiro()
