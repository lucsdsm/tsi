# // Comparação dos tempos
# // 10 elementos:
# // Tempo com Stooge: 0.10170 ms
# // Tempo com Bubble Sort: 0.12200 ms
# // Tempo com Selection Sort: 0.08080 ms
# // Tempo com Insertion Sort: 0.05480 ms

# // 100 elementos:
# // Tempo com Stooge: 3.47950 ms
# // Tempo com Bubble Sort: 0.87380 ms
# // Tempo com Selection Sort: 0.26920 ms
# // Tempo com Insertion Sort: 0.16460 ms

# // 1000 elementos:
# // Tempo com Stooge: 421.88780 ms
# // Tempo com Bubble Sort: 5.10490 ms
# // Tempo com Selection Sort: 3.20390 ms
# // Tempo com Insertion Sort: 1.77190 ms

# // 10000 elementos:
# // Tempo com Stooge: 307548.34240 ms
# // Tempo com Bubble Sort: 577.90780 ms
# // Tempo com Selection Sort: 58.27540 ms
# // Tempo com Insertion Sort: 26.13680 ms

import matplotlib.pyplot as plt
import numpy as np

# 1. Estruturar os dados coletados
# Eixo X: Número de elementos
n_elementos = [10, 100, 1000, 10000]

# Eixo Y: Tempos de execução em milissegundos (ms)
tempos = {
    'Stooge Sort': [0.10170, 3.47950, 421.88780, 307548.34240],
    'Bubble Sort': [0.12200, 0.87380, 5.10490, 577.90780],
    'Selection Sort': [0.08080, 0.26920, 3.20390, 58.27540],
    'Insertion Sort': [0.05480, 0.16460, 1.77190, 26.13680]
}

# Cores para os algoritmos para um visual mais agradável
cores = {
    'Stooge Sort': 'red',
    'Bubble Sort': 'orange',
    'Selection Sort': 'blue',
    'Insertion Sort': 'green'
}


# 2. Configurar e criar o gráfico
# plt.subplots() é uma boa prática para ter mais controle sobre a figura
fig, ax = plt.subplots(figsize=(10, 10))

# 3. Plotar os dados de cada algoritmo
for algoritmo, tempos_execucao in tempos.items():
    ax.plot(
        n_elementos, 
        tempos_execucao, 
        label=algoritmo,
        marker='o', # Adiciona um ponto em cada medição
        linestyle='-', # Linha conectando os pontos
        color=cores[algoritmo]
    )

# 4. Configurar as escalas para logarítmica
# Essencial para visualizar dados com grandes variações
ax.set_xscale('log')
ax.set_yscale('log')

# 5. Adicionar títulos, legendas e grade para melhor visualização
ax.set_title('Comparação de Desempenho de Algoritmos de Ordenação', fontsize=16)
ax.set_xlabel('Número de Elementos (N) - Escala Logarítmica', fontsize=12)
ax.set_ylabel('Tempo de Execução (ms) - Escala Logarítmica', fontsize=12)
ax.legend(title='Algoritmos')
ax.grid(True, which="both", linestyle='--', linewidth=0.5)

# 6. Mostrar o gráfico
plt.show()