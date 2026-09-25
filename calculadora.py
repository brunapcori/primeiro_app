def calcular():
    try:
        primeiro_numero = float(input("Digite o primeiro número real: "))
        segundo_numero = float(input("Digite o segundo número real: "))
    except ValueError:
        print("Erro: digite números reais válidos.")
        return

    print("\nEscolha uma operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    operacao = input("Digite o número da operação: ").strip()

    if operacao == "1":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "2":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "3":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "4":
        if segundo_numero == 0:
            print("Erro: não é possível dividir por zero.")
            return
        resultado = primeiro_numero / segundo_numero
    else:
        print("Erro: operação inválida.")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calcular()
