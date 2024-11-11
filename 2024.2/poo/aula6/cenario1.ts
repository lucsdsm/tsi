// Cenário
// • Em uma empresa, existem Funcionários que trabalham em diferentes
// Departamentos. Cada funcionário pertence a um departamento específico, mas um
// departamento pode ter vários funcionários.

// • Instruções
// 1. Crie uma classe chamada Departamento, que possui:
// o Um atributo nome (do tipo string), que representa o nome do
// departamento.
// o Um método exibirInformacoes que mostra no console o nome do
// departamento.

// 2. Crie uma classe chamada Funcionario, que possui:
// o Um atributo nome (do tipo string), que representa o nome do
// funcionário.
// o Um atributo departamento do tipo Departamento para associar o
// funcionário ao seu departamento.
// o Um método exibirInformacoes que mostra no console o nome do
// funcionário e o nome do seu departamento.

// 3. No código principal, faça o seguinte:
// o Crie duas instâncias de Departamento chamadas departamento1 e
// departamento2, com nomes como "TI" e "RH".
// o Crie três instâncias de Funcionario e associe cada uma a um
// departamento.
// o Chame o método exibirInformacoes de cada Funcionario para exibir as
// informações no console.

class Departamento {
  nome: string;

  constructor(nome: string) {
    this.nome = nome;
  }

  exibirInformacoes() {
    return "Departamento: " + this.nome;
  }
}

class Funcionario {
  nome: string;
  departamento: Departamento;
 
  constructor(nome: string, departamento: Departamento) {
    this.nome = nome;
    this.departamento = departamento;
  }

  exibirInformacoes() {
    return "Funcionário: " + this.nome + "; " + this.departamento.nome
  }
 
}

let departamento1 = new Departamento("TI");
let departamento2 = new Departamento("RH");

let funcionario1 = new Funcionario("Alice", departamento1);
let funcionario2 = new Funcionario("Bruno", departamento1);
let funcionario3 = new Funcionario("Carla", departamento2);

console.log(funcionario1.exibirInformacoes())
console.log(funcionario2.exibirInformacoes())
console.log(funcionario3.exibirInformacoes())
