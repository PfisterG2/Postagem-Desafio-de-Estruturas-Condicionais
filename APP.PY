def calcular_reajuste(salario_atual, inflacao):
    if salario_atual <= 280:
        percentual = 20
    elif 280 < salario_atual <= 700:
        percentual = 15
    else:
        percentual = 10  # Opcional: ajuste para salários acima de 700
    
    aumento = salario_atual * (percentual / 100)
    novo_salario = salario_atual + aumento
    aumento_real = aumento - (inflacao * salario_atual)

    print("=== Detalhes do Reajuste ===")
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real (descontando inflação): R$ {aumento_real:.2f}")

# Exemplo de uso
salario = float(input("Digite o salário atual do colaborador: R$ "))
inflacao = float(input("Digite o percentual de inflação (em decimal, ex.: 0.05 para 5%): "))
calcular_reajuste(salario, inflacao)