def obtener_generacion(edad):
    if edad >= 77:
        return "Generación Silenciosa (nacidos antes de 1946)"
    elif 58 <= edad <= 76:
        return "Baby Boomers (1946 - 1964)"
    elif 42 <= edad <= 57:
        return "Generación X (1965 - 1981)"
    elif 26 <= edad <= 41:
        return "Millennials (1982 - 1996)"
    elif 10 <= edad <= 25:
        return "Generación Z (1997 - 2013)"
    elif edad <= 9:
        return "Generación Alfa (nacidos después de 2013)"
    else:
        return "Edad fuera de rango"

# Solicitar la edad
try:
    edad = int(input("Ingresa tu edad: "))
    print(f"Pertences a la {obtener_generacion(edad)}.")
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")
