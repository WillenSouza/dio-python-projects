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