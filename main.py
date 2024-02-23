import json



with open('coffe.json', 'r') as coffe:
    data = json.load(coffe)
    data["numero"] += 2

# Grava o número de volta no arquivo
with open('coffe.json', 'w') as coffe:
    json.dump(data, coffe)



