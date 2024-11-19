import json
import hashlib

# Diccionario para almacenar los usuarios
usuarios_db = {}

# Función para cargar datos desde un archivo JSON, con el nombre de archivo como parámetro
def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            global usuarios_db
            usuarios_db = json.load(archivo)
            print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo, se creará uno nuevo al guardar.")
    except json.JSONDecodeError:
        print("El archivo está vacío o tiene un formato incorrecto.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

# Función para guardar datos en un archivo JSON, con el nombre de archivo como parámetro
def guardar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(usuarios_db, archivo)
            print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")

# Función para hashear una contraseña
def hashear_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para registrar un nuevo usuario
def registrar_usuario(nombre_archivo):
    print("\n--- Registro de Usuario ---")
    nombre = input("Ingrese el nombre de usuario: ")

    # Verificar si el nombre de usuario ya existe
    if nombre in usuarios_db:
        print("Este nombre de usuario ya existe. Prueba con otro nombre.")
        return

    # Pedir el email y verificar si ya está en uso
    email = input("Ingrese el email: ")
    if any(datos["email"] == email for datos in usuarios_db.values()):
        print("Este correo electrónico ya está en uso. Prueba con otro.")
        return

    try:
        edad = int(input("Ingrese la edad: "))
        contraseña = input("Ingrese una contraseña: ")
        
        # Validación básica del email
        if "@" not in email or "." not in email:
            raise ValueError("El email ingresado no es válido.")
        
        # Guardamos el usuario en el diccionario con la contraseña hasheada
        usuarios_db[nombre] = {
            "edad": edad,
            "email": email,
            "contraseña": hashear_contraseña(contraseña)
        }
        print(f"Usuario '{nombre}' registrado con éxito.")
        guardar_datos(nombre_archivo)  # Guardamos los datos con el nombre de archivo como parámetro
    
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente de nuevo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Función para mostrar todos los usuarios registrados (sin mostrar las contraseñas)
def mostrar_usuarios():
    print("\n--- Lista de Usuarios Registrados ---")
    if usuarios_db:
        for usuario, datos in usuarios_db.items():
            print(f"Nombre: {usuario}, Edad: {datos['edad']}, Email: {datos['email']}")
    else:
        print("No hay usuarios registrados.")

# Función para verificar la contraseña
def verificar_contraseña(nombre_usuario, contraseña):
    # Verificar si el usuario existe y si el hash de la contraseña coincide
    if nombre_usuario in usuarios_db:
        hash_contraseña = hashear_contraseña(contraseña)
        if usuarios_db[nombre_usuario]["contraseña"] == hash_contraseña:
            print("Contraseña verificada con éxito. Login exitoso")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    else:
        print("El usuario no existe.")
        return False

# Función principal del menú
def menu():
    # Nombre del archivo como parámetro
    nombre_archivo = "usuarios_db.json"
    cargar_datos(nombre_archivo)  # Cargar los datos usando el nombre de archivo
    
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Login/Verificar contraseña")
        print("4. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
            
            if opcion == 1:
                registrar_usuario(nombre_archivo)
            elif opcion == 2:
                mostrar_usuarios()
            elif opcion == 3:
                nombre = input("Ingrese el nombre de usuario: ")
                contraseña = input("Ingrese la contraseña: ")
                verificar_contraseña(nombre, contraseña)
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        
        except ValueError:
            print("Error: Debes ingresar un número correspondiente a una opción del menú.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutamos el menú
#menu()





