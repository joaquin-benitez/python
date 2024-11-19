
#lista para almacenar los hobbies
hobbies = []
#for para obtener 3 hobbies 
for i in range(3):
    hobby = input(f"Introduce el hobby {i+1}: ")
    hobbies.append(hobby)
# Escribir los hobbies en un archivo de texto
with open('hobbies.txt', 'w') as f:
    for hobby in hobbies:
        f.write(hobby + '\n')
print("Los hobbies se han guardado en hobbies.txt con EXITO")