from fuzzywuzzy import process, fuzz

opcoes = ["ovo", "galinha", "hortelã"]

resultado = process.extractBests("Quem veio primeiro? o ovo? ou a galinha?", opcoes, score_cutoff=50)

print(resultado)