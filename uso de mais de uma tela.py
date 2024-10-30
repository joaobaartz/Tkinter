import tkinter as tk

def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('janela nova')
    botao_fechar = tk.Button(janela2, text = "fechar", command = janela2.destroy)
    botao_fechar.grid(row = 1, column = 0 )
    
    
janela = tk.Tk()
botao = tk.Button(janela, text = 'ir para outra janela', command = abrir_janela)
botao.grid(row = 2,  column = 3)

janela.mainloop()