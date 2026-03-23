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

print("Métodos da classe list:".center(70, "-"))

lista = []

lista.append(1)  # Adiciona o número 1 à lista

lista.clear()  # Limpa a lista, removendo todos os elementos

lista_2 = lista.copy()  # Cria uma cópia da lista

print(id(lista)) 
print(id(lista_2))  

lista.clear()

lista = [1, 1, 2, 3, 4, 4, 4]

print(lista.count(4))  # Conta quantas vezes o número 4 aparece na lista

lista.extend(["Python", "Java", "C++"])  # Adiciona os elementos de outra lista à lista atual

print(lista)

print(lista.index("Python"))  # Retorna o índice do primeiro elemento "Python" na lista

lista.pop()  # Remove e retorna o último elemento da lista
lista.pop(0)  # Remove e retorna o elemento no índice 0 (primeiro elemento)
print(lista)

lista.reverse()  # Inverte a ordem dos elementos na lista
print(lista)

lista.remove(4)  # Remove a primeira ocorrência do número 4 na lista
print(lista)

lista.clear()
lista = ["banana", "maçã", "laranja", "abacaxi", "uva"]
lista.sort()  # Ordena os elementos da lista em ordem crescente

print(lista)        


lista.sort(reverse=True)  # Ordena os elementos da lista em ordem decrescente
print(lista)

lista.sort(key=lambda x: len(x))  # Ordena os elementos da lista pelo comprimento de cada elemento

print(len(lista))  # Retorna o número de elementos na lista