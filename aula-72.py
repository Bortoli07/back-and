# Lê quatro valores do teclado e os guarda em uma tupla
numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: ")),
)

print("-" * 30)
print(f"Você digitou os valores: {numeros}")

# A) Quantas vezes apareceu o valor 9
print(f"A) O valor 9 apareceu {numeros.count(9)} vez(es).")

# B) Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    # Soma-se 1 porque o índice em Python começa em 0 (posição humana = índice + 1)
    print(f"B) O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição.")
else:
    print("B) O valor 3 não foi digitado em nenhuma posição.")

# C) Quais foram os números pares
pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f"C) Os números pares digitados foram: {pares}")
else:
    print("C) Não foram digitados números pares.")
