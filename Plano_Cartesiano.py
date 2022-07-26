from cProfile import label
from tkinter import BOTH, W, Button, Entry, Frame, Label, StringVar, Tk, Canvas, Toplevel, messagebox


def destruir():
    messagebox.showinfo(title="Chau" , message="😥")
    ventana_principal.destroy()


ventana_principal = Tk()
ventana_principal.title("Plano Cartesiano")
ventana_principal.resizable(False,False)
ventana_principal.config(bg ="gray")
ventana_principal.geometry("750x400")

Frame1 = Frame(ventana_principal)
Frame1.config(bg="white", width=1480, height=680)
Frame1.pack(fill=BOTH, padx=10, pady=10)



label1 = Label(Frame1, text="GRAFICADORA DE FUNCIONES LINEALES", fg="black", font=("Arial", 15)).place(x= 170, y= 20)

label2 = Label(Frame1, text="Ingrese el valor de X1: "). place(x=50,y= 150)

label3 = Label(Frame1, text="Ingrese el valor de Y1: "). place(x=50, y= 200)

label4 = Label(Frame1, text="Ingrese el valor de X2: "). place(x= 380, y = 150)

label5 = Label(Frame1, text="Ingrese el valor de Y2: "). place(x= 380, y = 200)




entrada1 = Entry(Frame1, bg="gray", highlightthickness=2, highlightcolor="red"). place(x=190, y= 150)

entrada2 = Entry(Frame1, bg="gray", highlightthickness=2, highlightcolor="red"). place(x=190, y= 200)

entrada3 = Entry(Frame1, bg="gray", highlightthickness=2, highlightcolor="red"). place(x=520, y= 150)

entrada4 = Entry(Frame1, bg="gray", highlightthickness=2, highlightcolor="red"). place(x=520, y= 200)

bt1=Button(Frame1, text="     CERRAR     ", command=destruir).place(x=640,y=350)


def graficar():
    ventana_graficacion = Toplevel()
    ventana_graficacion.geometry("800x500")
    ventana_graficacion.title="GRAFICA"
    ventana_graficacion.resizable(False,False)
    
    Frame_graficacion = Frame(ventana_graficacion)
    Frame_graficacion.config(bg="white", width=780, height=480)
    Frame_graficacion.pack(fill=BOTH, padx=10, pady=10)
    
    c = Canvas(Frame_graficacion, width=760, height=460, bg="white")
    c.place(x=10, y= 10)
    
    ejeY= c.create_line(380,0,380,760, fill="black")
    ejeX= c.create_line(0,230,760,230, fill="black")
    la1= Label(c, text="Y"). place(x=385, y=0)
    la2= Label(c, text="X"). place(x= 750, y=230)
   

bt2 = Button(Frame1, text= "   GRAFICAR   ", command=graficar). place(x=5, y=350)





ventana_principal.mainloop()
