from time import perf_counter_ns
import random
from buscas import *
from ordenacao import *

REPETICOES = 10
TAMANHOS = [1_000, 10_000, 50_000, 100_000]
gerador = random.Random(42)

def sortear(tamanho: int) -> tuple[list[int], int]:
    lista = gerador.sample(range(tamanho * 2), tamanho)
    objetivo = lista[tamanho // 2]  # número do meio da lista NÃO ordenada
    return lista, objetivo


def medir_selection_sort(lista: list, objetivo: int) -> int:
    copia = lista.copy()  #SELECTION altera a lista da memória, então usamos uma cópia
    inicio = perf_counter_ns()
    ordenada = selection_sort(copia)
    busca_binaria(ordenada, objetivo)
    return perf_counter_ns() - inicio


def medir_insertion_sort(lista: list, objetivo: int) -> int:
    #INSERTION também altera a lista da memória, então usamos uma cópia
    copia = lista.copy()
    inicio = perf_counter_ns()
    ordenada = insertion_sort(copia)
    busca_binaria(ordenada, objetivo)
    return perf_counter_ns() - inicio


def medir_merge_sort(lista: list, objetivo: int) -> int:
    inicio = perf_counter_ns()
    ordenada = merge_sort(lista)  # não altera a original, não precisa de cópia
    busca_binaria(ordenada, objetivo)
    return perf_counter_ns() - inicio


def medir_busca_binaria(lista: list, objetivo: int) -> int:
    ordenada = sorted(lista)  # ordena ANTES do tempo: aqui medimos só a busca
    inicio = perf_counter_ns()
    busca_binaria(ordenada, objetivo)
    return perf_counter_ns() - inicio


def medir_busca_sentinela(lista: list, objetivo: int) -> int:
    inicio = perf_counter_ns()
    BuscaLinearSentinela(lista, objetivo)  # funciona na lista bagunçada
    return perf_counter_ns() - inicio


def repetir(medir, lista: list, objetivo: int) -> float:
    soma = 0
    for x in range(REPETICOES):
        soma += medir(lista, objetivo)
    return soma / REPETICOES


for n in TAMANHOS:
    lista, objetivo = sortear(n)

    print(f"\nLista de {n} elementos:")

    print(f"Selection Sort + busca {repetir(medir_selection_sort, lista, objetivo) / 1_000_000:>12,.3f} ms")
    print(f"Insertion Sort + busca {repetir(medir_insertion_sort, lista, objetivo) / 1_000_000:>12,.3f} ms")
    print(f"Merge Sort + busca {repetir(medir_merge_sort, lista, objetivo) / 1_000_000:>12,.3f} ms")
    print(f"Busca binária (só busca) {repetir(medir_busca_binaria, lista, objetivo) / 1_000_000:>12,.3f} ms")
    print(f"Busca Linear com sentinela {repetir(medir_busca_sentinela, lista, objetivo) / 1_000_000:>12,.3f} ms")
