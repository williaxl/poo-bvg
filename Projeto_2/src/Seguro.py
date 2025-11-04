from datetime import datetime

class Seguro:
    def __init__(self, cliente, carros, valor, inicio_vigencia, fim_vigencia):
        self.cliente = cliente
        self.carros = carros
        self.valor = valor
        self.inicio_vigencia = inicio_vigencia
        self.fim_vigencia = fim_vigencia

    def calcular_valor(self, base_valor, taxa):
        self.valor = base_valor + (base_valor * taxa)
        return self.valor

    def verificar_vigencia(self):
        hoje = datetime.now().date()
        return self.inicio_vigencia <= hoje <= self.fim_vigencia