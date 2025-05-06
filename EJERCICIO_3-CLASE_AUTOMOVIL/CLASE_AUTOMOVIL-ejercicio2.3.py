class Automóvil:


    class TipoCombustible:
        GASOLINA = "GASOLINA"
        BIOETANOL = "BIOETANOL"
        DIESEL = "DIESEL"
        BIODIESEL = "BIODIESEL"
        GAS_NATURAL = "GAS_NATURAL"

    class TipoAutomóvil:
        CIUDAD = "CIUDAD"
        SUBCOMPACTO = "SUBCOMPACTO"
        COMPACTO = "COMPACTO"
        FAMILIAR = "FAMILIAR"
        EJECUTIVO = "EJECUTIVO"
        SUV = "SUV"

    class TipoColor:
        BLANCO = "BLANCO"
        NEGRO = "NEGRO"
        ROJO = "ROJO"
        NARANJA = "NARANJA"
        AMARILLO = "AMARILLO"
        VERDE = "VERDE"
        AZUL = "AZUL"
        VIOLETA = "VIOLETA"


    def __init__(self, marca, modelo, motor, tipoCombustible, tipoAutomóvil, númeroPuertas, cantidadAsientos, velocidadMáxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomóvil = tipoAutomóvil
        self.númeroPuertas = númeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMáxima = velocidadMáxima
        self.color = color
        self.velocidadActual = 0


    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipoCombustible

    def get_tipo_automóvil(self):
        return self.tipoAutomóvil

    def get_número_puertas(self):
        return self.númeroPuertas

    def get_cantidad_asientos(self):
        return self.cantidadAsientos

    def get_velocidad_máxima(self):
        return self.velocidadMáxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidadActual

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipoCombustible):
        self.tipoCombustible = tipoCombustible

    def set_tipo_automóvil(self, tipoAutomóvil):
        self.tipoAutomóvil = tipoAutomóvil

    def set_número_puertas(self, númeroPuertas):
        self.númeroPuertas = númeroPuertas

    def set_cantidad_asientos(self, cantidadAsientos):
        self.cantidadAsientos = cantidadAsientos

    def set_velocidad_máxima(self, velocidadMáxima):
        self.velocidadMáxima = velocidadMáxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidadActual):
        self.velocidadActual = velocidadActual

    def acelerar(self, incrementoVelocidad):
        if self.velocidadActual + incrementoVelocidad < self.velocidadMáxima:
            self.velocidadActual += incrementoVelocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def desacelerar(self, decrementoVelocidad):
        if (self.velocidadActual - decrementoVelocidad) >= 0:
            self.velocidadActual -= decrementoVelocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidadActual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidadActual > 0:
            return distancia / self.velocidadActual
        else:
            return 0

    def imprimir(self):
        print()
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipoCombustible}")
        print(f"Tipo de automóvil = {self.tipoAutomóvil}")
        print(f"Número de puertas = {self.númeroPuertas}")
        print(f"Cantidad de asientos = {self.cantidadAsientos}")
        print(f"Velocida máxima = {self.velocidadMáxima}")
        print(f"Color = {self.color}")
        print(f"Velocidad actual = {self.velocidadActual}")
        print()

if __name__ == "__main__":
    auto1 = Automóvil("Ford", 2018, 3, Automóvil.TipoCombustible.DIESEL,
        Automóvil.TipoAutomóvil.EJECUTIVO, 5, 6, 250,
        Automóvil.TipoColor.NEGRO)
    auto1.imprimir()
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    auto1.frenar()
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    auto1.desacelerar(20)
    print()