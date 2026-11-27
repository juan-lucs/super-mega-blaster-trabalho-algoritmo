from buscas import BuscaLinearSentinela, busca_binaria
from medicoes import medir_sort_nativo
from ordenacao import insertion_sort, merge_sort, selection_sort


def mostrar_resultado(caso, esperado, recebido):
    if recebido == esperado:
        status = "OK"
    else:
        status = "ERRO"

    print(f"{caso} | esperado: {esperado} | recebido: {recebido} | {status}")


def verificar_ordenacoes(caso, lista, esperado):
    mostrar_resultado(f"Selection Sort, {caso}", esperado, selection_sort(lista.copy()))
    mostrar_resultado(f"Insertion Sort, {caso}", esperado, insertion_sort(lista.copy()))
    mostrar_resultado(f"Merge Sort, {caso}", esperado, merge_sort(lista.copy()))


if __name__ == "__main__":
    print("Ordenações")
    verificar_ordenacoes("lista vazia", [], [])
    verificar_ordenacoes("um elemento", [7], [7])
    verificar_ordenacoes("lista ordenada", [1, 2, 3], [1, 2, 3])
    verificar_ordenacoes("lista invertida", [3, 2, 1], [1, 2, 3])
    verificar_ordenacoes("repetidos e negativo", [3, -1, 3, 0], [-1, 0, 3, 3])

    print("\nBusca binária (resultado: índice)")
    ordenada = [-7, 9, 20]
    mostrar_resultado("Melhor caso: alvo no meio", 1, busca_binaria(ordenada, 9))
    mostrar_resultado("Alvo no início", 0, busca_binaria(ordenada, -7))
    mostrar_resultado("Alvo no fim", 2, busca_binaria(ordenada, 20))
    mostrar_resultado("Alvo ausente", -1, busca_binaria(ordenada, 8))
    mostrar_resultado("Lista vazia", -1, busca_binaria([], 20))

    print("\nBusca com sentinela (resultado: índice e valor)")
    casos_sentinela = [
        ("Melhor caso: alvo no início", [0, 9, -7], 0, (0, 0)),
        ("Primeira ocorrência do alvo", [5, 9, 9], 9, (1, 9)),
        ("Alvo no fim", [20, 9, -7], -7, (2, -7)),
        ("Pior caso: alvo ausente", [20, 9, -7], 40, (-1, 0)),
        ("Lista vazia", [], 20, (-1, 0)),
    ]

    for caso, lista, alvo, esperado in casos_sentinela:
        entrada = lista.copy()
        recebido = BuscaLinearSentinela(entrada, alvo)
        mostrar_resultado(caso, esperado, recebido)
        mostrar_resultado("Lista após a busca", lista, entrada)

    print("\nMedição do list.sort()")
    lista = [3, -1, 3, 0]
    tempo = medir_sort_nativo(lista, 3)
    mostrar_resultado("Tempo é um inteiro não negativo", True, isinstance(tempo, int) and tempo >= 0)
    mostrar_resultado("Lista após a medição", [3, -1, 3, 0], lista)
