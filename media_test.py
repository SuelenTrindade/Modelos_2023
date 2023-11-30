preco_por_kwh = float(input("Digite o preço por kWh consumido: "))
quantidade_kwh = float(input("Digite a quantidade de kWh consumidos no mês: "))
tipo_consumidor = input("Digite o tipo de consumidor com a letra maiúscula (I para Industrial, C para Comercial, R para Residencial): ")

valor_conta = preco_por_kwh * quantidade_kwh
if tipo_consumidor == 'I':
    valor_conta *= 1.15  # Acréscimo de 15% para consumidor industrial
elif tipo_consumidor == 'C':
    valor_conta *= 1.05  # Acréscimo de 5% para consumidor comercial
elif tipo_consumidor == 'R':
    pass
else:
    print("Tipo de consumidor inválido.")
print(f"Valor da conta mensal: R${valor_conta:.2f}")