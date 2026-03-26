coders = {
    1: {
        "id": 1048229292,
        "nombre": "Jander",
        "apellido": "Arguello",
        "edad": 30,
        "nvlIngles": "-A0"
    },
    2: {
        "id": 1048229296,
        "nombre": "Luisa",
        "apellido": "De la Rosa",
        "edad": 19,
        "nvlIngles": "C30"
    },
    3: {
        "id": 1048229297,
        "nombre": "Maria",
        "apellido": "Sanchez",
        "edad": 19,
        "nvlIngles": "C1"
    }
}

'''print(coders)

nombre = input("dig un nombre: ")

#Nuevo coder

coders[4] = {"id":100203033,"nombre":nombre, "apellido":"Guzman","edad": 20, "nvlIngles": "B2"}

print("imprimiendo luego de añadir otro coder\n")

print(coders)

print("Buscando el nombre de un coder especifico")

print(coders[4])

print("Buscando con el metodo get")

print(coders.get(11, "No encontrado"))



print("Buscando por numero de documento")

busqueda_id = 1048229292
coder_encontrado = None

for llave, coder in coders.items():
    if coder["id"] == busqueda_id:
        coder_encontrado = coder

print(coder_encontrado)


for j, k in coders.items():
    if k["id"] == busqueda_id:
        print("Encontrado")
'''


def buscar_elemento (coders, coder):
    if coder in coders:
        return coders[coder]
    else:
        return "Coder no encontrado"
    
def eliminar_elemento(coders, coder):
    if coder in coders:
        del coders[coder]
        return "Coder eliminado"
    else:
        return "Coder no existe"
    
busqueda = buscar_elemento(coders, 1)
print(busqueda)

borrar = eliminar_elemento(coders, 2)
print(borrar)

for coder, valor in coders.items():
  print(coder, "-", valor)




