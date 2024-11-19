
class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def actualizar_email(self, nuevo_email):
        #"""Actualiza el correo electrónico del cliente."""
        self.email = nuevo_email
        print(f"El email del cliente {self.nombre} ha sido actualizado a {self.email}.")

    def mostrar_informacion(self):
        #"""Muestra la información completa del cliente."""
        return f"Cliente: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"


    