import {bubbleSort} from "./Algoritmos";
import {selectionSort} from "./Algoritmos";
import {insertionSort} from "./Algoritmos";
import {shellSort} from "./Algoritmos";
import { mergeSort } from "./Algoritmos";
import { quickSort } from "./Algoritmos";

const N = 1000;

// Criar vetor ordenado de N itens sem itens repetidos:
const vetorOrdenado = Array.from({ length: N }, (_, i) => i + 1);
// console.log("Vetor ordenado:", vetorOrdenado);

// Criar vetor desordenado de N itens sem itens repetidos:
const vetorDesordenado = Array.from({ length: N }, (_, i) => i + 1).sort(() => Math.random() - 0.5);
// console.log("Vetor desordenado:", vetorDesordenado);

// Exemplos de uso:

// Buble Sort:
const inicioBubble = performance.now();
const vetorOrdenadoBubble = bubbleSort(vetorDesordenado);
const fimBubble = performance.now();
const tempoTotalBubble = fimBubble - inicioBubble;
// console.log("Vetor ordenado com Bubble:", vetorOrdenadoBubble);
console.log("Tempo total de execução com Bubble:", tempoTotalBubble.toFixed(5), "milissegundos");

// Selection Sort:
const inicioSelection = performance.now();
const vetorOrdenadoSelection = selectionSort(vetorDesordenado);
const fimSelection = performance.now();
const tempoTotalSelection = fimSelection - inicioSelection;
// console.log("Vetor ordenado com Selection:", vetorOrdenadoSelection);
console.log("Tempo total de execução com Selection:", tempoTotalSelection.toFixed(5), "milissegundos");

// Insertion Sort:
const inicioInsertion = performance.now();
const vetorOrdenadoInsertion = insertionSort(vetorDesordenado);
const fimInsertion = performance.now();
const tempoTotalInsertion = fimInsertion - inicioInsertion;
// console.log("Vetor ordenado com Insertion:", vetorOrdenadoInsertion);
console.log("Tempo total de execução com Insertion:", tempoTotalInsertion.toFixed(5), "milissegundos");

// Shell Sort:
const inicioShell = performance.now();
const vetorOrdenadoShell = shellSort(vetorDesordenado);
const fimShell = performance.now();
const tempoTotalShell = fimShell - inicioShell;
// console.log("Vetor ordenado com Shell:", vetorOrdenadoShell);
console.log("Tempo total de execução com Shell:", tempoTotalShell.toFixed(5), "milissegundos");

// Merge Sort:
const inicioMerge = performance.now();
const vetorOrdenadoMerge = mergeSort(vetorDesordenado);
const fimMerge = performance.now();
const tempoTotalMerge = fimMerge - inicioMerge;
// console.log("Vetor ordenado com Merge:", vetorOrdenadoMerge);
console.log("Tempo total de execução com Merge:", tempoTotalMerge.toFixed(5), "milissegundos");

// Quick Sort:
const inicioQuick = performance.now();
const vetorOrdenadoQuick = quickSort(vetorDesordenado);
const fimQuick = performance.now();
const tempoTotalQuick = fimQuick - inicioQuick;
// console.log("Vetor ordenado com Quick:", vetorOrdenadoQuick);
console.log("Tempo total de execução com Quick:", tempoTotalQuick.toFixed(5), "milissegundos");