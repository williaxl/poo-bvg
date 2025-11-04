from .SeguroVeiculo import SeguroVeiculo

class SeguroMoto(SeguroVeiculo):
    def __init__(self, cliente, valor, inicio_vigencia, fim_vigencia, cilindradas):
        super().__init__(cliente, valor, inicio_vigencia, fim_vigencia)
        self._cilindradas = cilindradas
    def calcular_valor(self):
        """Valor depende da cilindrada"""
        if self._cilindradas > 250:
            return self._valor * 1.20
        return self._valor * 1.10