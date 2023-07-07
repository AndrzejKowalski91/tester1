import json

with open('dane.json','r') as file:
    data = json.load(file)

print(data['members'][2]['powers'][3])