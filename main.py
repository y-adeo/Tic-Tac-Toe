import tkinter
from tkinter import *
from tkinter import ttk

# ---------- cores ---------- 
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# Criando janela principal
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

# Dividindo a janela

frame_resultado = Frame(janela, width=240, height=100, background=co1, relief='raised')
frame_resultado.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_corpo = Frame(janela, width=240, height=300, background=fundo, relief='flat')
frame_corpo.grid(row=1, column=0, sticky=NW)

# Configurando freme cima
app_x = Label(frame_resultado, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), background=co1, fg=co7)
app_x.place(x=25, y=10)

app_x = Label(frame_resultado, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 '), background=co1, fg=co0)
app_x.place(x=22, y=70)

app_xpontos = Label(frame_resultado, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), background=co1, fg=co0)
app_xpontos.place(x=80, y=20)


app_o = Label(frame_resultado, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), background=co1, fg=co4)
app_o.place(x=170, y=10)

app_o = Label(frame_resultado, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 '), background=co1, fg=co0)
app_o.place(x=169, y=70)

app_opontos = Label(frame_resultado, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), background=co1, fg=co0)
app_opontos.place(x=130, y=20)

# Configurando freme baixo

# Linhas verticais
app_lv = Label(frame_corpo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), background=co0, fg=co0)
app_lv.place(x=80, y=25)

app_lv = Label(frame_corpo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), background=co0, fg=co0)
app_lv.place(x=175, y=25)


# Linhas horizontais
app_lv = Label(frame_corpo, text='', width=48, relief='flat', padx=2, anchor='center', font=('Ivy 5 bold'), background=co0, fg=co0)
app_lv.place(x=80, y=25)

app_lv = Label(frame_corpo, text='', width=48, relief='flat', padx=2, anchor='center', font=('Ivy 5 bold'), background=co0, fg=co0)
app_lv.place(x=175, y=25)


janela.mainloop()
