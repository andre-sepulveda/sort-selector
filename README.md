# sort-selector

Projeto da disciplina Estruturas de Dados Avançadas: um ordenador que **olha os dados e escolhe o método de ordenação mais adequado**.

Os métodos reunidos são inserção, intercalação, rápida (pivô aleatório), híbrida, contagem e base. A função `escolher(v)` decide qual usar, e `ordenar(v)` chama `escolher` e executa.

## Instalação

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Rodar os testes

```bash
pytest
```

## Refazer as medições

> A ser preenchido quando o `benchmark.py` estiver pronto: comando exato, parâmetros (tamanhos, repetições, semente) e onde a saída é gravada.

```bash
python medicao/benchmark.py
```