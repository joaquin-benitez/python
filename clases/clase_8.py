# Clase base Mamifero
class Mamifero:
    def __init__(self, cantMamas, esperanzaDeVida):
        self.cantMamas = cantMamas
        self.esperanzaDeVida = esperanzaDeVida

    def amamantar(self):
        return f"Este mamífero amamanta a sus crías con {self.cantMamas} mamas."

    def nacer(self):
        return "El mamífero ha nacido."

# Clase base AnimalMarino
class AnimalMarino:
    def __init__(self, tieneBranqueas, especie):
        self.tieneBranqueas = tieneBranqueas
        self.especie = especie

    def nadar(self):
        return f"El {self.especie} nada y {'tiene' if self.tieneBranqueas else 'no tiene'} branquias."

# Clase derivada Cetaceo que hereda de Mamifero y AnimalMarino
class Cetaceo(Mamifero, AnimalMarino):
    def __init__(self, cantMamas, esperanzaDeVida, tieneBranqueas, especie, notas, viveEn, peso):
        #herencia
        Mamifero.__init__(self, cantMamas, esperanzaDeVida)
        AnimalMarino.__init__(self, tieneBranqueas, especie)
        #atributos especif
        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso

    def nacer(self):
        return "El cetáceo ha nacido en el agua."

    def nadar(self):
        return f"Este cetáceo nada en {self.viveEn} y pesa aproximadamente {self.peso} kg."

# Ejemplo de uso
ballena = Cetaceo(2, 80, False, "ballena", "Grandes notas", "océano", 30000)

print(ballena.amamantar())
print(ballena.nacer())
print(ballena.nadar())
print(ballena.esperanzaDeVida)

