interface Atleta {
    nome: string;
    posicao: string;
    altura: number;
    idade: number;
    cidade: string;
}

const atletas: Atleta[] = []

const atheletForm = document.getElementById('athleteForm') as HTMLFormElement;
const athleteList = document.getElementById('athleteList') as HTMLUListElement;

function ListAthletes(): void {
    athleteList.innerHTML = '';
    atletas.forEach(atleta => {
        const listItem = document.createElement('li');
        listItem.textContent = `
        Nome: ${atleta.nome} <br> 
        Posição: ${atleta.posicao} <br>
        Altura: ${atleta.altura} cm <br>
        Idade: ${atleta.idade} anos <br>
        Cidade: ${atleta.cidade} <br>
        `;
        athleteList.appendChild(listItem);
    });
}

atheletForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const nomeInput = (document.getElementById('nome') as HTMLInputElement).value;
    const posicaoInput = (document.getElementById('posicao') as HTMLInputElement).value;
    const alturaInput = parseFloat((document.getElementById('altura') as HTMLInputElement).value);
    const idadeInput = parseInt((document.getElementById('idade') as HTMLInputElement).value);
    const cidadeInput = (document.getElementById('cidade') as HTMLInputElement).value;

    const novoAtleta: Atleta = {
        nome: nomeInput,
        posicao: posicaoInput,
        altura: parseFloat(alturaInput.toFixed(2)),
        idade: parseInt(idadeInput.toString()),
        cidade: cidadeInput
    }

    atletas.push(novoAtleta);
    ListAthletes();

    atheletForm.reset();
})

document.addEventListener('DOMContentLoaded', () => {
    ListAthletes();
});