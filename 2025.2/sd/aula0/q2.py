peso = float(input("Qual o seu peso em kilos? "))
altura = float(input("Qual sua altura em metros? "))

imc = peso/(altura**2)

print(f"Seu IMC é: {imc}")