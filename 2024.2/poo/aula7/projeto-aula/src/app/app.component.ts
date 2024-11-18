import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Vendedor } from './vendedor';
import { CurrencyPipe } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, CurrencyPipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  vendedor: Vendedor = new Vendedor('', 0, 0);
  salarioTotal = 0;

  onSalarioTotal() {
    this.salarioTotal = this.vendedor.calcularSalario();
  }
}
