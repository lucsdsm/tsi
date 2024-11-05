// Crie uma classe base Funcionario:
// Propriedades:
// nome (string)
// salarioBase (number)

// Construtor: inicialize as propriedades nome e salarioBase.

// Método:
// calcularSalario() que retorna o salário base.

// Crie uma classe Gerente que herda de Funcionario:
// Adicione uma nova propriedade bonus (number).
// Modifique o método calcularSalario() para retornar o salário base somado ao bônus.

// Crie uma classe Vendedor que herda de Funcionario:

// Adicione uma nova propriedade comissao (number).
// Modifique o método calcularSalario() para retornar o salário base somado à comissão.

// Teste o código:
// Crie uma instância de Funcionario, Gerente e Vendedor.
// Exiba o salário de cada um usando o método calcularSalario.

class Funcionario {
  nome: string;
  salarioBase: number;
 
  constructor(nome: string, salarioBase: number) {
    this.nome = nome;
    this.salarioBase = salarioBase;
  }
 
  calcularSalario() {
     return this.salarioBase;
  }
}

class Gerente extends Funcionario {
bonus: number;
  
  constructor(nome: string, salarioBase: number, bonus: number) {
  super(nome, salarioBase);
      this.bonus = bonus;
  }
  
  calcularSalario() {
     return this.salarioBase + this.bonus;
  }
}

class Vendedor extends Funcionario {
comissao: number;
  
  constructor(nome: string, salarioBase: number, comissao: number) {
  super(nome, salarioBase);
      this.comissao = comissao;
  }
  
  calcularSalario() {
     return this.salarioBase + this.comissao;
  }
}

let f: Funcionario = new Funcionario("Lucas", 1200);
f.calcularSalario();


