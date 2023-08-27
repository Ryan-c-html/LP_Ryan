# inclusão das bibliotecas 
from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox

# Variaveis das cores

co0 = "#f0f3f5" # preto
co1 = "#f0f3f5" # cinza
co2 = "#feffff" # branco
co3 = "#38576b" # black

# Criação da janela
janela = Tk()
janela.title("Agenda")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames

frame_cima = Frame(janela, width=500, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=240, bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10,pady=1, sticky=NSEW)

janela.mainloop()
# 



