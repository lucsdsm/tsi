idade = int(input("Digite sua idade: "))

if (idade < 18):
    print('Menor')

elif idade >= 18 and idade < 65:
    print('Maior')

else:
    print('Idoso')