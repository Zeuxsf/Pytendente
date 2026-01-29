import re

string = "Alexandre"

padrao = re.compile("Alexandre")

resultado = re.fullmatch(padrao, string)
print(resultado)