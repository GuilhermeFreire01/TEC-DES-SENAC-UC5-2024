import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo simples de entrada")

entrada = tk.Entry(janela)
entrada.pack(pady=10)

janela.mainloop()