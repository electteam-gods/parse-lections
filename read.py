import json

f = open('jopa.json', 'r')

print(json.loads(f.read()))