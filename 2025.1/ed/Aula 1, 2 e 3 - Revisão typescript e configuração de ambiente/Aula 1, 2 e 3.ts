let nome = "Lucas"
console.log(`Olá ${nome}, tudo bem?`)

// Criar um array com nomes:
let nomes: string[] = ["Lucas"]
// Imprimir nome por nome do array:
for (let i = 0; i < nomes.length; i++) {
    console.log(nomes[i])
}

let fruta = "banana"

switch (fruta) {
    case "banana":
        console.log("A fruta é banana")
        break
    case "maçã":
        console.log("A fruta é maçã")
        break
    default:
        console.log("Fruta desconhecida")
}

// Criar uma função que retorne "Olá, Visitante" caso não sejam passados parâmetros
function ola(nome: string) {
    console.log(`Olá ${nome}`)
}

function max(...numeros: number[]): number {
    let maior = numeros[0]
    for (let i = 1; i < numeros.length; i++) {
        if (numeros[i] > maior) {
            maior = numeros[i]
        }
    }
    return maior
}

console.log(max(1, 3, 2))

// Um array de frutas
let frutas: string[] = ["banana", "maçã", "laranja"]
// Imprimr as frutas formatadas com - usando o join
console.log(frutas.join(" - "))