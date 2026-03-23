animes = ["naruto", "dragon ball", "pokemon"]
print(animes[0])  # Acessando o primeiro elemento da lista
print(animes[:-1])  # Acessando todos os elementos, exceto o último
print(animes[::-1])  # Acessando a lista de trás para frente
print(animes[1:])  # Acessando a lista a partir do segundo elemento
print(animes[0:3:2])  # Acessando a lista do primeiro ao terceiro elemento, pulando de 2 em 2

numeros = list(range(10))  # Criando uma lista de números de 0 a 9
print(numeros)

print("Listas aninhadas:")
listas_aninhadas = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

print(listas_aninhadas)  

print(listas_aninhadas[0])  # Acessando a primeira sublista
print(listas_aninhadas[1][2])  # Acessando o terceiro elemento
print(listas_aninhadas[2][0])  # Acessando o primeiro elemento da terceira sublista
print(listas_aninhadas[::-1])  # Acessando a lista de trás para frente
print(listas_aninhadas[0][-1])
print(listas_aninhadas[-1][0])

print("acessando elementos de uma lista:")

nomes = ["Willen", "Luzia", "Leticia"]

for nome in nomes:
    print(nome, end=" ")  

for i, nome in enumerate(nomes):
    print(f"O nome na posição {i} é {nome}.", end=" ")

for nome in nomes:
    if nome == "Luzia":
        print(f"\nO nome {nome} foi encontrado na lista.")
        break

anos = list(range(2000, 2025))  # Cria uma lista de anos de 2000 a 2024
bisexto = [ano for ano in anos if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)] 
print("\nAnos bissextos entre 2000 e 2024:", bisexto)

quadrado = []
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    quadrado.append(numero ** 2)

print("\nQuadrados dos números:", quadrado)

print("Metodos de listas:".center(70, "-"))

lista = []

lista.append(1)  # Adiciona o número 1 à lista

lista.clear()  # Limpa a lista, removendo todos os elementos

lista_2 = lista.copy()  # Cria uma cópia da lista

print(id(lista)) 
print(id(lista_2))  

lista.clear()

lista = [1, 1, 2, 3, 4, 4, 4]

print(lista.count(4))  # Conta quantas vezes o número 4 aparece na lista