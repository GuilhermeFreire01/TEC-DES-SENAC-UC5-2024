import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de caixa de texto")

texto = tk.Text(janela, height=5, width=40)
texto.pack(pady=10)

janela.mainloop()