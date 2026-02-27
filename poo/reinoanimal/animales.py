import tkinter as tk
from PIL import Image, ImageTk

def ventana():
    global v1
    v1=tk.Tk()
    v1.title("Animales")
    v1.geometry("600x600")
    v1.config(bg="#A0D378")

    etq1=tk.Label(v1,text="REINO ANIMAL",font=("Comic Sans MS",25),fg="GREEN", bg="#A0D378")
    etq1.pack()
    
    imagen=Image.open("C:/Users/DELL/Documents/reinoanimal")
    
    rd1=tk.Radiobutton(v1,text="Elefante",value=1,font=("Comic Sans MS",18), bg="#5BAE1C")
    rd1.pack(pady=20)
    rd2=tk.Radiobutton(v1,text="Jirafa",value=2,font=("Comic Sans MS",18), bg="#5BAE1C")
    rd2.pack(pady=20)
    rd3=tk.Radiobutton(v1,text="Castor",value=3,font=("Comic Sans MS",18), bg="#5BAE1C")
    rd3.pack(pady=20)
    rd4=tk.Radiobutton(v1,text="Leon",value=4,font=("Comic Sans MS",18), bg="#5BAE1C")
    rd4.pack(pady=20)
    boton1=tk.Button(v1,text="Visualizar",font=("Comic Sans MS",18), bg="#5BAE1C")
    boton1.pack(pady=20)
        
    v1.mainloop()
    
    
def destruir(ventana_actual):
    ventana_actual.destroy()
    ventana()
    
def ventana2():
    v1.destroy()
    v2=tk.Tk()
    v2.title("707")
    v2.geometry("400x500")
    v2.config(bg="#ECC1FF")

    etq2=tk.Label(v2,text="TOOM TOOM",font=("Comic Sans MS",14),fg="black", bg="#ECC1FF")
    etq2.pack()

    boton2=tk.Button(v2,text="Volver",font=("Comic Sans MS",12), bg="#8974A7",command=lambda:destruir(v2))
    boton2.pack(pady=20)

    v2.mainloop()
    
    
def ventana3():
    v1.destroy()
    v3=tk.Tk()
    v3.title("707")
    v3.geometry("400x300")
    v3.config(bg="#ECC1FF")

    etq3=tk.Label(v3,text="IF I OLNY COULD",font=("Comic Sans MS",14),fg="black", bg="#ECC1FF")
    etq3.pack()

    boton3=tk.Button(v3,text="Volver",font=("Comic Sans MS",12), bg="#8974A7",command=lambda:destruir(v3))
    boton3.pack(pady=20)

    v3.mainloop()
    
def ventana4():
    v1.destroy()
    v4=tk.Tk()
    v4.title("707")
    v4.geometry("400x300")
    v4.config(bg="#ECC1FF")

    etq4=tk.Label(v4,text="MAKE A DEAL WITH GOD",font=("Comic Sans MS",14),fg="black", bg="#ECC1FF")
    etq4.pack()

    boton4=tk.Button(v4,text="Volver",font=("Comic Sans MS",12), bg="#8974A7",command=lambda:destruir(v4))
    boton4.pack(pady=20)

    v4.mainloop()
    
def ventana5():
    v1.destroy()
    v5=tk.Tk()
    v5.title("707")
    v5.geometry("400x300")
    v5.config(bg="#ECC1FF")

    etq5=tk.Label(v5,text="MD",font=("Comic Sans MS",14),fg="black", bg="#ECC1FF")
    etq5.pack()

    boton5=tk.Button(v5,text="Volver",font=("Comic Sans MS",12), bg="#8974A7",command=lambda:destruir(v5))
    boton5.pack(pady=20)

    v5.mainloop()
    
ventana()