class Planeta:


    class TipoPlaneta:
        GASEOSO = "GASEOSO"
        TERRESTRE = "TERRESTRE"
        ENANO = "ENANO"


    def __init__(self, nombre=None, cantidadSatélites=0, masa=0.0, volumen=0.0, diámetro=0, distanciaSol=0, tipo=None, esObservable=False):

        self.nombre = nombre
        self.cantidadSatélites = cantidadSatélites
        self.masa = masa
        self.volumen = volumen
        self.diámetro = diámetro
        self.distanciaSol = distanciaSol
        self.tipo = tipo
        self.esObservable = esObservable


    def imprimir(self):

        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidadSatélites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diámetro}")
        print(f"Distancia al sol = {self.distanciaSol}")
        print(f"Tipo de planeta = {self.tipo}")
        print(f"Es observable = {self.esObservable}")
        print()


    def calcular_densidad(self):

        return self.masa / self.volumen
        # Densidad = masa / volumen


    def es_planeta_exterior(self):

        limite = 149597870 * 3.4
        # Un planeta exterior está situado más allá del cinturón de asteroides
        # El cinturón se encuentra entre 2,1 y 3,4 UA (UA = 149.597.870 Km)
        if self.distanciaSol > limite:
            return True
        else:
            return False


if __name__ == "__main__":
    planet1 = Planeta("Tierra", 1, 5.9736e24, 1.0832e12, 12742, 150000000, Planeta.TipoPlaneta.TERRESTRE, True)
    planet1.imprimir()
    print(f"Densidad del planeta = {planet1.calcular_densidad()}")
    print(f"Es planeta exterior = {planet1.es_planeta_exterior()}")
    print()

    planet2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820, 750000000, Planeta.TipoPlaneta.GASEOSO, True)
    planet2.imprimir()
    print(f"Densidad del planeta = {planet2.calcular_densidad()}")
    print(f"Es planeta exterior = {planet2.es_planeta_exterior()}")
