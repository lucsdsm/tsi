votoscandidato1 = 0
votoscandidato2 = 0
votoscandidato3 = 0
votosembranco = 0
votosnulos = 0

voto = 0

while voto != -1:
    voto = int(input("Digite seu voto (1, 2, 3, 0 para branco, -1 para sair e qualquer outro  valor para nulo): "))

    match voto:
        case 1:
            votoscandidato1 += 1
        case 2:
            votoscandidato2 += 1
        case 3:
            votoscandidato3 += 1
        case 0:
            votosembranco += 1
        case -1:
            print("Votação encerrada.")
        case _:
            votosnulos += 1

print(f'Número do candidato vencedor foi: {max(votoscandidato1, votoscandidato2, votoscandidato3)}')
print(f'Número de votos em branco: {votosembranco}')
print(f'Número de votos nulos: {votosnulos}')
print(f'Número de eleitores que votaram: {votoscandidato1 + votoscandidato2 + votoscandidato3 + votosembranco + votosnulos}')