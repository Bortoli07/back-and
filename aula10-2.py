preco = float(input('Qual é o preço do produto?R$'))

novo_preco = preco - (preco * 5 / 100)

print(f'o produto que custa R${preco:.2f}, com 5% de desconto, vai custar R${novo_preco:.2f}')
