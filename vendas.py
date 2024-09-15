def calcular_total(v1, v2, v3):
    total = (v1 + v2 + v3) / 3
    return total

def calcular_valor_recebido(total):
    if total <= 120:
        vr = total * 10 / 100
        print(f"Você ficou abaixo da média com: {total:.2f}")
    else:
        vr = total * 20 / 100
        print(f"Você ficou acima da média com: {total:.2f}")
    print(f"O valor recebido foi: {vr:.2f}")

def main():
    try:
        v1 = float(input("Insira o valor da primeira venda: "))
        v2 = float(input("Insira o valor da segunda venda: "))
        v3 = float(input("Insira o valor da terceira venda: "))

        total = calcular_total(v1, v2, v3)
        calcular_valor_recebido(total)
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
