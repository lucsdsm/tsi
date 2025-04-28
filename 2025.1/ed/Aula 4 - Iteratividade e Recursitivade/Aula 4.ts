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

console.log(`Fibonacci: ${fibonacci(5)}`); 

// 1
function somaVetor(vetor: number[], n: number): number {
    if (n < 0) return 0;
    return vetor[n] + somaVetor(vetor, n - 1);
}

const v = [1, 2, 3, 4, 5];
console.log(`Soma do vetor: ${somaVetor(v, v.length - 1)}`);

// 2
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

// 3
function potencia(base: number, expoente: number): number {
    if (expoente == 0) return 1;
    return base * potencia(base, expoente - 1);
}

console.log(`Potência: ${potencia(2, 3)}`); // 8

// 4
function mdc(a: number, b: number): number {
    if (b == 0) return a;
    return mdc(b, a % b);
}

console.log(`MDC: ${mdc(48, 18)}`); // 


// 5
function multiplicacao(a: number, b: number): number {
    if (b == 0) return 0;
    return a + multiplicacao(a, b - 1);
}

console.log(`Multiplicação: ${multiplicacao(3, 4)}`); // 12

// 6
function converteNaturalBinario(n: number): string {
    if (n == 0) return "";
    return converteNaturalBinario(Math.floor(n / 2)) + (n % 2);
}

console.log(`Número binário: ${converteNaturalBinario(2)}`); // 10  