# Conta o número de vogais em uma string

def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    cont = 0
    
    for char in texto:
        if char in vogais:
          cont += 1  
    return cont

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")