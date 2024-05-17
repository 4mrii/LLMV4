import csv
import json
import random

# Define the templates
templates = [
    {"instruction" : "apa maksud {word}?", 
     "input" : "<noinput>", 
     "output" : "Menurut {edition}, {word} disebut dengan {phonetic} dan ditulis {jawi} di dalam tulisan jawi ialah {description}."},

    {"instruction" : "apakah maksud {word}?", 
     "input" : "<noinput>", 
     "output" : "Menurut {edition}, {word} disebut dengan {phonetic} dan ditulis {jawi} di dalam tulisan jawi ialah {description}."},
    
    {"instruction" : "apakah definisi perkataan ini?", 
     "input" : "{word}", 
     "output" : "Menurut {edition}, {word} disebut dengan {phonetic} dan ditulis {jawi} di dalam tulisan jawi ialah {description}."},
    
    {"instruction" : "apakah definisi perkataan ini?", 
     "input" : "{word}", 
     "output" : "{word}  {phonetic} \n {jawi} bermaksud: \n 1) {description}. \n 2) {description}. \n 3) {description}"},
    
    {"instruction" : "apakah maksud {word}?", 
     "input" : "<noinput>", 
     "output" : "{word}  {phonetic} \n {jawi} bermaksud: \n 1) {description}. \n 2) {description}. \n 3) {description}"}
]

# Read the CSV file
with open('cleaned_V1_filled.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    first_row = next(reader)
    print(first_row)
    data = list(reader)
    


# Convert the data to the Alpaca JSON format
alpaca_data = []
for row in data:
    if ',' in row['description']:
        template = random.choice(templates[3:])
    else:
        template = random.choice(templates[:3])
    alpaca_data.append({
        "instruction": template['instruction'].format(word=row['word']),
        "input": template['input'].format(word=row['word']),
        "output": template['output'].format(word=row['word'], phonetic=row['phonetic'], jawi=row['jawi'], description=row['description'], edition=row['edition'])
    })

# Write the Alpaca JSON data to a file
with open('alpaca_dataV2.json', 'w', encoding='utf-8-sig') as f:
    json.dump(alpaca_data, f, ensure_ascii=False, indent=4)
