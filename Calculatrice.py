import math
from tkinter import *


calcul = ""

def nb(nombre):                               # fonction pour le stockage des nombre à calculer    
    global calcul
    calcul = calcul + str(nombre)
    operation.set(calcul)


def egal():                                   # fonction pour le calcul
    try:
        global calcul
        total = str(eval(calcul))
        operation.set(total)
        calcul = ""

    except:
        operation.set(" erreur ! ")
        calcul = ""



def supprimer():
    global calcul
    calcul = ""
    operation.set("")

fenetre = Tk()
def basetotxt(valeur):                   # fonction pour l'affichage du choix de la base dans les fenetre
    if valeur==2:
        return("binaire")
    if valeur == 8:
        return("Octal")
    if valeur==10:
        return("décimal")
    if valeur==16:
       return("héxadécimal")
    if valeur==3:
        return("binaire signé")
    if valeur==11:
        return("decimal négatif")
    if valeur==9:
        return("réel decimal")
    if valeur==1:
        return("réel binaire")
    

def binToDec(calcul_affichage):           # fontion de convertion du TP calculatrice programeur 
    nb_bin = calcul_affichage [::-1]      # reformuler pour le fonctionnement de certaine fonction
    nb_dec=0
    for i in range(len(nb_bin)):
        nb_dec += int(nb_bin[i]) * 2**i 
    return str(nb_dec)

def decToBin(calcul_affichage):
    nb_bin =""
    nb_dec = int(calcul_affichage)
    while nb_dec != 0:
        nb_bin += str(nb_dec % 2)
        nb_dec //=2 
    nb_bin = nb_bin[::-1]
    return nb_bin
    

