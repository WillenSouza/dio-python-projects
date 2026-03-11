print("_________Operradores Aritméticos_________")

produto_1 = 50
produto_2 = 25

print(produto_1 + produto_2)  # Soma
print(produto_1 - produto_2)  # Subtração
print(produto_1 * produto_2)  # Multiplicação
print(produto_1 / produto_2)  # Divisão
print(produto_1 // produto_2) # Divisão inteira
print(produto_1 % produto_2)  # Módulo (resto da divisão)
print(produto_1 ** produto_2) # Potência

x = 10 ** 2 + 5 * 3 - 8 / 2

print(x)

print("_________Operradores de Comparação_________")

saldo = 1000
saque = 500 

print(saldo > saque)  # Maior que
print(saldo < saque)  # Menor que   
print(saldo >= saque) # Maior ou igual a
print(saldo <= saque) # Menor ou igual a
print(saldo == saque) # Igual a
print(saldo != saque) # Diferente de

print("_________Operradores de Atribuição_________")

saldo = 1000
print(saldo)
saldo += 500  # saldo = saldo + 500
print(saldo)
saldo -= 200  # saldo = saldo - 200 
print(saldo)
saldo *= 2    # saldo = saldo * 2
print(saldo)
saldo /= 4    # saldo = saldo / 4
print(saldo)
saldo //= 2   # saldo = saldo // 2
print(saldo)
saldo %= 3    # saldo = saldo % 3
print(saldo)
saldo **= 3   # saldo = saldo ** 3
print(saldo)

print("_________Operradores Lógicos_________")

print(True and False)  # E lógico
print(True or False)   # Ou lógico
print(not True)        # Negação lógica

comparacao = (saldo > 100) and (saldo < 500)
print(comparacao)
comparacao = (saldo > 100) or (saldo < 500)
print(comparacao)   
comparacao = not (saldo > 100)
print(comparacao)

print("_________Operradores de Identidade_________")

saldo = 1500
limite = 1500

print(saldo is limite)  # Verifica se são o mesmo objeto
print(saldo is not limite)  # Verifica se são objetos diferentes

print("_________Operradores de Associação_________")

amigos = ["Vitor", "Camila", "Izabela"]
local = "Universidade Estadual do Mato Grosso - UNEMAT"

print("Vitor" in amigos)  # Verifica se "Vitor" está na lista de amigos
print("Jaque" not in amigos)  # Verifica se "Jaque" não está na lista de amigos
print("UNEMAT" in local)  # Verifica se "UNEMAT" está na string local