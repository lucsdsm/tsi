import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Usuario } from './usuario'
import { UsuarioService } from './usuario.service'
import { JsonPipe } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, JsonPipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  usuarios: Usuario[] = [];
  
  constructor(private servico: UsuarioService) {}

  onGetUsuarios(): void {
    this.servico.getUsuarios().subscribe({
      next: (dados) => {
        console.log(dados);
      },
      error: (erro) => {
        console.log(erro)
      },
      complete: () => {
        console.log('Chamada finalizada.')
      }
    })
  }
}
