from entregas.pre_entrega2.Clientes import Cliente
from entregas.pre_entrega1.PreEntrega1 import menu

menu()

# Ejemplo de uso:
if __name__ == "__main__":
    cliente = Cliente("Joaquín Benitez", "joaquin@example.com", "Concepción del Uruguay", "+54 123 456 789")
    print(cliente.mostrar_informacion())
    cliente.actualizar_email("joaconuevo@example.com")
    print(cliente)# Ejemplo de uso: str

 