class Persona:

    def __init__(self, nombre, apellidos, númeroDocumentoIdentidad, añoNacimiento):

        self.nombre = nombre
        self.apellidos = apellidos
        self.númeroDocumentoIdentidad = númeroDocumentoIdentidad
        self.añoNacimiento = añoNacimiento


    def imprimir(self):

        print()
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.númeroDocumentoIdentidad}")
        print(f"Año de nacimiento = {self.añoNacimiento}")
        print()


if __name__ == "__main__":
    per1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    per2 = Persona("Luis", "León", "1053223344", 2001)
    per1.imprimir()
    per2.imprimir()