def binToHex(calcul_affichage) :
    dictionnaire = {"0000":"0", "0001":"1", "0010":"2", "0011":"3","0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"C", "1110":"E", "1111":"F"}
    resultat = ""
    while len(calcul_affichage)%4 != 0 :
        calcul_affichage = "0"+calcul_affichage
    longueur = int(len(calcul_affichage)/4)
    for i in range (longueur):
        octet = calcul_affichage[4*i:4*i+4]
        resultat = resultat + dictionnaire [octet]
    return resultat

def hexToBin(calcul_affichage) :
    dictionnaire = {"0":"0000", "1":"0001", "2":"0010", "3":"0011","4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
    resultat = ""
    for i in range (len(calcul_affichage)):
        octet = calcul_affichage [i]
        resultat = resultat + dictionnaire [octet]
    return resultat

def decToHex(calcul_affichage) :
    nb_bin = decToBin(calcul_affichage)
    resultat = binToHex(nb_bin)
    return resultat

def hexToDec(calcul_affichage) :
    dictionnaire = {"0":"0", "1":"1", "2":"2", "3":"3","4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15"}
    resultat = 0
    nb_hex = calcul_affichage[::-1]
    for i in range (len(nb_hex)):
        resultat = resultat + int(dictionnaire[nb_hex[i]])*16**i
    return resultat

def binToOct(calcul_affichage) :
    dictionnaire = {"000":"0", "001":"1", "010":"2", "011":"3","100":"4", "101":"5", "110":"6", "111":"7"}
    resultat = ""
    while len(calcul_affichage)%3 != 0 :
        calcul_affichage = "0"+calcul_affichage
    longueur = int(len(calcul_affichage)/3)
    for i in range (longueur):
        octet = calcul_affichage[3*i:3*i+3]
        resultat = resultat + dictionnaire [octet]
    return resultat

def octToBin(calcul_affichage) :
    dictionnaire = {"0":"000", "1":"001", "2":"010", "3":"011","4":"100", "5":"101", "6":"110", "7":"111"}
    resultat = ""
    for i in range (len(calcul_affichage)):
        octet = calcul_affichage [i]
        resultat = resultat + dictionnaire [octet]
    return resultat

def decToOct(calcul_affichage) :
    nb_bin = decToBin(calcul_affichage)
    resultat = binToOct(nb_bin)
    return resultat

def hexToOct(calcul_affichage) :
    nb_bin = hexToBin(calcul_affichage)
    resultat = binToOct(nb_bin)
    return resultat

def octToDec(calcul_affichage) :
    nb_bin = octToBin(calcul_affichage)
    resultat = binToDec(nb_bin)
    return resultat

def octToHex(calcul_affichage) :
    nb_bin = octToBin(calcul_affichage)
    resultat = binToHex(nb_bin)
    return resultat

def decNegToBin(calcul_affichage) :              
    resultat = int(calcul_affichage,10)*(-1)
    resultat = decToBin(resultat)
    for i in range (0,8-len(resultat)) : 
        resultat = "0"+resultat
    inverse = ""
    for i in resultat :
        if i == "0" :
            inverse = inverse + "1"
        else : 
            inverse = inverse + "0"
    resultat = decToBin(int(inverse,2) + 1)  
    return resultat 

def binNegToDec(calcul_affichage) :
    if len (calcul_affichage)<8 or calcul_affichage[0]=="0" :
        resultat = binToDec(calcul_affichage)
        return resultat
    elif len (calcul_affichage)>8:
        return "overflow"
    else : 
        inverse = ""
        for i in calcul_affichage :
            if i == "0" :
                inverse = inverse + "1"
            else : 
                inverse = inverse + "0"
        resultat = -1*(int(inverse,2) + 1)
        return resultat

def decReelToBin(calcul_affichage) :
    entier,decimal = (calcul_affichage).split(".")
    entier = decToBin(int(entier,10))
    decimal = float("0."+decimal)
    resultat = ""
    for i in range (0,15) :
        decimal = decimal*2
        resultat = resultat + str(decimal)[0]
        decimal = decimal-math.floor (decimal) 
    resultat = entier + "." + resultat
    return resultat

# def decReelToBin_IEEE754(calcul_affichage):

def binReelToDec(calcul_affichage) :
    entier,decimal = (calcul_affichage).split(".")
    entier = binToDec(entier)
    resultat = 0
    for i in range (0,len(decimal)):
        if decimal[i]=="1" :
            resultat = resultat + 2**-(i+1)
    decimal=resultat
    resultat = int(entier) + float(decimal)
    return resultat


def chx_conv(psource, pdest, pdest2, pdest3, ptype):
    if ptype=="positif":
        affichageconvpositif(psource, pdest, pdest2, pdest3)
    if ptype=="signe":
        affichageconvsigne(psource,pdest)
    if ptype=="reel":
        affichageconvreel(psource,pdest)





def affichageconvpositif(source, dest, dest2, dest3):      # fenêtre pour la convertion de nombre positif
    s = basetotxt(source)
    d = basetotxt(dest)
    d2 = basetotxt(dest2)
    d3 = basetotxt(dest3)
    
    fenetre2 = Tk()
    fenetre2.title("Nombre "+s+" -> ... (Entiers)")
    fenetre2.config(bg="#87CEEB")
    fenetre2.maxsize(400, 200)
    fenetre2.minsize(400, 200)
    
    texte = Label(fenetre2, text="Entrez votre nombre "+ s+" puis appuyer sur entrée", bg="yellow")
    texte.pack()
       
    def convertion(event):
        afficher.configure(text = "Nombre "+s+" "+str(nb_ent.get()))

        if source ==2:                              # en fonction de la base de départ (source) fait les convertions des les autres bases
            resultat1 = binToDec(nb_ent.get())
            resultat2 = binToHex(nb_ent.get())
            resultat3 = binToOct(nb_ent.get())
        
        if source==8:
            resultat1 = octToBin(nb_ent.get())
            resultat2 = octToDec(nb_ent.get())
            resultat3 = octToHex(nb_ent.get())
            
        if source==10:
            resultat1 = decToBin(nb_ent.get())
            resultat2 = decToHex(nb_ent.get())
            resultat3 = decToOct(nb_ent.get())
            
        if source==16:
            resultat1 = hexToBin(nb_ent.get())
            resultat2 = hexToDec(nb_ent.get())
            resultat3 = hexToOct(nb_ent.get())

        afficherr.configure(text = "Nombre "+d+" "+str(resultat1))
        afficherr2.configure(text = "Nombre "+d2+" "+str(resultat2))
        afficherr3.configure(text = "Nombre "+d3+" "+str(resultat3))

    nb_ent = Entry(fenetre2)
    nb_ent.bind("<Return>", convertion)
    afficher = Label(fenetre2, text = ".....")
    afficherr= Label(fenetre2,text=".....")
    afficherr2= Label(fenetre2,text=".....")
    afficherr3= Label(fenetre2,text=".....")
    nb_ent.pack() 
    afficher.pack() 
    afficherr.pack()
    afficherr2.pack()
    afficherr3.pack()

    retour=Button(fenetre2,text="Retour",command= fenetre2.destroy, background='#ff9999')
    retour.pack(side=RIGHT,padx=20,pady=10)
    quitterb=Button(fenetre2,text="Quitter",command = quitter, background='#ff0033')
    quitterb.pack(side=LEFT,padx=20,pady=10)



def affichageconvsigne(source,dest):            # fenêtre pour la convertion de nombre signé
    s = basetotxt(source)
    d = basetotxt(dest)
    fenetre3 = Tk()
    fenetre3.title("Nombre "+s+" -> Nombre "+d)
    fenetre3.config(bg="#87CEEB")
    fenetre3.maxsize(400,150)
    fenetre3.minsize(400,150)
    
    texte = Label(fenetre3, text="Entrez votre nombre "+ s+" puis appuyer sur entrée", bg="yellow")
    texte.pack()
       
    def convertion(event):
        afficher.configure(text = "Nombre "+s+" "+str(calcul_affichage.get()))
        if dest==3:
            resultat = decNegToBin(calcul_affichage.get())
        if dest==11:
            resultat = binNegToDec(calcul_affichage.get())
        afficherr.configure(text = "Nombre "+d+" "+str(resultat)) 

    calcul_affichage = Entry(fenetre3)
    calcul_affichage.bind("<Return>", convertion)
    afficher = Label(fenetre3, text = ".....") 
    afficherr= Label(fenetre3,text=".....")
    calcul_affichage.pack() 
    afficher.pack() 
    afficherr.pack()

    retour=Button(fenetre3,text="Retour",command= fenetre3.destroy, background='#ff9999')
    retour.pack(side=RIGHT,padx=20,pady=10)
    quitterb=Button(fenetre3,text="Quitter",command = quitter, background='#ff0033')
    quitterb.pack(side=LEFT,padx=20,pady=10)

    fenetre3.mainloop()

def affichageconvreel(source,dest):                 # fenêtre pour la convertion de nombre réel
    s = basetotxt(source)
    d = basetotxt(dest)
    fenetre4 = Tk()
    fenetre4.title("Nombre "+s+" -> Nombre "+d)
    fenetre4.config(bg="#87CEEB")
    fenetre4.maxsize(400,150)
    fenetre4.minsize(400,150)
    
    texte = Label(fenetre4, text="Entrez votre nombre "+ s+" puis appuyer sur entrée", bg="yellow")
    texte.pack()
       
    def convertion(event):
        afficher.configure(text = "Nombre "+s+" "+str(calcul_affichage.get()))
        if dest==1:
            resultat = decReelToBin(calcul_affichage.get())
        if dest==9:
            resultat = binReelToDec(calcul_affichage.get())
        afficherr.configure(text = "Nombre "+d+" "+str(resultat)) 

    calcul_affichage = Entry(fenetre4)
    calcul_affichage.bind("<Return>", convertion)
    afficher = Label(fenetre4, text = ".....") 
    afficherr= Label(fenetre4,text=".....")
    calcul_affichage.pack() 
    afficher.pack() 
    afficherr.pack()

    retour=Button(fenetre4,text="Retour",command= fenetre4.destroy, background='#ff9999')
    retour.pack(side=RIGHT,padx=20,pady=10)
    quitterb=Button(fenetre4,text="Quitter",command = quitter, background='#ff0033')
    quitterb.pack(side=LEFT,padx=20,pady=10)

    fenetre4.mainloop()

def quitter():                              # configuration de la fonction pour fermer les fenêtre de la calculatrice
    quitter1=Tk()
    quitter1.config(bg="#87CEEB")
    quitter1.maxsize(210,100)
    quitter1.minsize(210,100)
    quitter1.title("Quitter")
    question = Label(quitter1, text="Voulez vous quitter ?", bg="yellow")
    question.pack()
    oui=Button(quitter1,text="Oui", command = quit, background='#ff0033')
    non=Button(quitter1,text="Non",command= quitter1.destroy, background='#99cc66')
    oui.pack(side=LEFT,padx=20)
    non.pack(side=RIGHT,padx=20 )
    quitter1.mainloop 

def Menu():                                 # configuration de la fenêtre Menu
    Menu1=Tk()
    Menu1.config(bg="#87CEEB")
    Menu1.maxsize(450,210)
    Menu1.minsize(450,210)
    Menu1.title("Menu")
    texte = Label(Menu1, text="Choisissez votre fonction de convertion", bg="yellow")
    bouton1=Button(Menu1,text="Binaire -> ... (Entiers)", command=lambda: chx_conv(2,10,16,8,"positif"), background='#99cc66')        # bouton relié au fonction de convertion par l'envoi dans la fonction chx_conv de la source, de la destination et du signe
    bouton2=Button(Menu1,text="Decimal -> ... (Entiers)", command=lambda: chx_conv(10,2,16,8,"positif"), background='#99cc66')
    bouton3=Button(Menu1,text="Hexadecimal -> ... (Entiers)", command=lambda: chx_conv(16,2,10,8,"positif"), background='#99cc66')
    bouton8=Button(Menu1,text="Octal -> ... (Entiers)", command=lambda: chx_conv(8,2,10,16,"positif"), background='#99cc66')
    bouton4=Button(Menu1,text="Decimal négatif -> Binaire signé", command=lambda: chx_conv(11, 3, 0, 0, "signe"), background='#99cc66')
    bouton5=Button(Menu1,text="Binaire signé -> Decimal", command=lambda: chx_conv(3, 11, 0, 0, "signe"), background='#99cc66')
    bouton6=Button(Menu1,text="Réel décimal -> Réel binaire", command=lambda: chx_conv(9, 1, 0, 0, "reel"), background='#99cc66')
    bouton7=Button(Menu1,text="Réel binaire -> Réel décimal", command=lambda: chx_conv(1, 9, 0, 0, "reel"), background='#99cc66')
    bouton_quitter=Button(Menu1,text="Quitter",command = quitter, background='#ff0033')
    retour=Button(Menu1,text="Retour",command= Menu1.destroy, background='#ff9999')
    
    
    texte.pack()
    bouton1.place(x=18, y=30)
    bouton2.place(x=145, y=30)
    bouton3.place(x=278, y=30)
    bouton4.place(x=62, y=100)
    bouton5.place(x=247, y=100)
    bouton6.place(x=65, y=135)
    bouton7.place(x=228, y=135)
    bouton8.place(x=170, y=65)
    bouton_quitter.place(x=175, y=170)
    retour.place(x=230, y=170)
    Menu1.mainloop 


fenetre.title("Calculatrice")              # configuration de la fenêtre d'accueil, calculatrice
fenetre.config(bg="#87CEEB")
fenetre.maxsize(360,470)
fenetre.minsize(360,470)

canvas = Canvas(fenetre, width=330, height=150, background='#cccccc')
operation = StringVar()

calcul_affichage = Entry(fenetre, textvariable=operation)
bouton_Menu=Button(fenetre,text="Menu", width=6, height=3, command = Menu, background='#cc6600')
bouton_c0=Button(fenetre,text="0", width=6, height=3, command=lambda: nb(0), background='#fedb00')  # bouton pour les chiffre ou opérateur de calcul de la calculatrice envoi le clique dans la fonction de calcul nb
bouton_v=Button(fenetre,text=",", width=6, height=3, command=lambda: nb("."), background='#fedb00')
bouton_egal=Button(fenetre,text="=", width=15, height=3, command=egal, background='#ffccff')
bouton_c1=Button(fenetre,text="1", width=6, height=3, command=lambda: nb(1), background='#fedb00')
bouton_c2=Button(fenetre,text="2", width=6, height=3, command=lambda: nb(2), background='#fedb00')
bouton_c3=Button(fenetre,text="3", width=6, height=3, command=lambda: nb(3), background='#fedb00')
bouton_plus=Button(fenetre,text="+", width=6, height=3, command=lambda: nb("+"), background='#99cc66')
bouton_moins=Button(fenetre,text="-", width=6, height=3, command=lambda: nb("-"), background='#99cc66')
bouton_c4=Button(fenetre,text="4", width=6, height=3, command=lambda: nb(4), background='#fedb00')
bouton_c5=Button(fenetre,text="5", width=6, height=3, command=lambda: nb(5), background='#fedb00')
bouton_c6=Button(fenetre,text="6", width=6, height=3, command=lambda: nb(6), background='#fedb00')
bouton_multiplier=Button(fenetre,text="*", width=6, height=3, command=lambda: nb("*"), background='#99cc66')
bouton_diviser=Button(fenetre,text="/", width=6, height=3, command=lambda: nb("/"), background='#99cc66')
bouton_c7=Button(fenetre,text="7", width=6, height=3, command=lambda: nb(7), background='#fedb00')
bouton_c8=Button(fenetre,text="8", width=6, height=3, command=lambda: nb(8), background='#fedb00')
bouton_c9=Button(fenetre,text="9", width=6, height=3, command=lambda: nb(9), background='#fedb00')
bouton_quitter=Button(fenetre,text="Quitter", width=6, height=3, command = quitter, background='#ff0033')
bouton_AC= Button(fenetre,text="AC", width=6, height=3, command = supprimer, background='#ffcc99')



canvas.pack()                                   # placement des différents éléments sur la fenêtre
calcul_affichage.place(x=115, y=60)
bouton_Menu.place(x=220, y=180)
bouton_quitter.place(x=285, y=180)
bouton_c0.place(x=25, y=390)
bouton_v.place(x=90, y=390)
bouton_egal.place(x=220, y=390)
bouton_c1.place(x=25, y=320)
bouton_c2.place(x=90, y=320)
bouton_c3.place(x=155, y=320)
bouton_plus.place(x=220, y=320)
bouton_moins.place(x=285, y=320)
bouton_c4.place(x=25, y=250)
bouton_c5.place(x=90, y=250)
bouton_c6.place(x=155, y=250)
bouton_multiplier.place(x=220, y=250)
bouton_diviser.place(x=285, y=250)
bouton_c7.place(x=25, y=180)
bouton_c8.place(x=90, y=180)
bouton_c9.place(x=155, y=180)
bouton_AC.place(x=155, y=390)


fenetre.mainloop()