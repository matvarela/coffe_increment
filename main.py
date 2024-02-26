import json
from datetime import date

hoje = date.today().weekday()

with open('coffe.json', 'r') as coffe:
    data = json.load(coffe)
    
    if hoje < 5: 
        data["numero"] += 2
    else:
        data["numero"] += 1

with open('coffe.json', 'w') as coffe:
    json.dump(data, coffe)
