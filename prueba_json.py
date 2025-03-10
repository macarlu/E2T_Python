import json
'''
contactos = open("contactos.json","r")# en modo lectura
datos = json.load(contactos)
contactos.close()'''

with open("contactos.json","r") as ct:#sin alias no se puede utilizar esta forma
    datos =json.load(ct)

print(datos)

