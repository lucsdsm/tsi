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