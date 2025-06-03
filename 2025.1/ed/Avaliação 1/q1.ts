export function maxRecursivo(arr: number[], n: number): number {
    if (n === 1) { // caso base
        return arr[0]; 
    }
    return Math.max(arr[n - 1], maxRecursivo(arr, n - 1)); // se n > 1, compara o último elemento com o máximo do restante do array
}

console.log(maxRecursivo([1, 2, 3, 4, 5], 5));  // retorna 5
console.log(maxRecursivo([10, 20, 30, 40, 50], 5)); // retorna 50
console.log(maxRecursivo([-1, -2, -3, -4, -5], 5)); // retorna -1
console.log(maxRecursivo([5, 4, 3, 2, 1], 5)); // retorna 5
console.log(maxRecursivo([100, 200, 300, 400, 500], 5)); // retorna 500