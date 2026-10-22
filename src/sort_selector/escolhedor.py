"""escolher(v) e ordenar(v).

Restrição do enunciado: olhar os dados tem custo. Se `escolher` percorrer a
lista mais de uma vez, pode anular o ganho. Use poucas passadas, ou amostragem.
"""

from .metodos import METODOS


def escolher(v):
    """Olha a lista e devolve o NOME do método mais adequado (chave de METODOS)."""
    # TODO
    raise NotImplementedError


def ordenar(v):
    """Chama escolher(v) e executa o método escolhido."""
    return METODOS[escolher(v)](v)
