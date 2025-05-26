// 1. Implemente uma função recursiva que permita somar os elementos de um vetor de inteiros.
function somaRecursiva(vetor: number[], indice: number = 0): number {
    if (indice >= vetor.length) {
        return 0;
    }
    return vetor[indice] + somaRecursiva(vetor, indice + 1);
}

const numeros = [1, 2, 3, 4, 5];
const resultado = somaRecursiva(numeros);
console.log(`Soma dos elementos do vetor: ${resultado}`);

// 2. Implemente uma função contagemRegressiva(n: number) que imprime no console uma contagem de n até 0.
function contagemRegressiva(n: number): void {
    if (n < 0) {
        return;
    }
    console.log(n);
    contagemRegressiva(n - 1);
}

const numeroInicial = 5;
console.log(`Contagem regressiva de ${numeroInicial}:`);
contagemRegressiva(numeroInicial);

// 5. A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo multiplicação(n1, n2) que calcule a multiplicação de dois inteiros.

function multiplicacao(n1: number, n2: number): number {
    if (n2 === 0) {
        return 0;
    }
    if (n2 > 0)
        return n1 + multiplicacao(n1, n2 - 1);
    return -multiplicacao(n1, -n2); // Se n2 for negativo, inverte o sinal
}

const num1 = 2;
const num2 = 4;
const produto = multiplicacao(num1, num2);
console.log(`Multiplicação de ${num1} e ${num2}: ${produto}`);

// 8. Implemente uma função recursiva para dizer se uma palavra é palíndroma sem normaliza-la.

function ehPalindromo(palavra: string, inicio: number = 0, fim: number = palavra.length - 1): boolean {
    if (inicio >= fim) {
        return true;
    }
    if (palavra[inicio] !== palavra[fim]) {
        return false;
    }
    return ehPalindromo(palavra, inicio + 1, fim - 1);
}

const palavraTeste = "radar";
const resultadoPalindromo = ehPalindromo(palavraTeste);
console.log(`A palavra "${palavraTeste}" é palíndroma? ${resultadoPalindromo}`);

