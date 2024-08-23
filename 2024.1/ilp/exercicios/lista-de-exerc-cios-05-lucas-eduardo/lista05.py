# 1. Criação e acesso: Escreva um programa que crie uma tupla que seja criada contendo
# os dados nome, idade e estado. Como saída, o programa deve imprimir cada um
# desses valores separadamente. Exemplos:
# Entrada 1:
# Ana
# 20
# RN

# Saída 1:
# Nome: Ana
# Idade: 20
# Estado: RN

# Entrada 2:
# José
# 15
# CE

# Saída 2:
# Nome: José
# Idade: 15
# Estado: CE

# 2. Desempacotamento: Escreva um programa que realiza o cálculo da distância entre
# dois pontos no plano cartesiano. O programa deve receber como entrada 4 valores
# inteiros para os dois pontos. Em seguida, calcular a distância entre os dois pontos e
# exibir o valor da distância ao usuário. Exemplos:
# Entrada 1:
# Ponto 1: 1 3
# Ponto 2: 1 8

# Saída 1:
# Distância: 5

# Entrada 2:
# Ponto 1: 0 0
# Ponto 2: 5 5

# Saída 2:
# Distância: 7.07

# 3. Concatenação de tuplas: Escreva um programa que cria duas tuplas: uma para frutas
# e outra para vegetais. O programa deve imprimir no terminal o resultado de uma única
# tupla formada pela concatenação das duas tuplas anteriormente fornecidas pelo
# usuário. Exemplos:
# Entrada 1:
# Frutas: Uva, banana e maçã
# Vegetais:
# Cenoura e batata

# Saída 1:
# Alimentos:
# (‘uva’, ‘banana’, ‘maçã, ‘cenoura’, ‘batata’)

# 4. Conversão de Lista para Tupla: Escreva um programa que dada uma lista de números,
# converta essa lista em uma tupla e, em seguida, utilize slices para criar uma nova tupla

# que contenha apenas os três primeiros elementos da tupla original. Imprima o
# resultado da lista original e as duas tuplas criadas. Exemplo:
# Entrada:
# lista: [1,2,3,4,5]

# Saída:
# Tupla: (1,2,3,4,5)
# Slice da tupla: (1,2,3)

# 5. Troca de posições em tuplas: Escreva um programa que, dada uma tupla e dois valores
# inteiros correspondentes às posições nessa tupla, troque os elementos conforme as
# posições fornecidas. Lembre-se de que tuplas são imutáveis, portanto, você precisará
# converter a tupla para uma lista, fazer a troca e depois converter de volta para uma
# tupla. Imprima o resultado da tupla inicial e com as posições permutadas. Exemplos:
# Entrada 1:
# Tupla: (1,2,3,4,5)
# Posição 1: 2
# Posição 2: 4

# Saída 1:
# Tupla A: (1,2,3,4,5)
# Tupla B: (1,2,5,4,3)

# Entrada 2:
# Tupla: (7,2,4,8,3)
# Posição 1: 0
# Posição 2: 3

# Saída 2:
# Tupla A: (7,2,4,8,3)
# Tupla B: (8,2,4,7,3)

# Conjuntos:
# 6. Criação de conjuntos a partir de listas: Escreva um programa que, dada uma lista
# números fornecida pelo usuário, converta a lista em um conjunto para eliminar
# duplicatas. Em seguida, adicione um número extra que seja o dobro do maior valor do
# conjunto e adicione ao conjunto resultante. Imprima a lista inicial e o conjunto final.
# Exemplos:
# Entrada 1:
# Lista: [1, 1, 2, 3,
# 3, 4, 4]

# Saída 1:
# Lista: [1, 1, 2, 3, 3,
# 4, 4]
# Conj: {1, 2, 3, 4, 8}

# Entrada 2:
# Lista: [7, 1, 1, 4, 3,
# 4, 4]

# Saída 2:
# Lista: [7, 1, 1, 4, 3,
# 4, 4]
# Conj: {1, 3, 4, 7, 14}

# 7. União e diferença: Escreva um programa que solicite ao usuário 3 conjuntos (A, B e
# C) de números inteiros e em seguida realize as seguintes operações sobre conjuntos:
# união: (A È B); e diferença: (A È B) - C. O programa deverá exibir como saída o
# resultado da união e diferença entre os conjuntos (use as funções embutidas union()
# e difference()). Exemplo:
# Entrada 1:
# A: 1,2,3,4
# B: 2,5,7,9
# C: 1,4,7,6

