from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry
from tkinter import ttk

###cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


###janela

janela = Tk()
janela.title("")
janela.geometry('1044x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

#estilizando e dividindo janelas
frame_up = Frame(janela, width=310, height=50, background=co2, relief='flat')
frame_up.grid(row=0, column=0)

frame_down = Frame(janela, width=310, height=400, background=co1, relief='flat')
frame_down.grid(row=1, column=0, padx=1, pady=1, sticky=NSEW )

frame_direita = Frame(janela, width=588, height=400, background=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)



###label Up
app_nome = Label(frame_up, text='Formulário - Consultoria', anchor= NW, font =('Ivy 13 bold'), fg=co1, bg=co2, relief='flat')
app_nome.place(x=10, y=20)



###label down

#nome
l_nome = Label(frame_down, text='Nome', anchor= NW, font =('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_down, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

#email
l_email = Label(frame_down, text='E-mail', anchor= NW, font =('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_down, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

#telefone
l_tel = Label(frame_down, text='Telefone', anchor= NW, font =('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_tel.place(x=10, y=130)
e_tel = Entry(frame_down, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

#data
l_data = Label(frame_down, text='Data da consulta', anchor= NW, font =('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_data.place(x=10, y=190)
e_data = DateEntry(frame_down, width=12, background='darkblue', foreground= 'white', borderwith=2, year=2023)
e_data.place(x=15, y=220)

#estado
l_estado = Label(frame_down, text='Estado da consulta', anchor= NW, font =('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_down, width=22, justify='left', relief='solid')
e_estado.place(x=160, y=220)

#sobre
l_sobre = Label(frame_down, text='Comentários', anchor= NW, font =('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_sobre.place(x=15, y=260)
e_sobre = Entry(frame_down, width=45, justify='left', relief='solid')
e_sobre.place(x=15, y=290)

#button inserir
b_inserir = Button(frame_down, text='Cadastrar', width=10, font =('Ivy 7 bold'), fg=co1, bg=co2, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

#button atualizar
b_atualizar = Button(frame_down, text='Atualizar', width=10, font =('Ivy 7 bold'), fg=co1, bg=co6, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)

#button deletar
b_del = Button(frame_down, text='Deletar', width=10, font =('Ivy 7 bold'), fg=co1, bg=co7, relief='raised', overrelief='ridge')
b_del.place(x=205, y=340)



## frame direita

lista = [
    [1, 'João', 'joao@gmail.com', 1234567, '12/19/2022', 'Normal', 'Presencial'],
    [2, 'Maria', 'maria@gmail.com', 1234567, '12/19/2022', 'Normal', 'Presencial'],
    [3, 'Fulano', 'fulano@gmail.com', 1234567, '12/19/2022', 'Urgente', 'Presencial'],
    [4, 'Sicrano', 'sicrano@gmail.com', 1234567, '12/19/2022', 'Normal', 'Presencial'],
    [5, 'Beltrano', 'joao@gmail.com', 1234567, '12/19/2022', 'Normal', 'Presencial']
]
list_header = ['Id', 'Nome', 'E-mail', 'Telefone', 'Data', 'Estado', 'Sobre']


##criando tabela
tree = ttk.Treeview(frame_direita, selectmode='extended', columns= list_header, show='headings')

#vertical
vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)

#horizontal
hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)


tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frame_direita.grid_rowconfigure(0, weight=12)

#alinhamento header/linhas
hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'center', 'center']
h = [30, 170, 140, 100, 120, 50, 100]
n = 0

for col in list_header:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])
    
    n+=1
    
for item in lista:
    tree.insert('', 'end', values=item)    


janela.mainloop()