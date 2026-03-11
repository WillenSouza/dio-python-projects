valor = "15.50"
print(float(valor))
print(int(float(valor)))
print(float(100))

TAXA_MAQUININHA = 0.15
valor_final = TAXA_MAQUININHA + float(valor)

menssagem = f"O valor da sua compra é R${valor} e o valor final com a taxa da maquininha é R${valor_final}"
print(menssagem)

valor = int(float(valor))
print(valor / 2)
print(valor // 2)
print(type(valor))
print(type(menssagem))
print(type(TAXA_MAQUININHA))