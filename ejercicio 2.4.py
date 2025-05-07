import math

class Circulo:
    def __init__(self, radio_cm):
        self.radio = radio_cm

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def imprimir(self):
        print(f"El área del círculo es = {self.area()}")
        print(f"El perímetro del círculo es = {self.perimetro()}\n")


class Rectangulo:
    def __init__(self, base_cm, altura_cm):
        self.base = base_cm
        self.altura = altura_cm

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def imprimir(self):
        print(f"El área del rectángulo es = {self.area()}")
        print(f"El perímetro del rectángulo es = {self.perimetro()}\n")


class Cuadrado:
    def __init__(self, lado_cm):
        self.lado = lado_cm

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def imprimir(self):
        print(f"El área del cuadrado es = {self.area()}")
        print(f"El perímetro del cuadrado es = {self.perimetro()}\n")


class TrianguloRectangulo:
    def __init__(self, base_cm, altura_cm):
        self.base = base_cm
        self.altura = altura_cm

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.altura + math.hypot(self.base, self.altura)

    def tipo(self):
        a, b, c = self.base, self.altura, math.hypot(self.base, self.altura)
        eps = 1e-6
        lados = sorted([a, b, c])
        if abs(lados[0] - lados[2]) < eps:
            return "Equilátero"
        elif abs(lados[0] - lados[1]) < eps or abs(lados[1] - lados[2]) < eps:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir(self):
        print(f"El área del triángulo es = {self.area()}")
        print(f"El perímetro del triángulo es = {self.perimetro()}")
        print(f"Es un triángulo {self.tipo()}\n")


class Rombo:
    def __init__(self, diagonal_mayor_cm, diagonal_menor_cm, lado_cm):
        self.D = diagonal_mayor_cm
        self.d = diagonal_menor_cm
        self.lado = lado_cm

    def area(self):
        return (self.D * self.d) / 2

    def perimetro(self):
        return 4 * self.lado

    def imprimir(self):
        print(f"El área del rombo es = {self.area()}")
        print(f"El perímetro del rombo es = {self.perimetro()}\n")


class Trapecio:
    def __init__(self, base_mayor_cm, base_menor_cm, lado_izq_cm, lado_der_cm, altura_cm):
        self.B = base_mayor_cm
        self.b = base_menor_cm
        self.l1 = lado_izq_cm
        self.l2 = lado_der_cm
        self.h = altura_cm

    def area(self):
        return ((self.B + self.b) * self.h) / 2

    def perimetro(self):
        return self.B + self.b + self.l1 + self.l2

    def imprimir(self):
        print(f"El área del trapecio es = {self.area()}")
        print(f"El perímetro del trapecio es = {self.perimetro()}\n")


def main():
    c = Circulo(2)
    r = Rectangulo(1, 2)
    q = Cuadrado(3)
    t = TrianguloRectangulo(3, 5)
    rom = Rombo(6, 4, 5)
    trap = Trapecio(8, 5, 4, 3, 4)

    c.imprimir()
    r.imprimir()
    q.imprimir()
    t.imprimir()
    rom.imprimir()
    trap.imprimir()


if __name__ == "__main__":
    main()
