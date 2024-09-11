import tkinter as tk

def ao_clicar():
    print("Botão clicado")

janela = tk.Tk()
janela.title("Exemplo simples de botão")
janela.geometry("400x400")

botao = tk.Button(janela, text="Clique", command=ao_clicar)
botao.pack(pady=10)

janela.mainloop()