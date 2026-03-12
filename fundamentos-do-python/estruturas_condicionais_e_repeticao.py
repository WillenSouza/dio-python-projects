print("__________Estruturas Condicionais_________")

idade = int(input("Digite uma idade: "))

if idade < 0 or idade > 120:
    print("Idade inválida!")
elif idade >=18 and idade <= 55:
    print("Você já é adulto!")
elif idade < 18:
    print("Você é menor de idade!")
else: 
    print("Você é idoso!")


valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = valor_1 + valor_2
elif operacao == "-":
    resultado = valor_1 - valor_2
elif operacao == "*":
    resultado = valor_1 * valor_2
elif operacao == "/":
    if valor_2 != 0:
        resultado = valor_1 / valor_2
    else:
        resultado = "Erro: Divisão por zero!"
print(f"Resultado: {resultado}")    

resultado = "sucesso"
validacao = resultado if resultado == "sucesso" else "Resultado negativo!"  # Operador ternário
print(validacao)


print("__________Estruturas de Repetição_________")

VOGAIS = "AEIOU"
palavra = input("Digite uma palavra: ")

for letras in palavra:
    if letras.upper() in VOGAIS:
        print(f"{letras} é uma vogal!")

valor = int(input("Digite um número para calcular a tabuada: "))

for numero in range(0, 11):
    resultado = numero * valor
    print(f"{numero} x {valor} = {resultado}")


print("Olá, bem vindo ao menu de opções!")
print("Digite 1 para fazer uma transferência\n Digite 2 para ver o saldo \n Digite 0 para sair")
opcao = -1
while opcao != 0:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Você escolheu fazer uma transferência!")
    elif opcao == 2:
        print("Você escolheu ver o saldo!")
    elif opcao == 0:
        print("Saindo do menu, até mais!")
    else:
        print("Opção inválida, tente novamente!")


print("Olá, bem vindo ao menu de opções!")
print("Digite 1 para fazer uma transferência\n Digite 2 para ver o saldo \n Digite 0 para sair")
opcao = -1
while True:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Você escolheu fazer uma transferência!")
    elif opcao == 2:
        print("Você escolheu ver o saldo!")
    elif opcao == 0:
        break
    else:
        print("Opção inválida, tente novamente!")
