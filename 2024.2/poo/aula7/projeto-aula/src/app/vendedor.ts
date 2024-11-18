export class Vendedor {
    nome: string;
    salarioBase: number;
    totalVendido:  number;

    constructor(nome: string, salarioBase: number, totalVendido: number) {
        this.nome = nome;
        this.salarioBase = salarioBase;
        this.totalVendido = totalVendido;
    }

    calcularSalario(): number {
        let percentual = this.totalVendido * 0.05;
        let salarioTotal = this.salarioBase + percentual;
        return salarioTotal
    }
}
