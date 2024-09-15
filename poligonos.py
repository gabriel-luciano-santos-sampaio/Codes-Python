import math

poligono = float(input("Escolha qual polígono você deseja\n1 para quadrado\n2 para retângulo\n3 para triângulo\n4 para círculo\n5 para cilindro\n: "))

match poligono:
    case 1:  # Quadrado
        lado = float(input("Coloque a medida do lado: "))
        perimetro = 4 * lado
        area = lado ** 2
        print("O perímetro é: ", perimetro)
        print("A área é: ", area)
    case 2:  # Retângulo
        base = float(input("Coloque a medida da base: "))
        altura = float(input("Coloque a medida da altura: "))
        perimetro = 2 * (base + altura)
        area = base * altura
        print("O perímetro é: ", perimetro)
        print("A área é: ", area)
    case 3:  # Triângulo
        base = float(input("Coloque a medida da base: "))
        altura = float(input("Coloque a medida da altura: "))
        lado_a = float(input("Coloque a medida do lado A: "))
        lado_b = float(input("Coloque a medida do lado B: "))
        perimetro = base + lado_a + lado_b
        area = (base * altura) / 2
        print("O perímetro é: ", perimetro)
        print("A área é: ", area)
    case 4:  # Círculo
        raio = float(input("Coloque a medida do raio: "))
        perimetro = 2 * math.pi * raio
        area = math.pi * (raio ** 2)
        print("O perímetro é: ", perimetro)
        print("A área é: ", area)
    case 5:  # Cilindro
        raio = float(input("Coloque a medida do raio da base: "))
        altura = float(input("Coloque a medida da altura: "))
        area_base = math.pi * (raio ** 2)
        area_lateral = 2 * math.pi * raio * altura
        area_total = 2 * area_base + area_lateral
        volume = area_base * altura
        print("A área lateral é: ", area_lateral)
        print("A área total é: ", area_total)
        print("O volume é: ", volume)
    case _:  # Opção inválida
        print("Não existe essa opção")
