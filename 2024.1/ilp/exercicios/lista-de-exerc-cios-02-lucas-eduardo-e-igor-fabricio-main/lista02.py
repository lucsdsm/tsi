# 1. Crie um programa que leia o salário de uma pessoa e calcule o imposto de renda a
# ser pago baseado nas seguintes faixas: até R$ 1.903,98 isento, de R$ 1.903,99 até
# R$ 2.826,65 o imposto é de 7,5%, de R$ 2.826,66 até R$ 3.751,05 o imposto é de
# 15%, de R$ 3.751,06 até R$ 4.664,68 o imposto é de 22,5%, acima de R$ 4.664,68
# o imposto é de 27,5%.

# salario = float(input("Salário: "))
# ir_porcentagem = 0
# ir_valor = 0

# if(salario <= 1903.98):
#     ir_situacao = 0
#     ir_porcentagem = 0
#     ir_valor = 0

# elif(2826.65 > salario > 1903.98):
#     ir_situacao = 7.5
#     ir_porcentagem = 0.075
#     ir_valor = salario * ir_porcentagem

# elif(3751.05 > salario > 2826.66):
#     ir_situacao = 15
#     ir_porcentagem = 0.15
#     ir_valor = salario * ir_porcentagem

# elif(4664.68 > salario > 3751.06):
#     ir_situacao = 22.5
#     ir_porcentagem = 0.225
#     ir_valor = salario * ir_porcentagem

# else:
#     ir_situacao = 27.5
#     ir_porcentagem = 0.275
#     ir_valor = salario * ir_porcentagem

# print(f"{ir_situacao}% do seu salário, equivalente a R${ir_valor}, será convertido em imposto de renda.")


# 2. Escreva um programa que solicita o valor de um ano ao usuário, em seguida informa
# se o ano fornecido é ou não bissexto. [Dica: um ano é bissexto se é divisível por 4,
# mas não por 100. Para que um número X seja considerado divisível por um número
# Y é preciso que o resto da divisão de X por Y seja igual a ZERO].

# ano = int(input("Ano: "))

# if (ano % 4 == 0) and (ano % 100 != 0):
#     print(f"{ano} é um ano bissexto.")

# else:
#     print(f"{ano} não é um ano bissexto.")


# 3. Escreva um programa que solicite um número entre 1 e 10. Caso o usuário digite um
# valor dentro dessa faixa o programa deverá exibir a mensagem “O número digitado
# está DENTRO da faixa solicitada.”, senão o programa deverá exibir a mensagem “O
# número digitado está FORA da faixa solicitada.”.

# n = float(input("Um número de 1 a 10: "))
# if (1 > n > 10):
#     print(f"{n} não está na faixa solicitada.")
# else:
#     print(f"{n} está dentro da faixa solicitada.")


# 4. Escreva um programa que dado dois valores informe qual deles é o maior.


# 5. Escreva um programa que leia dois valores inteiros e escreva como saída a diferença
# entre o maior valor e o menor valor.


# 6. Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida o pro-
# grama deverá exibir os 3 valores digitados pelo usuário em ordem crescente.


# 7. Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida o pro-
# grama deverá perguntar ao usuário se deseja ver os valores impressos em ordem
# crescente ou decrescente. Após a escolha, o programa deverá exibir os valores or-
# denados conforme indicação do usuário.


# 8. Escreva um programa que leia três valores e determine se eles podem formar um
# triângulo. Caso possam, classifique o triângulo como equilátero, isósceles ou esca-
# leno.