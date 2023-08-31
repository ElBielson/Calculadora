from tkinter import *
from tkinter import ttk

#cores
cor_preta = '#000000'
cor_laranja = '#ffa500'
cor_cinzaclaro = '#d3d3d3'
cor_branca = '#FFFFFF'
cor_cinzaescuro = '#474a51'

#Configuração da Janela:
janela =Tk()
janela.title('Calculadora')
janela.geometry('400x630')
janela.config(bg=cor_preta)



#var valores
todos_valores = ''

#func: mostrar número:
def valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    resultado = eval('1+1')
    texto.set(todos_valores)


#func: calcular:
def calcular():
    resultado=eval(todos_valores)
    texto.set(resultado)

def limpar():
    todos_valores = ''
    texto.set('')

#label:
texto = StringVar()
label1 = Label(textvariable=texto, width=17, height=2, padx=7, relief=FLAT, anchor='e', bg=cor_preta, fg=cor_branca, font=('Ivy 20 bold'))
label1.place(x=0 , y=170)

#Botão:
b_2 = Button(command=limpar,text='C', width=8, height=2, bg=cor_cinzaclaro, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_2.place(x=70, y=240)
b_3 = Button(command=lambda: valores(event='%'),text='%', width=2, height=2, bg=cor_cinzaclaro, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_3.place(x=210, y=240)
b_4 = Button(command=lambda: valores(event='/'), text='÷', width=2, height=2, bg=cor_laranja, bd=0, fg=cor_branca, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_4.place(x=280, y=240)
b_5 = Button(command=lambda: valores(event='*'),text='x', width=2, height=2, bg=cor_laranja,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_5.place(x=280, y=310)
b_6 = Button(command=lambda: valores(event='-'),text='-', width=2, height=2, bg=cor_laranja,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_6.place(x=280, y=380)
b_7 = Button(command=lambda: valores(event='+'),text='+', width=2, height=2, bg=cor_laranja,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_7.place(x=280, y=450)
b_8 = Button(command=calcular,text='=', width=2, height=2, bg=cor_laranja,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_8.place(x=280, y=520)
b_9 = Button(command=lambda: valores(event='7'),text='7', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_9.place(x=74, y=310)
b_10 = Button(command=lambda: valores(event='8'),text='8', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_10.place(x=140, y=310)
b_11 = Button(command=lambda: valores(event='9'),text='9', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_11.place(x=210, y=310)
b_12 = Button(command=lambda: valores(event='4'),text='4', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_12.place(x=74, y=380)
b_13 = Button(command=lambda: valores(event='5'),text='5', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_13.place(x=140, y=380)
b_14 = Button(command=lambda: valores(event='6'),text='6', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_14.place(x=210, y=380)
b_15 = Button(command=lambda: valores(event='1'),text='1', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_15.place(x=74, y=450)
b_16 = Button(command=lambda: valores(event='2'),text='2', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_16.place(x=140, y=450)
b_17 = Button(command=lambda: valores(event='3'),text='3', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_17.place(x=210, y=450)
b_18 = Button(command=lambda: valores(event='0'),text='0', width=7, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_18.place(x=74, y=520)
b_19 = Button(command=lambda: valores(event='.'),text=',', width=2, height=2, bg=cor_cinzaescuro,fg=cor_branca , bd=0, relief=FLAT, overrelief=FLAT, font=('Ivy 13 bold'))
b_19.place(x=210, y=520)





janela.mainloop()