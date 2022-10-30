from tkinter import Tk, Label, Button, Entry, Menu, Toplevel, Frame, StringVar

rootWindow = Tk()

rootWindow.title("Calculadora")
rootWindow.geometry("500x500")
rootWindow.configure(bg='black')
boton = ""
calculo = StringVar()


def digito(num):
    global boton
    boton = boton + str(num)
    calculo.set(boton)


def igual():
    try:
        global boton
        total = str(eval(boton))
        calculo.set(total)
        boton = ""
    except:

        calculo.set(" error ")


def limpiar():
    calculo.set("")


def donothing():
    filewin = Toplevel(rootWindow)
    button = Button(filewin, text="Do nothing button")
    button.pack()


menuBar = Menu(rootWindow, background='blue', fg='white')
fileMenu = Menu(menuBar, tearoff=0, bg='black', fg='white')
fileMenu.add_command(label="New", command=donothing)
fileMenu.add_command(label="Separar")

fileMenu.add_separator()

fileMenu.add_command(label="Salir", command=rootWindow.quit)
menuBar.add_cascade(label="Funciones", menu=fileMenu)

rootWindow.config(menu=menuBar)

btnCero = Button(rootWindow, text="0", bg='black', fg='white', command=lambda: digito(0))
btnUno = Button(rootWindow, text="1", bg='black', fg='white', command=lambda: digito(1))
btnDos = Button(rootWindow, text="2", bg='black', fg='white', command=lambda: digito(2))
btnTres = Button(rootWindow, text="3", bg='black', fg='white', command=lambda: digito(3))
btnCuatro = Button(rootWindow, text="4", bg='black', fg='white', command=lambda: digito(4))
btnCinco = Button(rootWindow, text="5", bg='black', fg='white', command=lambda: digito(5))
btnSeis = Button(rootWindow, text="6", bg='black', fg='white', command=lambda: digito(6))
btnSiete = Button(rootWindow, text="7", bg='black', fg='white', command=lambda: digito(7))
btnOcho = Button(rootWindow, text="8", bg='black', fg='white', command=lambda: digito(8))
btnNueve = Button(rootWindow, text="9", bg='black', fg='white', command=lambda: digito(9))
btnParentesisIzq = Button(rootWindow, text="(", bg='black', fg='white', command=lambda: digito("("))
btnParentesisDer = Button(rootWindow, text=")", bg='black', fg='white', command=lambda: digito(")"))
btnMas = Button(rootWindow, text="+", bg='black', fg='white', command=lambda: digito("+"))
btnDivision = Button(rootWindow, text="/", bg='black', fg='white', command=lambda: digito("/"))
btnMenos = Button(rootWindow, text="-", bg='black', fg='white', command=lambda: digito("-"))
btnMultiplicacion = Button(rootWindow, text="x", bg='black', fg='white', command=lambda: digito("*"))
btnC = Button(rootWindow, text="C", bg='black', fg='white', command=limpiar)
btnIgual = Button(rootWindow, text="=", bg='black', fg='white', command=igual)
border_color = Frame(rootWindow, background="white")
datos = Label(border_color, textvariable=calculo, bg='black', fg='white')
# lblResultado = Label(border_color)

btnParentesisIzq.place(relx=0.05, rely=0.77, relwidth=0.1, relheight=0.1)
btnCero.place(relx=0.17, rely=0.77, relwidth=0.1, relheight=0.1)
btnParentesisDer.place(relx=0.29, rely=0.77, relwidth=0.1, relheight=0.1)

btnMas.place(relx=0.05, rely=0.17, relwidth=0.1, relheight=0.1)
btnDivision.place(relx=0.05, rely=0.29, relwidth=0.1, relheight=0.1)

btnMenos.place(relx=0.17, rely=0.17, relwidth=0.1, relheight=0.1)
btnMultiplicacion.place(relx=0.17, rely=0.29, relwidth=0.1, relheight=0.1)

btnIgual.place(relx=0.29, rely=0.29, relwidth=0.1, relheight=0.1)
btnC.place(relx=0.29, rely=0.17, relwidth=0.1, relheight=0.1)

btnSiete.place(relx=0.05, rely=0.41, relwidth=0.1, relheight=0.1)
btnCuatro.place(relx=0.05, rely=0.53, relwidth=0.1, relheight=0.1)
btnUno.place(relx=0.05, rely=0.65, relwidth=0.1, relheight=0.1)

btnOcho.place(relx=0.17, rely=0.41, relwidth=0.1, relheight=0.1)
btnCinco.place(relx=0.17, rely=0.53, relwidth=0.1, relheight=0.1)
btnDos.place(relx=0.17, rely=0.65, relwidth=0.1, relheight=0.1)

btnNueve.place(relx=0.29, rely=0.41, relwidth=0.1, relheight=0.1)
btnSeis.place(relx=0.29, rely=0.53, relwidth=0.1, relheight=0.1)
btnTres.place(relx=0.29, rely=0.65, relwidth=0.1, relheight=0.1)

border_color.place(relx=0.45, rely=0.17, relwidth=0.5, relheight=0.7)
datos.place(relx=0.007, rely=0.007, relwidth=0.983, relheight=0.983)

rootWindow.mainloop()
