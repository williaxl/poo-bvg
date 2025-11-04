from datetime import date
class SeguroVeiculo:
    def __init__(self, cliente, valor, inicio_vigencia, fim_vigencia):
        self._cliente = cliente
        self._valor = valor
        self._inicio_vigencia = inicio_vigencia
        self._fim_vigencia = fim_vigencia
    def calcular_valor(self):
        """Cálculo base do seguro de veículo"""
        return self._valor
    def verificar_vigencia(self):
        """Verifica se o seguro ainda está dentro do período de vigência"""
        hoje = date.today()
        return self._inicio_vigencia <= hoje <= self._fim_vigencia
    def get_cliente(self):
        return self._cliente