const atletas = []

const athleteForm = document.getElementById("athleteForm")
const athleteList = document.getElementById("athleteList")

function ListAthletes() {
  athleteList.innerHTML = ""
  atletas.forEach(atleta => {
    const listItem = document.createElement("li")
    listItem.innerHTML = `
      <strong>Nome:</strong> ${atleta.nome}<br>
      <strong>Posição:</strong> ${atleta.posicao}<br>
      <strong>Altura:</strong> ${atleta.altura} m<br>
      <strong>Idade:</strong> ${atleta.idade} anos<br>
      <strong>Cidade:</strong> ${atleta.cidade} <br>
    `
    athleteList.appendChild(listItem)
  })
}

athleteForm.addEventListener("submit", event => {
  // Imprimir algo no console para teste
  console.log("Formulário enviado com sucesso!")
  event.preventDefault()

  const nomeInput = document.getElementById("nome").value
  const posicaoInput = document.getElementById("posicao").value
  const alturaInput = parseFloat(document.getElementById("altura").value)
  const idadeInput = parseInt(document.getElementById("idade").value)
  const cidadeInput = document.getElementById("cidade").value

  const novoAtleta = {
    nome: nomeInput,
    posicao: posicaoInput,
    altura: parseFloat(alturaInput.toFixed(2)),
    idade: parseInt(idadeInput.toString()),
    cidade: cidadeInput
  }

  atletas.push(novoAtleta)
  ListAthletes()

  athleteForm.reset()
})

document.addEventListener("DOMContentLoaded", () => {
  ListAthletes()
})
