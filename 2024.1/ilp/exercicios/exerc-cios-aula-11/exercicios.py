# 1. Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e remova todos os elementos duplicados, mantendo a
# ordem original dos elementos. Ao final, apresente os valores fornecidos
# pelo usuário e o resultado do processamento da sua solução;

# quantidade_numeros = int(input("Digite a quantidade de números a serem fornecidos: "))
# lista_numeros = []

# for x in range(quantidade_numeros):
#     lista_numeros_fornecidos = []
#     numero_fornecido = input("Número inteiro: ")
#     if numero_fornecido not in lista_numeros:
#         lista_numeros_fornecidos = [numero_fornecido]
#         lista_numeros = lista_numeros + lista_numeros_fornecidos

# 2. Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e um número alvo. O programa deve encontrar todos os
# pares de números na lista cuja soma seja igual ao número alvo.
# 1. Exemplo: Digite os números separados por espaço: 2 4 3 5 7
# Digite o valor alvo: 7
# Pares encontrados: (2, 5), (3, 4)

# valores = input("Digite os números separados por UM espaço: ")
# numero_alvo = int(input("Digite um número alvo: "))
# lista_numeros = valores.split()
# lista_pares = []
# for x in lista_numeros:
#     for y in lista_numeros:
#         if int(x)+int(y) == numero_alvo:
#             par = [f"{x} + {y} = {numero_alvo}"]
#             lista_pares = lista_pares + par

# print(f"Pares encontrados: {lista_pares}")

# 3. Escreva um programa que leia uma lista de números inteiros fornecida pelo
# usuário e um número de passos. O programa deve rotacionar a lista para a
# direita pelo número de passos especificado.
# Exemplo: Digite os números separados por espaço: 1 2 3 4 5
# Digite o número de passos: 2
# Lista rotacionada: [4, 5, 1, 2, 3]

# 4. Escreva um programa que leia uma lista de números inteiros fornecida pelo
# usuário e utilize uma list comprehension para gerar uma nova lista contendo
# os quadrados de todos os números ímpares da lista original.
# Exemplo: Digite os números separados por espaço: 1 2 3 4 5 6 7 8 9 10
# Quadrados dos números ímpares: [1, 9, 25, 49, 81]