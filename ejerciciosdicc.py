# Ejercicios de diccionario

nombre = input("Ingrese su nombre: ").strip()
edad = input("Ingrese su edad: ").strip()
direc = input("Ingrese su dirección: ").strip()
telf = input("Ingresa tu telefono: ").strip()

usuarios = {"Nombre": nombre, "Edad": edad, "Direccion": direc, "telefono": telf}

print(usuarios)