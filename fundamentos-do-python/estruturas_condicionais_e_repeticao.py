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