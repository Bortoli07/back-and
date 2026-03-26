km_percorrido=float(input("quantos km foram percorridos?"))
dias_alugados=int(input("por quantos dias o carro foi alugado?"))
preco_total=(dias_alugados * 60) + (km_percorrido * 0.15)
print(f"o total a pagar é R$ {preco_total:.2f}")
