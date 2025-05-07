class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta, interes_mensual):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta 
        self.saldo = 0.0
        self.interes_mensual = interes_mensual  

    def imprimir_datos(self):
        print(f"Nombres del titular = {self.nombres}")
        print(f"Apellidos del titular = {self.apellidos}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta}")
        print(f"Saldo = {self.saldo}")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se ha consignado ${monto:.0f} en la cuenta. El nuevo saldo es ${self.saldo:.0f}")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Se ha retirado ${monto:.0f} en la cuenta. El nuevo saldo es ${self.saldo:.0f}")
        else:
            print("Retiro inválido: monto mayor al saldo.")

    def aplicar_interes(self):
        incremento = self.saldo * (self.interes_mensual / 100)
        self.saldo += incremento
        print(f"Se aplicó interés mensual de {self.interes_mensual:.2f}%. El nuevo saldo es ${self.saldo:.0f}")


def main():
    cuenta = CuentaBancaria("Pedro", "Pérez", "123456789", "AHORROS", interes_mensual=1.5)
    cuenta.imprimir_datos()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    cuenta.aplicar_interes()


if __name__ == "__main__":
    main()
