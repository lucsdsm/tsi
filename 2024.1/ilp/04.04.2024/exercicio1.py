#Exercício de fixação 01
#Escreva um algoritmo que leia o valor de um número inteiro digitado pelo usuário e armazene esse valor em uma variável;
#O algoritmo deve verificar se o valor digitado é um número positivo.
#Se o valor digitado for maior do que ZERO o programa deve escrever na tela “O número é positivo!”

#n = int(input("Digite um número: "))
#if (n > 0):
  #print("O número é positivo!")

curso_tsi = input("Você faz TSI no IFRN? (s/n): ")
potiguar = input("Você é potiguar? (s/n): ")

if (curso_tsi == "s" and potiguar == "s"):
  print("Você faz TSI e é portiguar")

elif (curso_tsi == "s" and potiguar == "n"):
  print("Você faz TSI mas não é portiguar")

elif (curso_tsi == "n" and potiguar == "s"):
  print("Você não faz TSI mas é portiguar")

elif (curso_tsi == "n" and potiguar == "n"):
  print("Você nem faz TSI e nem é portiguar")

else:
  print("Você não é nada.")