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



# Visual freme resultado
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







# Criando a Lógica do jogo
jogador_1 = 'X'
jogador_2 = 'O'

ponto_jog1 = 0
ponto_jog2 = 0

tabela = [['1', '2', '3'] , ['4', '5', '6'] , ['7', '8', '9']]



jogando = 'X'
contador = 0
jogar = ''



def iniciar_jogo():
    def controlar(i):
        global jogando
        global contador
        global jogar
        global cor

        #Comparando valor recebido
        if i==str(1):
            #Verificar se a posição está vazia
            if b_0['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')


        if i==str(2):
            #Verificar se a posição está vazia
            if b_1['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')
        

        if i==str(3):
            #Verificar se a posição está vazia
             if b_2['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')


        if i==str(4):
            #Verificar se a posição está vazia
            if b_3['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')


        if i==str(5):
            #Verificar se a posição está vazia
            if b_4['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')


        if i==str(6):
            #Verificar se a posição está vazia
            if b_5['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')
        

        if i==str(7):
            #Verificar se a posição está vazia
             if b_6['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')


        if i==str(8):
            #Verificar se a posição está vazia
            if b_7['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')
        

        if i==str(9):
            #Verificar se a posição está vazia
             if b_8['text']=='':
                #Verificando quem está jogando e definir a cor
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                #Defininco cor do texto do botão e marcar posição com o valor de quem está jogando
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[[0][0]] = jogando

                #Verificando quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #Add no contador
                contador+=1

                if contador>=5:
                    #[linha][coluna]
                    #linhas
                    if tabela[0][0] == tabela [0][1] == [0][2] != '':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                        vencedor(jogando)
                    
                    #colunas
                    if tabela[0][0] == tabela [1][0] == [2][0] != '':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                        vencedor(jogando)

                    #diagonais
                    if tabela[0][0] == tabela [1][1] == [2][2] != '':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Empate')






        print(i)

    def vencedor(i):
        pass

    def fim():
        pass


    # Visual freme corpo
    # Linhas verticais
    app_lv = Label(frame_corpo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), background=co0, fg=co0)
    app_lv.place(x=80, y=25)

    app_lv = Label(frame_corpo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), background=co0, fg=co0)
    app_lv.place(x=175, y=25)


    # Linhas horizontais
    app_lh = Label(frame_corpo, text='', width=200, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'), background=co0, fg=co0)
    app_lh.place(x=30, y=73)

    app_lh = Label(frame_corpo, text='', width=200, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'), background=co0, fg=co0)
    app_lh.place(x=30, y=143)   



    # Botões

    # Linha 0
    b_0 = Button(frame_corpo, command=lambda:controlar('1'), text='', width=3, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_0.place(x=25, y=20)

    b_1 = Button(frame_corpo, command=lambda:controlar('2'), text='', width=5, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_1.place(x=89, y=20)

    b_2 = Button(frame_corpo, command=lambda:controlar('3'), text='', width=3, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_2.place(x=182, y=20)

    # Linha 1
    b_3 = Button(frame_corpo, command=lambda:controlar('4'), text='', width=3, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_3.place(x=25, y=85)

    b_4 = Button(frame_corpo, command=lambda:controlar('5'), text='', width=5, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_4.place(x=89, y=85)

    b_5 = Button(frame_corpo, command=lambda:controlar('6'), text='', width=3, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_5.place(x=182, y=85)

    # Linha 2
    b_6 = Button(frame_corpo, command=lambda:controlar('7'), text='', width=3, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_6.place(x=25, y=155)

    b_7 = Button(frame_corpo, command=lambda:controlar('8'), text='', width=5, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_7.place(x=89, y=155)

    b_8 = Button(frame_corpo, command=lambda:controlar('9'), text='', width=3, relief='flat', font=('Ivy 18 bold'), overrelief=RIDGE, background=fundo, fg=co7)
    b_8.place(x=182, y=155)


# Botão Jogar
b_jogar = Button(frame_corpo, command=iniciar_jogo, text='Jogar', width=10, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, background=fundo, fg=co0)
b_jogar.place(x=85, y=215)



janela.mainloop()
