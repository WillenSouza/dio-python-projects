print("Documento de entrada e saída")

nome = input("Digite seu nome: ")
print(f"Olá {nome}, seja bem-vindo ao curso de Python")
idade = input("Digite sua idade: ")
print(f"Você tem {idade} anos")

print(nome, end=f", ({idade} anos) \n")
print(nome, idade, sep=" - ")