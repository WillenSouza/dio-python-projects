texto = "PersErVerAnça"

print(texto.upper())  # PERSERVERANÇA
print(texto.lower())  # perseverança
print(texto.title())  # Perseverança

texto = "    Bom isso é tudo pessoal! "
print(texto.strip())  # Remove os espaços em branco no início e no final
print(texto.lstrip())  # Remove os espaços em branco no início
print(texto.rstrip())  # Remove os espaços em branco no final

texto = "Programador"
print(texto.replace("a", "o"))  # ProgroModor
print(texto.center(20, "*"))  # ****Programador****
print(texto.count("o"))  # 2

print(".".join(texto))  # P.r.o.g.r.a.m.a.d.o.r
print(texto.split("a"))  # ['Progr', 'm', 'dor']

print("Interpolação de strings:".center(100, "_"))

nome = "Willen"
idade = 22
email = "souzawillen.dev@gmail.com"

print("Muito prazer, meu nome é %s, tenho %d anos e meu email é %s.\n\n" % (nome, idade, email))

print("Muito prazer, meu nome é {}, tenho {} anos e meu email é {}.\n\n".format(nome, idade, email))

print("Muito prazer, meu nome é {0}, tenho {1} anos e meu email é {2}.\n\n".format(nome, idade, email))

print("Muito prazer, meu nome é {n}, tenho {i} anos e meu email é {e}.\n\n".format(n=nome, i=idade, e=email))

print(f"Muito prazer, meu nome é {nome}, tenho {idade} anos e meu email é {email}.\n\n")

PI = 3.14159
print(f"O valor de PI é aproximadamente {PI:.2f}.")  # Delimitando o número de casas decimais para 2

print("Fatiamento de strings:".center(100, "_"))

nome = "Willen Souza"
print(nome[0])  # W
print(nome[1])  # i
print(nome[0:6])  # Willen
print(nome[:6])  # Willen
print(nome[7:])  # Souza
print(nome[-6:])  # Souza
print(nome[::2])  # Wle oa
print(nome[::-1])  # azuoS nelleW

print("Strings multilinhas:".center(100, "_"))

menu = """
========================================
    Menu:
    1.Iniciar  sistema
    2.Configurações
    3.Sair

=======================================
"""

print(menu)