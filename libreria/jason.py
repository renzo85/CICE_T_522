import json

objectJS = '{"name":"Vito"}'
dict_python = json.loads(objectJS)

from_dict = json.dumps(dict_python) #es para pasarlo del json dict_python al diccionario from_dict
print(from_dict) #from_dict es un string que puede ser un diccionario