x = int(input ("Escreva o valor de x: "))
y = int(input ("Escreva o valor de Y: "))

def determinar_quadrante(x, y):
    if x > 0 and y > 0:
        return "Primeiro Quadrante"
    elif x < 0 and y > 0:
        return "Segundo Quadrante"
    elif x < 0 and y < 0:
        return "Terceiro Quadrante"
    elif x > 0 and y < 0:
        return "Quarto Quadrante"
    elif x == 0 and y == 0:
        return "Origem"
    elif x == 0:
        return "Sobre o eixo Y"
    elif y == 0:
        return "Sobre o eixo X"

# Exemplo de uso

print(determinar_quadrante(x, y))  # Saída esperada: "Primeiro Quadrante"
