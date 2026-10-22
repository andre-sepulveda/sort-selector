"""Geradores dos quatro cenários de medição.

Cada gerador recebe o tamanho n e uma semente, para que as medições sejam
reproduzíveis.
"""


def aleatorio_chaves_grandes(n, semente=0):
    # TODO
    raise NotImplementedError


def faixa_estreita(n, semente=0):
    # TODO
    raise NotImplementedError


def quase_ordenado(n, semente=0):
    # TODO
    raise NotImplementedError


def lista_minuscula(n=16, semente=0):
    # TODO
    raise NotImplementedError


CENARIOS = {
    "aleatorio_chaves_grandes": aleatorio_chaves_grandes,
    "faixa_estreita": faixa_estreita,
    "quase_ordenado": quase_ordenado,
    "lista_minuscula": lista_minuscula,
}