# Saída 1:
# União: {1,2,3,4,5,7,9}
# Diferença: {2,5,3,9}

# Entrada 2:
# A: 8,2,5,6
# B: 2,5,7,4
# C: 2,4,7,6

# Saída 2:
# União: {1,2,3,4,5,7,9}
# Diferença: {2,5,3,9}

# 8. Remoção Condicional em Conjuntos: Escreva um programa que receba como entrada
# uma sequência de valores inteiros e cria um conjunto a partir desses valores. Além
# disso, o programa também recebe um valor numérico base para atuar como um divisor.
# Crie um novo conjunto, a partir dos valores inicialmente fornecidos, formado pelos
# números divisíveis pelo divisor digitado pelo usuário. Exiba na tela os dois conjuntos e
# o divisor. Exemplos:

# Entrada 1:
# Valores:
# 1, 9, 3, 2, 3, 6, 4
# Divisor: 3

# Saída 1:
# Conj 1: {1,9,3,2,6,4}
# Conj 2: {9,3,6}

# Entrada 2:
# Valores:
# 16, 8, 2, 3, 6, 40
# Divisor: 4

# Saída 2:
# Conj 1: {16,8,2,3,6,40}
# Conj 2: {16,8,40}

# 9. Operações em Conjuntos: Escreva um programa que, dados dois conjuntos A e B de
# valores fornecidos pelo usuário, verifique se B é um subconjunto de A. Em seguida crie
# um conjunto C com valores do conjunto A, mas sem os valores do conjunto B. Ao final,
# exiba os valores de ambos os conjuntos. Exemplos:
# Entrada 1:
# A: {1, ‘a’, 8, ‘4’}
# B: {8, ‘4’}

# Saída 1:
# B é subconjunto de A
# A: {1, ‘a’, 8, ‘4’}
# B: {8, ‘4’}
# C: {1, ‘a’}

# Entrada 2:
# A: {1, ‘a’, 8, ‘4’}
# B: {8, 4}

# Saída 2:
# B não é subconjunto de A
# A: {1, ‘a’, 8, ‘4’}
# B: {8, 4}
# C: {1, ‘a’, ‘4’}

# 10. Presença de valores em Conjuntos: Escreva um programa que solicite ao usuário uma
# relação de valores e adicione-os a um conjunto (utilize o operador | para isso). Em
# seguida, crie uma lista com outros valores e verifique quais desses valores estão
# presentes no conjunto. A quantidade de valores a serem fornecidos para o conjunto e
# para a lista é indeterminada e deve ser interrompida quando o usuário digitar o valor
# ‘$$’ para indicar o término de cada uma das coleções. Ao final o programa deverá exibir
# o conjunto e a relação de valores da lista informando se os mesmos estão presentes
# no conjunto. Exemplo:
# Entrada 1:
# Conjunto: {1,2,3,5,6,7,8,9}
# Lista: [1,4,7]

# Saída 1:
# Conjunto: {1,2,3,5,6,7,8,9}
# Lista: 1:Sim, 4:Não, 7:Sim

# Dicionários:
# 11. Escreva um programa que receba como entrada uma string várias palavras separadas
# por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
# cada palavra no texto repassado como entrada para o programa, sem fazer distinção
# entre letras maiúsculas ou minúsculas. Os sinais de pontuação não devem ser
# contabilizados, como por exemplo “.” Ou “,”. Crie um dicionário que armazene a
# contagem de cada palavra no texto. A chave do dicionário deve ser a palavra e o valor
# deve ser o número de vezes que a palavra aparece no texto. Imprima o dicionário
# resultante. Exemplos:
# Entrada 1:
# Lorem ipsum
# dolor sit amet.
# Lorem opsum
# dolor amet, dolor
# comem.

# Saída 1:
# Contagem de
# palavras:
# {‘Lorem’:2, ‘ipsum’:1,
# ‘dolor’:3, ‘sit’:1,
# ‘amet’:2, ‘opsum’:1,
# ‘comem’:1}

# Entrada 2:
# Lorem ipsum
# ipsum lorem sit
# amet. Lorem
# corpus dolor
# amet, dolor
# comem CorpuS.

# Saída 2:
# Contagem de
# palavras:
# {‘lorem’:3, ‘ipsum’:2,
# ‘dolor’:2, ‘sit’:1,
# ‘amet’:1, ‘corpus’:2,
# ‘dolor’:2, ‘comem’:1}

