print("Conjuntos em Python".center(70, "-"))

lista = [1, 2, 3, 4, 5, 5, 6]
conjunto = set(lista)  # Criando um conjunto a partir de uma lista
print(conjunto)  # Imprime o conjunto, que não contém elementos duplicados

# ter cuidado ao trabalhar com set pois ele não mantém a ordem dos elementos e não permite acesso por índice

numeros = {1, 2, 3, 4, 5}  # Criando um conjunto diretamente
print(numeros)

conjunto.add(6)  # Adiciona o número 6 ao conjunto
print(conjunto)

numeros = list(numeros)  # Convertendo o conjunto de volta para uma lista
print(numeros)

carros = {"Fusca", "Gol", "Corsa", "Palio"}
for indice, carro in enumerate(carros):
    print(f"O carro na posição {indice} é {carro}.")

conjunto1 = {1,2}
conjunto2 = {4,3, 2}

print(conjunto1.union(conjunto2))  # União dos conjuntos
print(conjunto1.intersection(conjunto2))  # Interseção dos conjuntos
print(conjunto1.difference(conjunto2))  # Diferença dos conjuntos

print(conjunto1.issubset(conjunto2))  # Verifica se conjunto1 é um subconjunto de conjunto2
print(conjunto1.issuperset(conjunto2))  # Verifica se conjunto1 é um superconjunto de conjunto2
print(conjunto1.symmetric_difference(conjunto2))  # Elementos que estão em conjunto1 ou conjunto2, mas não em ambos

print(conjunto1.isdisjoint(conjunto2))  # Verifica se os conjuntos são disjuntos (sem elementos em comum)

conjunto1.add(3)  # Adiciona o número 3 ao conjunto1
conjunto1.add(3)  # Tentar adicionar o número 3 novamente não terá efeito, pois conjuntos não permitem duplicatas
print(conjunto1.discard(2))  # Remove o número 2 do conjunto1, se existir
print(conjunto1)
conjunto1.pop()  # Remove e retorna um elemento aleatório do conjunto1
print(conjunto1)

print(len(conjunto1))  # Retorna o número de elementos no conjunto1
print(3 in conjunto1)  # Verifica se o número 3 está presente no conjunto1