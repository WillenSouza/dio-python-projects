# Verifica se o ano é bisexto

def verificador_ano_bissexto():
    ano = int(input())
    ano = "SIM" if ((ano % 4 == 0) and (ano %100 !=0)) or (ano % 400 == 0) else "NÃO"
    print(ano)

verificador_ano_bissexto()