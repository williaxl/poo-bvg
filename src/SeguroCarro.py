from .SeguroVeiculo import SeguroVeiculo

class SeguroCarro(SeguroVeiculo):
    def __init__(self, cliente, valor, inicio_vigencia, fim_vigencia, veiculo):
        super().__init__(cliente, valor, inicio_vigencia, fim_vigencia)
        self._veiculo = veiculo

    def calcular_valor(self):
        """Adiciona taxa extra de 10% para carro"""
        return self._valor * 1.10