from time import perf_counter_ns # bagulho de medir tempo
import random
from buscas import *
from ordenacao import *

gerador = random.Random(42)
dados = gerador.sample(range(2_000), 1_000) # na teoria isso
                                                #faz exatamente 1.000 sorteios aleatorios pra fazer a lista, um para cada posição.


objetivo = dados[len(dados)//2] # vai pegar o número do meio da lista NÃO ordenada, no cao o numero da posicao 500

# A lista já está ordenada quando começa a medição da binria
dadosOrdenados = sorted(dados)

def medirBuscaBinaria():
    momentoInicial = perf_counter_ns()
    busca_binaria(dadosOrdenados, objetivo)
    return perf_counter_ns() - momentoInicial

def medirSelectionSort() :
    copiaDados = dados.copy() # uso isso porque a funcao de selection altera a lista na memoria, ao inves de criar uma nova lista
                            # e se eu apenas usar o =, ambas as variaveis vao apontar para a mesma lista na memoria
    momentoInicial = perf_counter_ns() # essa função não mede tempo, mas pega o momento exato do relógio
    listaOrdenada = selection_sort(copiaDados)
    momentoAposOrdenar = perf_counter_ns()
    busca_binaria(listaOrdenada, objetivo) # precisa me devolver o indice do numero que eu quero, na lista já ordenada pela função de antes
    momentoFim = perf_counter_ns()
    tempoDeOrdenacao = momentoAposOrdenar - momentoInicial
    tempoDeBusca = momentoFim - momentoAposOrdenar
    tempoTotal = momentoFim - momentoInicial
    return tempoDeOrdenacao, tempoDeBusca, tempoTotal

def medirMergeSort() :
    copiaDados = dados.copy()  # tecnicamente eu não preciso fazer isso aqui, já que a função do merge não altera a lista na memória, mas vamos para ficar mais fácil
    momentoInicial = perf_counter_ns()
    listaOrdenada = merge_sort(copiaDados)
    momentoAposOrdenar = perf_counter_ns()
    busca_binaria(listaOrdenada, objetivo) 
    momentoFim = perf_counter_ns()
    tempoDeOrdenacao = momentoAposOrdenar - momentoInicial
    tempoDeBusca = momentoFim - momentoAposOrdenar
    tempoTotal = momentoFim - momentoInicial
    return tempoDeOrdenacao, tempoDeBusca, tempoTotal

def medirInsertionSort():
        copiaDados = dados.copy() 
        momentoInicial = perf_counter_ns()
        listaOrdenada = insertion_sort(copiaDados)
        momentoAposOrdenar = perf_counter_ns()
        busca_binaria(listaOrdenada, objetivo) 
        momentoFim = perf_counter_ns()
        tempoDeOrdenacao = momentoAposOrdenar - momentoInicial
        tempoDeBusca = momentoFim - momentoAposOrdenar
        tempoTotal = momentoFim - momentoInicial
        return tempoDeOrdenacao, tempoDeBusca, tempoTotal

def medirBuscaLinearSentinela():
     copiaDados = dados.copy()
     momentoInicial = perf_counter_ns()
     BuscaLinearSentinela(copiaDados, objetivo) # Essa busca NÃO precisa da ordenação, ela consegue procurar em uma lista bagunçada
     momentoFinal = perf_counter_ns()
     return momentoFinal - momentoInicial



# amigos confesso que tudo aqui pra baixo foi IA, eu não entendi uma porra dessas repetições
repeticoes = 10

def repetir(nome, medir):
    soma_ordenacao = 0
    soma_busca = 0
    soma_total = 0

    for i in range(repeticoes):
        ordenacao, busca, total = medir()
        soma_ordenacao += ordenacao
        soma_busca += busca
        soma_total += total

    print(nome)
    print("  Média da ordenação:", soma_ordenacao / repeticoes, "ns")
    print("  Média da busca:", soma_busca / repeticoes, "ns")
    print("  Média do total:", soma_total / repeticoes, "ns")

repetir("Selection Sort", medirSelectionSort)
repetir("Insertion Sort", medirInsertionSort)
repetir("Merge Sort", medirMergeSort)

# Cada busca isolada devolve apenas o tempo da busca.
def repetirBusca(nome, medir):
    soma = 0
    for _ in range(repeticoes):
        soma += medir()
    print(nome)
    print("  Média da busca:", soma / repeticoes, "ns")

repetirBusca("Busca Binária (lista já ordenada)", medirBuscaBinaria)
repetirBusca("Busca com Sentinela", medirBuscaLinearSentinela)
