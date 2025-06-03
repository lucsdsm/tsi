export function maxRecursivo(arr: number[], n: number): number {
    if (n === 1) {
        return arr[0];
    }
    return Math.max(arr[n - 1], maxRecursivo(arr, n - 1));
}

const vetor = [3, 5, 2, 9, 1];
const tamanho = vetor.length;
const maximo = maxRecursivo(vetor, tamanho);
console.log(`O valor máximo do vetor é: ${maximo}`); 