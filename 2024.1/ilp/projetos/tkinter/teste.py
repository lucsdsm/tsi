import tkinter as tk

def on_button_click():
    label.config(text="Você clicou no botão!")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo 1")

# Criação de um botão
button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack()

# Criação de um rótulo (label)
label = tk.Label(root, text="Aguardando ação...")
label.pack()

# Inicia o loop da aplicação
root.mainloop()
