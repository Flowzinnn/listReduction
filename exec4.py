def indice_maior_elemento(lista, indice_atual=0, indice_max=0):
    if indice_atual == len(lista):
        return indice_max

    if lista[indice_atual] > lista[indice_max]:
        indice_max = indice_atual

    return indice_maior_elemento(lista, indice_atual + 1, indice_max)

lista_teste = [1, 28, 9, 15, 5, 3, 2]
indice = indice_maior_elemento(lista_teste)
print(f"O maior elemento é {lista_teste[indice]}, que está no índice {indice}")
