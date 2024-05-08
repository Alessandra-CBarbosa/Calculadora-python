def calculadora():
    while True:
        print("\nCalculadora Simples")
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue
        else:
            print("Operador inválido. Tente novamente.")
            continue

        print("Resultado: ", resultado)

        continuar = input("\nDeseja continuar? (s/n): ")
        if continuar.lower() != "s":
            break

calculadora()