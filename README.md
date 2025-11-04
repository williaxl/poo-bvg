# Projeto 2 - Sistema de Seguro de Carro

## Descrição do Projeto
Este projeto implementa um sistema básico de gestão de seguros de veículos, utilizando os conceitos de Programação Orientada a Objetos (POO) em Python. O sistema inclui classes para representar clientes, carros e seguros, e permite operações como exibir informações, atualizar atributos e calcular valores de seguro.

## Estrutura do Projeto

- `src/` : Contém todas as classes do projeto.
- `test_projeto2.py` : Script para testar o funcionamento das classes.
- `docs/Projeto2.pdf` : Documento PDF com diagramas UML, explicações e modelagem detalhada.
- `README.md` : Este arquivo com informações resumidas do projeto.

## Classes Principais

### Carro
- Atributos: ano, marca, modelo, cor, placa
- Métodos: `exibir_detalhes()`, `atualizar_cor(nova_cor)`

### Cliente
- Atributos: nome, cpf
- Métodos: `exibir_informacoes()`

### Seguro
- Atributos: carro, cliente, valor, vigência
- Métodos: `calcular_valor(base_valor, taxa)`, `verificar_vigencia()`

### SeguroVeiculo (base)
- Subclasses: `SeguroCarro`, `SeguroMoto`
- Benefício da herança: evita duplicação de código e permite especialização dos métodos.

## Uso
1. Execute `test_projeto2.py` para testar o funcionamento das classes.
2. Consulte o PDF em `docs/Projeto2.pdf` para entender a modelagem UML e os relacionamentos entre classes.
