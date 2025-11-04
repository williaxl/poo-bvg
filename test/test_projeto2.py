import sys
import os
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Cliente import Cliente
from src.Carro import Carro
from src.Seguro import Seguro
from src.SeguroVeiculo import SeguroVeiculo
from src.SeguroCarro import SeguroCarro
from src.SeguroMoto import SeguroMoto

print("===== TESTE CLASSES BÁSICAS =====")
cliente = Cliente("João Silva", "123.456.789-00")
carro = Carro(2020, "Toyota", "Corolla", "Branco", "XYZ-1234")
seguro = Seguro(
    cliente=cliente,
    carros=[carro],
    valor=1500,
    inicio_vigencia=date(2024, 1, 1),
    fim_vigencia=date(2025, 1, 1)
)
print(cliente.exibir_informacoes())
print(carro.exibir_detalhes())
print("Valor calculado:", seguro.calcular_valor(1000, 0.2))
print("Seguro válido?", "Sim" if seguro.verificar_vigencia() else "Não")

print("\n===== TESTE CLASSES COM HERANÇA =====")
seguro_base = SeguroVeiculo(cliente, 1200, date(2024, 1, 1), date(2025, 1, 1))
print(f"Seguro base válido? {'Sim' if seguro_base.verificar_vigencia() else 'Não'}")
seguro_carro = SeguroCarro(cliente, 1500, date(2024, 1, 1), date(2025, 1, 1), carro)
print("Valor Seguro Carro:", seguro_carro.calcular_valor())
seguro_moto = SeguroMoto(cliente, 1000, date(2024, 1, 1), date(2025, 1, 1), cilindradas=300)
print("Valor Seguro Moto:", seguro_moto.calcular_valor())
print("\n===== TESTE DE ENCAPSULAMENTO =====")
print("CPF do cliente (via método público):", cliente.get_cpf())
carro.atualizar_cor("Preto")
print("Cor atualizada do carro:", carro.exibir_detalhes())