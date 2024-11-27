import random

capacidade = 40  # Capacidade máxima do ônibus
paradas = 20  # Número total de paradas
lotacao = 0  # Lotação inicial

for parada in range(1, paradas + 1):  # Paradas de 1 a 20
    print(f"\nParada {parada}:")

    # Passageiros descendo
    descer = random.randint(1, 10)
    if lotacao >= descer:  # Apenas remove passageiros se houver suficientes
        lotacao -= descer
        print(f"  {descer} passageiros desceram. Lotação atual: {lotacao}.")
    else:
        print(f"  Apenas {lotacao} passageiros desceram. Lotação atual: 0.")
        lotacao = 0  # Lotação zerada se não houver suficientes

    # Passageiros subindo
    subir = random.randint(1, 10)
    if (capacidade - lotacao) >= subir:  # Verifica se há espaço para subir
        lotacao += subir
        print(f"  {subir} passageiros subiram. Lotação atual: {lotacao}.")
    else:
        print(f"  Não há espaço suficiente para {subir} passageiros. Apenas {capacidade - lotacao} subiram.")
        lotacao = capacidade  # Lotação máxima atingida
