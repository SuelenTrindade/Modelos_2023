#Faça um programa em Python que leia um vetor A com 
#10 números inteiros, calcule e mostre a soma dos 
#quadrados dos elementos da lista.

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_quadrados = sum([i**2 for i in A])
print(f"A soma dos quadrados dos elementos da lista é {soma_quadrados}.")
