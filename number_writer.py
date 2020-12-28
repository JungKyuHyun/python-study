import json

numbers = [2,3,4,5,6]

fileName = 'text_files/numbers.json'

with open(fileName, 'w') as f:
    json.dump(numbers, f)