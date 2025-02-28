'''
Crea la clase "Cuenta".
Cada cuenta tendrá un número (diferente a las demás) y un saldo (float).
El número de cuenta se puede consultar y modificar (getter y setter)
Pero el saldo tenemos que hacer un ingreso o una retirada.

Para modificar el saldo tenemos que hacer un ingreso o una retirada'''

class Cuenta:

    def __init__(self):
        self.num_cuenta = " "
        self.saldo = float()

    def set_nºdecuenta(self,numero):
        self.num_cuenta = numero

    def get_num_cuenta(self)
        return self.num_cuenta