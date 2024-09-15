def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return None

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

def main():
    try:
        peso = float(input('Coloque seu peso (kg): '))
        altura = float(input('Coloque sua altura (m): '))
        
        imc = calcular_imc(peso, altura)
        if imc is None:
            print("Erro: Altura não pode ser zero.")
        else:
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificar_imc(imc)}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
