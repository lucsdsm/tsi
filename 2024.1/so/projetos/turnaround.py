algoritmo = input("Algoritmo desejado (Fifo/SJF): ")

if (algoritmo == "Fifo" or algoritmo == "SJF"):
    quantidade_processos = int(input("Quantidade de processos para serem simulados: "))
    lista_tempos = []
    lista_tempos_turnaround = []

    # Digitar os tempos dos processos de acordo com a quantidade de processos.
    for x in range(quantidade_processos):
        tempo_processo = int(input(f"Tempo do processo {x+1}: ")) # Inicia uma variável para armazenar o tempo.
        novo_tempo = [tempo_processo] # Transforma a variável em uma lista.
        lista_tempos = lista_tempos + novo_tempo # Concatena a variável "novo_tempo" com a lista de tempos.

    if algoritmo == "Fifo":
        # Adiciona à lista de tempos de turnaround levando em consideração apenas os tempos de cada processo com o tempo do processo anterior.
        tempo_turnaround = 0
        for x in range(len(lista_tempos)):
            tempo_turnaround = tempo_turnaround + lista_tempos[x] # Adiciona o valor de turnaround ao valor de X na lista de tempos.
            novo_tempo_turnaround = [tempo_turnaround] # Transforma o novo tempo de turnaround em uma lista.
            lista_tempos_turnaround = lista_tempos_turnaround + novo_tempo_turnaround # Concatena a variável "novo_tempo_turnaround" com a lista de tempos de turnaround.

        print(f"Seguindo o algoritmo {algoritmo}, os tempos de turnaround de cada processo são: \n{lista_tempos_turnaround}")
    
    elif algoritmo == "SJF":

        # lista_tempos_ordenados = []
        # for x in lista_tempos:
        #     for y, valor in enumerate(lista_tempos_ordenados):
        #         if x < valor:
        #             lista_tempos_ordenados.insert(y, x)
        #             break
        #     else:
        #         menor_valor = [x]
        #         lista_tempos_ordenados = lista_tempos_ordenados + menor_valor

        lista_tempos_turnaround = []
        for x in lista_tempos:
            turnaround = x
            for y in lista_tempos:
                    if x <= y:
                        pass
                    elif x > y:
                        pass
else:
    print(f"'{algoritmo}' não é um algoritmo válido (Fifo/SJF). Digite um algoritmo válido.")
        