# 12. Escreva um programa que receba como entrada uma relação de tuplas formadas por
# nomes de frutas e valores. O programa deverá realizar o agrupamento da relação de
# tuplas pelo nome das tuplas e somar dos valores para criação de um dicionário onde
# o nome da fruta deve ser a chave e o resultado da soma o valor. Ao final, exiba a lista
# de valores inicialmente fornecida e o dicionário criado. Exemplos:
# Entrada 1:
# itens: [(‘banana’,
# 3), (‘uva’, 5),
# (‘uva’, 2),
# (‘banana’, 2),
# (‘pêra’, 2)]

# Saída 1:
# Lista: [(‘banana’, 3),
# (‘uva’, 5), (‘uva’, 2),
# (‘banana’, 2),
# (‘pêra’, 2)]
# Valores:
# {‘banana’:5, ‘uva’:7,
# ‘pêra’:2}

# Entrada 1:
# itens: [(‘banana’,
# 3), (‘uva’, 5), (‘uva’,
# 2), (‘banana’, 2),
# (‘pêra’, 2)]

# Saída 1:
# Lista: [(‘banana’, 3), (‘uva’,
# 5), (‘uva’, 2), (‘banana’, 2),
# (‘pêra’, 2)]
# Valores:
# {‘banana’:5, ‘uva’:7,
# ‘pêra’:2}

# 13. Escreva um programa que dado um dicionário aluno_nota, onde as chaves
# representam nomes de alunos e os valores representam suas respectivas notas, cujos
# valores sejam fornecidos pelo usuário. Crie um novo dicionário que inverta as chaves
# e os valores do dicionário aluno_nota, ou seja, as notas serão as chaves e os nomes
# dos alunos serão os valores. Considere que duas ou mais pessoas podem ter a mesma
# nota, e neste caso, o valor deve ser uma lista com os nomes dos alunos. Imprima o
# dicionário resultante. Exemplo:
# Entrada 1:
# aluno_nota:
# {‘Ana’:70, ‘José’:80,
# ‘João’:20, ‘Rita’:20}

# Saída 1:
# nota_aluno:
# {70:‘Ana’, 80:‘José’,
# 20: [‘João’, ‘Rita’]}

# Entrada 2:
# aluno_nota:
# {‘Ana’:80, ‘José’:80,
# ‘João’:20, ‘Rita’:20}

# Saída 2:
# nota_aluno:
# {80:[ ‘Ana’, ‘José’],
# 20: [‘João’, ‘Rita’]}

# 14. Escreva um programa que dado dois dicionários que representam valores de estoque
# de itens em duas lojas, cujos valores sejam fornecidos pelo usuário. Crie um novo
# dicionário para representar o estoque total que combine esses dois primeiros
# dicionários, somando as quantidades dos itens que aparecem em ambas as lojas. Para
# itens que aparecem apenas em uma loja, mantenha a quantidade original. Imprima o
# dicionário de cada loja e o dicionário resultante.
# Entrada 1:
# Loja 1: {‘Item 1’:10, ‘Item 2’:5, ‘Item 3’:10}
# Loja 2: {‘Item 1’:10, ‘Item 2’:2, ‘Item 4’:10}

# Saída 1:
# Loja 1: {‘Item 1’:10, ‘Item 2’:5, ‘Item 3’:10}
# Loja 2: {‘Item 1’:10, ‘Item 2’:5, ‘Item 4’:10}
# Estoque: {‘Item 1’:20, ‘Item 2’:7, ‘Item 3’:10,
# ‘Item 4’:10}

# 15. Escreva um programa que realiza o cálculo das vendas de uma lista de vendedores
# ao longo de um trimestre. O programa deve solicitar a relação de nomes dos
# vendedores e em seguida criar um dicionário em que o nome do vendedor é a chave
# e o valor deve ser o total das vendas desse vendedor. Faça com que o programa
# solicite para cada vendedor o quantitativo de vendas ao longo de cada mês no
# trimestre. Em seguida, calcule a soma das vendas de cada vendedor e crie uma lista
# de tuplas contendo o nome o valor total das vendas de cada vendedor ordenada pelo
# valor das vendas em ordem decrescente. Exiba ao final o dicionário do relatório de
# vendas e a lista ordenada de tuplas.