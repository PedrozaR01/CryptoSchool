# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#Método Caesar tkinter
#Team Bitch
#Irving Mancera
#Carlos Ceniceros
#Roberto Pedroza

from tkinter import *
from tkinter import messagebox as MessageBox
import numpy as np

#def txtenc():
 #   tencriptadol = []
  #  for letra in tplano.get():
   #     tencriptadol.append((chr((((int(ord(letra))-65)+int(clave.get()))%26)+65)))
    #    print(tencriptadol) 

def encriptar():
    #txtenc(tplano.get())
    #print(tencriptado)
    tencriptadol = []
    for letra in tplano.get().upper().replace(" ",""):
        tencriptadol.append(chr(((((int(ord(letra))-65)+int(clave.get()))%26)+65)))
        print(tencriptadol) 
        
    MessageBox.showinfo("Texto Encriptado", list(tencriptadol))
    print(list(tplano.get()))
    encricesa.set(tencriptadol)
    
def desencriptar():
    tencriptado2 = []
    for letra in tencriptado.get().upper().replace(" ",""):
        tencriptado2.append(chr(((((int(ord(letra))+65)-int(clave1.get()))%26)+65)))
        print(tencriptado2) 
        
    MessageBox.showinfo("Texto Desencriptado", list(tencriptado2))
    print(list(tencriptado.get()))
    descesar.set(tencriptado2)
def matriz():
    num_caracteres = len(tplano1.get())
    fila = (int(num_caracteres) / int(Columnas.get()) +0.9)
    matriz = []
    contador=1
    aux = 0
    for inicializar in range(int(fila)):
        matriz.append(["_"]*int(Columnas.get()))
    for i in range(int(fila)):
        for j in range(int(Columnas.get())):
            if aux<len(tplano1.get()):
                matriz[i][j] = tplano1.get()[aux]  
                aux+=1
    y=np.transpose(matriz) #El trans nos permite cambiar el orden y leerlo por columnas
    a="".join(map(str, y))
    MessageBox.showinfo("Cadena encriptada", a)
    MessageBox.showinfo("Matriz", matriz)
    print("La matriz es la siguiente:")
    for i in matriz:
        print(i)
    print(num_caracteres)
    
    
    
    
def vigen():
    texto = []
    clave = []
    texto = tplavigenere.get().upper().replace(" ","")
    clave = clavevigenere.get().upper().replace(" ","")
    encriptado=[]
    x=0
    for i in range (len(texto)):
        encriptado.append((chr((((((int(ord(texto[i]))-65)+(int(ord(clave[x])-65)))%26)+65)))))
        print(texto[i])
        print(clave[x])
        print("----------")
        x=x+1
        if x== len(clave):
            x=0
    print(texto)
    print(encriptado)
    MessageBox.showinfo("Texto Encriptado", list(encriptado))
    textovigenere.set(encriptado)

def desvigen():
    texto = []
    clave = []
    texto = destplavigenere.get().upper().replace(" ","")
    clave = desclavevigenere.get().upper().replace(" ","")
    encriptado=[]
    x=0
    for i in range (len(texto)):
        encriptado.append((chr((((((int(ord(texto[i]))-65)+(26-(int(ord(clave[x])-65)%26)))%26)+65)))))
        print(texto[i])
        print(clave[x])
        print("----------")
        x=x+1
        if x== len(clave):
            x=0
    print(texto)
    print(encriptado)
    MessageBox.showinfo("Texto Encriptado", list(encriptado))
    destextovigenere.set(encriptado)


