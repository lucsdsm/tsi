const THRESHOLD = 10;

export function fuzzysort(arr: number[]): void {
    fuzzysortRange(arr, 0, arr.length - 1);
}

function fuzzysortRange(arr: number[], left: number, right: number): void {
    if (left >= right) return;
    const tamanho = right - left + 1;
    if (tamanho <= THRESHOLD) {
        insertionSortRange(arr, left, right);
        return;
    }
    let minIdx = left;
    for (let i = left + 1; i <= right; i++) {
        if (arr[i] < arr[minIdx]) {
            minIdx = i;
        }
    }
    if (minIdx !== left) {
        [arr[left], arr[minIdx]] = [arr[minIdx], arr[left]];
    }
    for (let i = left; i < right; i++) {
        if (arr[i] > arr[i + 1]) {
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        }
    }
    fuzzysortRange(arr, left + 1, right - 1);
}

function insertionSortRange(arr: number[], left: number, right: number): void {
    for (let i = left + 1; i <= right; i++) {
        const chave = arr[i];
        let j = i - 1;
        while (j >= left && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chave;
    }
}

export function bubbleSort<T>(arr: T[]): T[] {
    const n = arr.length;
    let swapped: boolean;
    do {
      swapped = false;
      for (let i = 1; i < n; i++) {
        if (arr[i - 1] > arr[i]) {
          [arr[i - 1], arr[i]] = [arr[i], arr[i - 1]];
          swapped = true;
        }
      }
    } while (swapped);
    return arr;
}

export function selectionSort<T>(arr: T[]): T[] {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) {
        minIdx = j;
      }
    }
    if (minIdx !== i) {
      [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
    }
  }
  return arr;
}

export function insertionSort<T>(arr: T[]): T[] {
  for (let i = 1; i < arr.length; i++) {
    const key = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
  return arr;
}

const N = 10000;
const vetorDesordenado = Array.from({ length: N }, (_, i) => i + 1).sort(() => Math.random() - 0.5);
// console.log("Vetor desordenado:", vetorDesordenado);

// Fuzzy Sort:
const inicioFuzzy = performance.now();
const vetorOrdenadoFuzzy = fuzzysort(vetorDesordenado);
const fimFuzzy = performance.now();
const tempoTotalFuzzy = fimFuzzy - inicioFuzzy;
// console.log("Vetor ordenado com Fuzzy:", vetorOrdenadoFuzzy);
console.log("Tempo de execução com Fuzzy:", tempoTotalFuzzy.toFixed(5), "ms");

// Buble Sort:
const inicioBubble = performance.now();
const vetorOrdenadoBubble = bubbleSort(vetorDesordenado);
const fimBubble = performance.now();
const tempoTotalBubble = fimBubble - inicioBubble;
// console.log("Vetor ordenado com Bubble:", vetorOrdenadoBubble);
console.log("Tempo de execução com Bubble:", tempoTotalBubble.toFixed(5), "ms");

// Selection Sort:
const inicioSelection = performance.now();
const vetorOrdenadoSelection = selectionSort(vetorDesordenado);
const fimSelection = performance.now();
const tempoTotalSelection = fimSelection - inicioSelection;
// console.log("Vetor ordenado com Selection:", vetorOrdenadoSelection);
console.log("Tempo de execução com Selection:", tempoTotalSelection.toFixed(5), "ms");

// Insertion Sort:
const inicioInsertion = performance.now();
const vetorOrdenadoInsertion = insertionSort(vetorDesordenado);
const fimInsertion = performance.now();
const tempoTotalInsertion = fimInsertion - inicioInsertion;
// console.log("Vetor ordenado com Insertion:", vetorOrdenadoInsertion);
console.log("Tempo de execução com Insertion:", tempoTotalInsertion.toFixed(5), "ms");

// 10 números:
// Tempo de execução com Fuzzy: 0.13240 ms
// Tempo de execução com Bubble: 0.10480 ms
// Tempo de execução com Selection: 0.11690 ms
// Tempo de execução com Insertion: 0.05880 ms

// 100 números:
// Tempo de execução com Fuzzy: 0.70770 ms
// Tempo de execução com Bubble: 0.07030 ms
// Tempo de execução com Selection: 0.40030 ms
// Tempo de execução com Insertion: 0.07530 ms

// 1000 números:
// Tempo de execução com Fuzzy: 16.30570 ms
// Tempo de execução com Bubble: 0.09370 ms
// Tempo de execução com Selection: 4.30400 ms
// Tempo de execução com Insertion: 0.15800 ms

// 10.000 números:
// Tempo de execução com Fuzzy: 213.52050 ms
// Tempo de execução com Bubble: 0.42500 ms
// Tempo de execução com Selection: 99.04310 ms
// Tempo de execução com Insertion: 1.16510 ms

// 100.000 números:
// Fuzzy: RangeError: Maximum call stack size exceeded

// O fuzzy tem um bom desempenho em comparação aos outros algoritmos de ordenação com listas pequenas de até aproximadamente 100 números,
// mas a partir disso, o desempenho do fuzzy diminui drasticamente, de modo que com 100.000 números, ele não consegue completar a ordenação,
// dando um erro de "Maximum call stack size exceeded".