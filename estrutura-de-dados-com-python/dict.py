print("Dicionários em Python".center(70, "-"))

pessoa = {
    "nome": "Willen",
    "idade": 22,
    "cidade": "São Paulo"
}

print(pessoa)
print(pessoa["nome"])  # Acessando o valor associado à chave "nome"
print(pessoa["nome"], pessoa["idade"])

pessoa2 = dict(nome="Luzia", idade=50, cidade="Rio de Janeiro")  # Criando um dicionário usando a função dict
print(pessoa2)

pessoa["profissão"] = "Desenvolvedor"  # Adicionando um novo par chave-valor ao dicionário
print(pessoa)

for chave in pessoa:
    print(f"A chave é {chave} e o valor é {pessoa[chave]}.")

contatos ={
    "camila@gmail.com": {"nome": "Camila", "telefone": "123456789"},
    "izabela@gmail.com": {"nome": "Izabela", "telefone": "333333333"},
    "vitor@gmail.com": {"nome": "Vitor", "telefone": "555555555"}
}
print(contatos)
print(contatos["camila@gmail.com"]["telefone"])  # Acessando o telefone de Camila

for chave, valor in contatos.items():
    print(chave, valor)  # Imprime a chave e o valor correspondente para cada item no dicionário contatos

print("Métodos de dicionários".center(70, "-"))

lista_telefonica = {
    "Willen": "123456789",
    "Luzia": "666666666",
    "Camila": "555555555",
    "Izabela": "333333333"
}

copia_lista = lista_telefonica.copy()  # Criando uma cópia do dicionário lista_telefonica
print(copia_lista)

print(lista_telefonica["chave"]) # quando chamado uma chave que não existe, o Python gera um erro do tipo KeyError

print(lista_telefonica.get("chave"))  # O método get retorna None quando a chave não existe, evitando um erro
print(lista_telefonica.get("Willen",{"Não encontrado"}))  # O método get retorna o valor associado à chave "Willen", ou "Não encontrado" se a chave não existir
print(lista_telefonica.get("chave",{"Não encontrado"}))  # O método get retorna "Não encontrado" porque a chave "chave" não existe no dicionário lista_telefonica

print(lista_telefonica.items()) # O método items retorna uma visão dos itens do dicionário como pares chave-valor, permitindo iteração sobre eles
print(lista_telefonica.keys())  # O método keys retorna uma visão das chaves do dicionário
print(lista_telefonica.values())  # O método values retorna uma visão dos valores do dicionário

lista_telefonica.pop("Willen")  # O método pop remove o item com a chave "Willen" do dicionário lista_telefonica e retorna seu valor
print(lista_telefonica.pop("chave", "Não encontrado"))  # O método pop tenta remover o item com a chave "chave", mas como ela não existe, retorna "Não encontrado"
print(lista_telefonica)

lista_telefonica.popitem()  # O método popitem remove os itens na seguencia inversa de inserção, ou seja, o último item adicionado é o primeiro a ser removido
print(lista_telefonica)

lista_telefonica.setdefault("Vitor", "555555555")  # O método setdefault adiciona o par chave-valor "Vitor": "555555555" ao dicionário lista_telefonica se a chave "Vitor" não existir, caso contrário, retorna o valor associado à chave "Vitor"
print(lista_telefonica)

lista_telefonica.setdefault("Camila", "000000000")  # O método setdefault não altera o valor associado à chave "Camila" porque ela já existe no dicionário lista_telefonica
print(lista_telefonica)

lista_telefonica.update({"Luzia": "987654321"})  # O método update atualiza o dicionário lista_telefonica com os pares chave-valor fornecidos, sobrescrevendo os valores existentes para as chaves "Vitor" e "Luzia"
print(lista_telefonica)

print("Vitor" in lista_telefonica)  # O operador in verifica se a chave "Vitor" existe no dicionário lista_telefonica, retornando True ou False
print("Hellen" in lista_telefonica)  # O operador in verifica se a chave "Hellen" existe no dicionário lista_telefonica, retornando True ou False

del lista_telefonica["Luzia"]  # O comando del remove o item com a chave "Luzia" do dicionário lista_telefonica
print(lista_telefonica)
# del lista_telefonica["chave"] [ ] também pode ser usado para remover um item, mas se a chave não existir, o Python gera um erro do tipo KeyError

lista_telefonica.clear()  # O método clear remove todos os itens do dicionário lista_telefonica, deixando-o vazio