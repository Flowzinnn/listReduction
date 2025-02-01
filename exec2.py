
def soma_lista_aninhada(lista):
    soma = 0
    for item in lista:
        if isinstance(item, list):
            soma += soma_lista_aninhada(item)
        else:
            soma += item
    return soma
    

   
myList = [1, [2, 3], [4, [5]]]
result = soma_lista_aninhada(myList)
print(result)
