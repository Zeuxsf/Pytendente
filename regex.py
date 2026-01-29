import re

string = "Alexandre"

padrao = re.compile("Alexandre")

re.fullmatch(padrao, string)