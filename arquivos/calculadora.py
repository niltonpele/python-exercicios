# Programa de calculadora simples

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    print("Resultado:", a + b)
elif opcao == 2:
    print("Resultado:", a - b)
elif opcao == 3:
    print("Resultado:", a * b)
elif opcao == 4:
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Opção inválida.")