def Poly(): 
    listita = []
    listita2=[]
    palabrita="" #sedeclara para pasar la listita a string
    for letra in tplanopoly.get().upper():
        listita.append(str((ord(letra)-65)//5))
        listita.append(str((ord(letra)-65)%5))
    print(listita)
    print(palabrita.join(listita))
    MessageBox.showinfo("Texto Encriptado", list(listita))
    textopoly.set(listita)

 
        


def despoly():
    listita = []
    listita2=[]
    palabrita="" #sedeclara para pasar la listita a string
    for letra in encriptadopoly.get().upper().replace(" ", ""):
        listita.append(letra)
        
    print(listita)
    print(palabrita.join(listita))
    
    desencriptadopoly.set(listita)

    for x in range(0,len(listita), 2):
        pos1= int(listita[x])
        pos2= int(listita[x+1])
        letraAS = (pos1 * 5) + pos2
        print(letraAS)
        letraF1 = letraAS + 65
        caracter = chr(letraF1)
        listita2.append(caracter)
        desencriptadopoly.set(listita2)
    

###########################################################
root = Tk()#raíz de la ventana
tplano = StringVar()
tplano1 = StringVar()
clave = StringVar()
tencriptado = StringVar()
clave1 = StringVar()
Columnas = IntVar()
encricesa=StringVar()
descesar=StringVar()
#fila = (int(num_caracteres) / int(Columnas.get()) +0.9)

#Vigenere
tplavigenere=StringVar()
clavevigenere=StringVar()
destplavigenere=StringVar()
desclavevigenere=StringVar()
textovigenere=StringVar()
textovigenere=StringVar()
destextovigenere=StringVar()
#




#Poly
tplanopoly=StringVar()
encriptadopoly=StringVar()
desencriptadopoly=StringVar()
textopoly=StringVar()
#


#############################################################3
#Boton
btnEncriptar = Button(root, text="Encriptar", command=encriptar)
btnEncriptar.grid(column = 0, row = 0, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto = Label(root, text = "Texto plano: ")
lblTexto.grid(column = 0, row = 1)

#Entry plano
entryPlano = Entry(root, textvariable = tplano)
entryPlano.grid(column = 1, row = 1)

#label clave
lblClave = Label(root, text="Clave: ")
lblClave.grid(column = 0, row = 2)

#entry clave
entryClave = Entry(root, textvariable = clave)
entryClave.grid(column = 1, row = 2)

#Label tencriptado
lblEncriptado = Label(root, text="Texto Encriptado: ")
lblEncriptado.grid(column = 0, row=3)

entryClave = Entry(root, textvariable = encricesa)
entryClave.grid(column = 1, row = 3)

##############################################################################
#Boton
btnDesencriptar = Button(root, text="Desencriptar", command=desencriptar)
btnDesencriptar.grid(column = 0, row = 4, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto1 = Label(root, text = "Texto encriptado: ")
lblTexto1.grid(column = 0, row = 5)

#Entry plano
entryEncriptado = Entry(root, textvariable = tencriptado)
entryEncriptado.grid(column = 1, row = 5)

#label clave
lblClave1 = Label(root, text="Clave: ")
lblClave1.grid(column = 0, row = 6)

#entry clave
entryClave1 = Entry(root, textvariable = clave1)
entryClave1.grid(column = 1, row = 6)

#Label tencriptado
lblDesencriptado = Label(root, text="Texto Desencriptado: ")
lblDesencriptado.grid(column = 0, row=7)

#entry clave
entryClave1 = Entry(root, textvariable = descesar)
entryClave1.grid(column = 1, row = 7)



############################################################################3#
#Boton
btnDesencriptar = Button(root, text="Encriptar Vigenere", command=vigen)
btnDesencriptar.grid(column = 0, row = 8, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto1 = Label(root, text = "Texto plano: ")
lblTexto1.grid(column = 0, row = 9)

#Entry plano
entryEncriptado = Entry(root, textvariable = tplavigenere)
entryEncriptado.grid(column = 1, row = 9)

#label clave
lblClave1 = Label(root, text="llave: ")
lblClave1.grid(column = 0, row = 10)

#entry clave
entryClave1 = Entry(root, textvariable = clavevigenere)
entryClave1.grid(column = 1, row = 10)
entryClave1 = Entry(root, textvariable = textovigenere)
entryClave1.grid(column = 2, row = 10)

#Label tencriptado
#lblDesencriptado = Label(root, text="Texto Desencriptado: ")
#lblDesencriptado.grid(column = 0, row=11)


#####################################################################3##

############################################################################3#
#Boton
btnDesencriptar = Button(root, text="desencriptar Vigenere", command=desvigen)
btnDesencriptar.grid(column = 0, row = 11, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto1 = Label(root, text = "Texto plano: ")
lblTexto1.grid(column = 0, row = 12)

#Entry plano
entryEncriptado = Entry(root, textvariable = destplavigenere)
entryEncriptado.grid(column = 1, row = 12)

#label clave
lblClave1 = Label(root, text="llave: ")
lblClave1.grid(column = 0, row = 13)

#entry clave
entryClave1 = Entry(root, textvariable = desclavevigenere)
entryClave1.grid(column = 1, row = 13)

entryClave1 = Entry(root, textvariable = destextovigenere)
entryClave1.grid(column = 2, row = 13)


#####################################################################3##


############################################################################3#
#Boton
btnDesencriptar = Button(root, text="Encriptar Scytale", command=matriz)
btnDesencriptar.grid(column = 0, row = 14, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto1 = Label(root, text = "Texto plano: ")
lblTexto1.grid(column = 0, row = 15)

#Entry plano
entryEncriptado = Entry(root, textvariable = tplano1)
entryEncriptado.grid(column = 1, row = 15)

#label clave
lblClave1 = Label(root, text="Número de columnas: ")
lblClave1.grid(column = 0, row = 16)

#entry clave
entryClave1 = Entry(root, textvariable = Columnas)
entryClave1.grid(column = 1, row = 16)

#Label tencriptado
#lblDesencriptado = Label(root, text="Texto Desencriptado: ")
#lblDesencriptado.grid(column = 0, row=11)


#####################################################################3##




############################################################################3#
#Boton
btnDesencriptar = Button(root, text="Encriptar Polybios", command=Poly)
btnDesencriptar.grid(column = 0, row = 20, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto1 = Label(root, text = "Texto plano: ")
lblTexto1.grid(column = 0, row = 21)

#Entry plano
entryEncriptado = Entry(root, textvariable = tplanopoly)
entryEncriptado.grid(column = 1, row = 21)

#Entry plano
entryEncriptado = Entry(root, textvariable = textopoly)
entryEncriptado.grid(column = 2, row = 21)


#####################################################################3##
#Boton
btnDesencriptar = Button(root, text="desencriptar Polybios", command=despoly)
btnDesencriptar.grid(column = 0, row = 22, padx=5, pady=5, columnspan=2)

#label tplano
lblTexto1 = Label(root, text = "Pon el valor numerico : ")
lblTexto1.grid(column = 0, row = 23)

#Entry plano
entryEncriptado = Entry(root, textvariable = encriptadopoly)
entryEncriptado.grid(column = 1, row = 23)

#label tplano
lblTexto1 = Label(root, text = "numeros xD: " )
lblTexto1.grid(column = 0, row = 24)

#Entry plano
entryEncriptado = Entry(root, textvariable = desencriptadopoly)
entryEncriptado.grid(column = 1, row = 24)
#Label tencriptado
#lblDesencriptado = Label(root, text="Texto Desencriptado: ")
#lblDesencriptado.grid(column = 0, row=11)


#####################################################################3##




#####################################################################3##



root.mainloop()