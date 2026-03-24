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