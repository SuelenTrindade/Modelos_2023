# Solicitar ao usuário o número para a tabuada
numero = int(input("Montar a tabuada de: "))

# Solicitar ao usuário o valor inicial e verificar se é menor que o valor final
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

while fim < inicio:
    print("O valor final deve ser maior ou igual ao valor inicial.")
    fim = int(input("Terminar em: "))

# Construir e imprimir a tabuada
print(f"\nTabuada de {numero} de {inicio} a {fim}:\n")

for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")