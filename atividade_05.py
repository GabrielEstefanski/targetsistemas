# recebe a string a ser invertida
string = input("Digite a string a ser invertida: ")

# converte a string para uma lista de caracteres
lista = list(string)

# inverte a ordem da lista
for i in range(len(lista)//2):
    temp = lista[i]
    lista[i] = lista[len(lista)-i-1]
    lista[len(lista)-i-1] = temp

# converte a lista de volta para uma string
string_invertida = "".join(lista)

# imprime a string invertida
print("String invertida:", string_invertida)