# inclusao das bibliotecas 
from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox

# Variaveis das cores
co0 = "#f0f3f5"  # Preto
co1 = "#f0f3f5"  # cinza
co2 = "#feffff"  # branco
co3 = "#38576b"  # black
co4 = "#403d3d"  # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"  # vermelha
co7 = "#93cd95"  # verde

# Criacao da janela
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

# Configurando frame cima

l_linha = Label(frame_cima, text="Lista telefônica", anchor=NE, font=('times 20 bold'), bg=co3, fg=co1)
l_linha.place(x=10, y=5)

# Configurando frame do meio

l_nome = Label(frame_baixo, text="Nome:*", anchor=NW, font=("arial 12 bold"),bg=co1, fg=co3)
l_nome.place(x=20, y=10)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('',10), highlightthickness=1)
e_nome.place(x=110, y=10)

l_email = Label(frame_baixo, text="Email:*", anchor=NW, font=("arial 12 bold"),bg=co1, fg=co3)
l_email.place(x=20, y=35)
e_email = Entry(frame_baixo, width=25, justify='left', font=('',10), highlightthickness=1)
e_email.place(x=110, y=35)

l_tel = Label(frame_baixo, text="Telefone:*", anchor=NW, font=("arial 12 bold"),bg=co1, fg=co3)
l_tel.place(x=20, y=60)
e_tel = Entry(frame_baixo, width=25, justify='left', font=('',10), highlightthickness=1)
e_tel.place(x=110, y=60)

l_pesq = Button(frame_baixo, text="Pesquisar", font=('Ivy 12 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_pesq.place(x=20, y=90)
e_pesq = Entry(frame_baixo, width=16, justify='left', font=('',10), highlightthickness=1)
e_pesq.place(x=110, y=90)

janela.mainloop()