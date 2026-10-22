"""Os seis métodos de ordenação do semestre.

Todos recebem uma lista e devolvem uma NOVA lista ordenada, sem alterar a
original. Assim o benchmark pode reutilizar a mesma entrada em todos os métodos.
"""


def insercao(v):
    # TODO
    raise NotImplementedError


def intercalacao(v):
    # TODO
    raise NotImplementedError


def rapida(v):
    """Quicksort com pivô aleatório."""
    # TODO
    raise NotImplementedError


def hibrida(v):
    """Intercalação (ou rápida) que troca para inserção em subvetores pequenos."""
    # TODO
    raise NotImplementedError


def contagem(v):
    """Contagem. Atenção: memória proporcional à faixa de valores."""
    # TODO
    raise NotImplementedError


def base(v):
    """Radix sort, um dígito por vez, com passada estável."""
    # TODO
    raise NotImplementedError


METODOS = {
    "insercao": insercao,
    "intercalacao": intercalacao,
    "rapida": rapida,
    "hibrida": hibrida,
    "contagem": contagem,
    "base": base,
}
