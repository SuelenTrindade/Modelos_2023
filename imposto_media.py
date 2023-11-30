# Solicita ao usuário que insira o saldo médio bancário
saldo_medio = float(input("Informe o saldo médio bancário da conta corrente em M$: "))

# Inicializa a variável que armazenará o valor do imposto
imposto = 0.0

# Calcula o imposto com base nas faixas de saldo médio
if saldo_medio >= 100000:
    imposto = saldo_medio * 0.068
elif saldo_medio >= 10000:
    imposto = saldo_medio * 0.034
elif saldo_medio >= 1000:
    imposto = saldo_medio * 0.017
elif saldo_medio >= 100:
    imposto = saldo_medio * 0.0085

# Exibe o valor do imposto ISMB devido
print(f"O valor do imposto ISMB devido é de M${imposto:.2f}")