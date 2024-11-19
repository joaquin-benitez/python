texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
print (texto)

new_texto = texto.split("&")
print (new_texto)

# Usar map para capitalizar la primera letra de cada frase
frases_capitalizadas = list(map(lambda frase: frase[0].upper() + frase[1:] if frase else '', new_texto))
# Mostrar el resultado
print("\n".join(frases_capitalizadas))

print(type(new_texto))

