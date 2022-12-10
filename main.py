import json

with open('colors.txt') as f:
    data = f.readlines()
    
colors = dict()    

for line in data:
    
    line = line.strip().replace(";", "")
    key, value = line.split(":")
    value = value.replace("\n", '' ).strip()
    colors[key] = value.replace(";", '' )

 
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(colors, f, ensure_ascii=False, indent=4)
    
