// ITERAÇÃO
function soma1(n: number): number {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}

// RECURSÃO

// Soma recursiva
function soma2(n: number): number {
    if (n == 1) { // Caso base
        return 1;
    }
    else { // Caso recursivo
        return n + soma2(n - 1);
    }
}

function fibonacci(n: number): number {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

function somaVetor(vetor: number[], n: number): number {
    if (n < 0) return 0;
    return vetor[n] + somaVetor(vetor, n - 1);
}

function contagemRegressiva(n: number): number {
    if (n == 1) {
        return 1;
    }
    else {
        console.log(n);
        return contagemRegressiva(n - 1);
    }
}

console.log(contagemRegressiva(5)); // 5 4 3 2 1
const v = [1, 2, 3, 4, 5];
console.log(`Soma do vetor: ${somaVetor(v, v.length - 1)}`);