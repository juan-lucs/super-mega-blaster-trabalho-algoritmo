def busca_binaria(lista, alvo):
    #lembrando: essa busca precisa receber uma lista ORDENADA, se não morre tudo
    esquerdola = 0
    direitola = len(lista) - 1

    while esquerdola <= direitola:
        centro = (esquerdola + direitola) // 2

        if lista[centro] == alvo:
            return centro
        elif lista[centro] < alvo:
            esquerdola = centro + 1
        else:
            direitola = centro - 1

    return -1


def BuscaLinearSentinela(lista, alvo):
    #receber uma lista bagunçada
    #adicionar o alvo ao final dela (chamado sentinela)
    #começar uma comparação do alvo com todos os valores
    #quando achar preciso verificar a posição (ou indice), se for a mesma que a sentinela, o valor não está na lista e retonar -1
    # se estiver na lsita retorna a posicao dela (claro idiota)
    lista.append(alvo)
    posicaoSentinela = len(lista) - 1
    i = 0
    while lista[i] != alvo:               # basicamente isso vai percorrer até eu achar um valor igual ao "alvo", 
                                                # lembrando que a sentinela GARANTE que esse valor existe na listaC
        i += 1
    if i != posicaoSentinela:
        lista.pop(alvo) # remove a sentinela da lista, para não alterar a lista original
        return i, lista[i]

    else: 
        lista.pop(alvo) # remove a sentinela da lista, para não alterar a lista original
        return -1, 0

        # Não se usa esse código de baixo, porque ele verifica sempre se a lista já acabou, e isso atrasa na busca

        # for i in len(listaCopia):
        #if listaCopia[i] == alvo:
        #    if i == posicaoSentinela:
        #        return -1
        #return i