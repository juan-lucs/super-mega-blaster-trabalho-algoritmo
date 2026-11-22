def busca_binaria(lista, alvo):
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

lista = [2, 5, 8, 12, 16, 23, 38, 56]

print(busca_binaria(lista, 23)) 
print(busca_binaria(lista, 2))    
print(busca_binaria(lista, 56))   
print(busca_binaria(lista, 10))