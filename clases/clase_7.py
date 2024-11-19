def welcome (city) :
    return  print(f"Bienvenido a {city}")

welcome("Argentina")

def media (lista) :
    try :
        media = sum(lista) / len(lista)
        return  print(media)
    except :
        if len(lista) == 0:
         return  0
        
    

lista = []
media(lista)


    