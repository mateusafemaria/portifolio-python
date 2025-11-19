#SOMA DE NÚMEROS ÍMPARES

import time

def leia_int(msg):

    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("❌ Valor inválido! Digite um número inteiro.")

def somar_impares(a, b):

    if a > b:
        a, b = b, a  # Corrige automaticamente

    impares = [num for num in range(a, b + 1) if num % 2 != 0]
    return sum(impares), impares, a, b

def menu():
    print("\n===== SOMA DE NÚMEROS ÍMPARES =====")
    print("1 - Calcular soma de ímpares")
    print("2 - Sair")
    print("===================================\n")

while True:
    menu()
    opc = leia_int("Escolha uma opção: ")

    if opc == 1:
        print("\n--- NOVO CÁLCULO ---")
        a = leia_int("Digite o valor A: ")
        b = leia_int("Digite o valor B: ")

        total, lista, menor, maior = somar_impares(a, b)

        print(f"\nIntervalo considerado: {menor} até {maior}")
        print("Números ímpares encontrados:", lista)
        print(f"Soma total dos ímpares: {total}")
        print("-------------------------------\n")

        time.sleep(1)

    elif opc == 2:
        print("Encerrando... 👋")
        break

    else:
        print("❌ Opção inválida! Escolha novamente.\n")
