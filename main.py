from tkinter import *

root = Tk()
root.geometry('500x500+0+0')
root.title('desafio tela de cadastro com tkinter')

def imprimir():
    print('nome       : {}'.format(nomee.get()))
    print('email      : {}'.format(emae.get()))
    print('telefone   : {}'.format(tele.get()))
    print('observações: {}'.format(obse.get('1.0',END)))
    
Label(root,text='NOME:').place(x=10,y=30)
nomee= Entry(root,width=40)
nomee.place(x=10,y=50)

Label(root,text='EMAIL:').place(x=10,y=80)
emae= Entry(root,width=40)
emae.place(x=10,y=100)

Label(root,text='TELEFONE:').place(x=10,y=130)
tele= Entry(root,width=40)
tele.place(x=10,y=150)

Label(root,text='OBS.:').place(x=10,y=180)
obse= Text(root,width=35,height=7)
obse.place(x=10,y=200)

btn = Button(root,text='imprimir',command=imprimir)
btn.place(x=15,y=325)


root.mainloop()