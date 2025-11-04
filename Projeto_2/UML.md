# Diagrama UML - Projeto 2

## Estrutura das Classes

```mermaid
classDiagram
    class Cliente {
        -nome : str
        -cpf : str
        +exibir_informacoes() str
        +get_cpf() str
    }

    class Carro {
        -ano : int
        -marca : str
        -modelo : str
        -cor : str
        -placa : str
        +exibir_detalhes() str
        +set_cor(cor : str)
    }

    class Seguro {
        -cliente : Cliente
        -carros : list
        -valor : float
        -inicio_vigencia : date
        -fim_vigencia : date
        +calcular_valor(base_valor : float, taxa : float) float
        +verificar_vigencia() bool
    }

    class SeguroVeiculo {
        -cliente : Cliente
        -valor : float
        -inicio_vigencia : date
        -fim_vigencia : date
        +calcular_valor() float
        +verificar_vigencia() bool
        +get_cliente() Cliente
    }

    class SeguroCarro {
        -tipo_seguro : str
        +calcular_valor(base_valor : float, taxa : float) float
    }

    class SeguroMoto {
        +calcular_valor(base_valor : float, taxa : float) float
    }

    Cliente "1" --> "n" Seguro : possui
    Seguro --> "n" Carro : cobre
    SeguroVeiculo <|-- SeguroCarro
    SeguroVeiculo <|-- SeguroMoto
```

## Explicação Geral

- **Cliente**: armazena informações pessoais com CPF encapsulado.
- **Carro**: representa o veículo, permitindo alteração de cor via método público.
- **Seguro**: gerencia cliente e lista de carros segurados.
- **SeguroVeiculo**: classe base para seguros de veículos.
- **SeguroCarro / SeguroMoto**: especializações de SeguroVeiculo com cálculo de valor próprio.
- **Encapsulamento**: protege dados sensíveis (CPF, atributos do carro).
- **Herança**: permite especialização de tipos de seguro.
- **Composição**: Seguro depende de Cliente e Carro.

## Autor

**William Axel**  
Disciplina: Programação Orientada a Objetos  
Projeto 2 — Sistema de Seguros em Python
