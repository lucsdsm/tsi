import { stoogeSort } from "./Algoritmos";
import { bubbleSort } from "./Algoritmos";
import { selectionSort } from "./Algoritmos";
import { insertionSort } from "./Algoritmos";

const N = 10000;

const vetorDesordenado = Array.from({ length: N }, (_, i) => i + 1).sort(() => Math.random() - 0.5);
console.log("Vetor desordenado:", vetorDesordenado);


// Exemplos de uso:

// Stooge Sort:
const vetorParaStooge = [...vetorDesordenado];
const inicioStooge = performance.now();
stoogeSort(vetorParaStooge, 0, vetorParaStooge.length - 1);
const fimStooge = performance.now();
const tempoTotalStooge = fimStooge - inicioStooge;

// console.log("Vetor ordenado com Stooge:", vetorParaStooge);
console.log("Tempo com Stooge:", tempoTotalStooge.toFixed(5), "ms");

// Bubble Sort:
const vetorParaBubble = [...vetorDesordenado];
const inicioBubble = performance.now();
const vetorOrdenadoBubble = bubbleSort(vetorParaBubble);
const fimBubble = performance.now();
const tempoTotalBubble = fimBubble - inicioBubble;

// console.log("Vetor ordenado com Bubble Sort:", vetorOrdenadoBubble);
console.log("Tempo com Bubble Sort:", tempoTotalBubble.toFixed(5), "ms");

// Selection Sort:
const vetorParaSelection = [...vetorDesordenado];
const inicioSelection = performance.now();
const vetorOrdenadoSelection = selectionSort(vetorParaSelection);
const fimSelection = performance.now();
const tempoTotalSelection = fimSelection - inicioSelection;

// console.log("Vetor ordenado com Selection Sort:", vetorOrdenadoSelection);
console.log("Tempo com Selection Sort:", tempoTotalSelection.toFixed(5), "ms");

// Insertion Sort:
const vetorParaInsertion = [...vetorDesordenado];
const inicioInsertion = performance.now();
const vetorOrdenadoInsertion = insertionSort(vetorParaInsertion);
const fimInsertion = performance.now();
const tempoTotalInsertion = fimInsertion - inicioInsertion;

// console.log("Vetor ordenado com Insertion Sort:", vetorOrdenadoInsertion);
console.log("Tempo com Insertion Sort:", tempoTotalInsertion.toFixed(5), "ms");

// Comparação dos tempos
// 10 elementos:
// Tempo com Stooge: 0.10170 ms
// Tempo com Bubble Sort: 0.12200 ms
// Tempo com Selection Sort: 0.08080 ms
// Tempo com Insertion Sort: 0.05480 ms

// 100 elementos:
// Tempo com Stooge: 3.47950 ms
// Tempo com Bubble Sort: 0.87380 ms
// Tempo com Selection Sort: 0.26920 ms
// Tempo com Insertion Sort: 0.16460 ms

// 1000 elementos:
// Tempo com Stooge: 421.88780 ms
// Tempo com Bubble Sort: 5.10490 ms
// Tempo com Selection Sort: 3.20390 ms
// Tempo com Insertion Sort: 1.77190 ms

// 10000 elementos:
// Tempo com Stooge: 307548.34240 ms
// Tempo com Bubble Sort: 577.90780 ms
// Tempo com Selection Sort: 58.27540 ms
// Tempo com Insertion Sort: 26.13680 ms




