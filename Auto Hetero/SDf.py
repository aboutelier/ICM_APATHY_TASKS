import tkinter
from tkinter import *
import winsound
from winsound import *
import random
from timeit import time
import math
import os
from os.path import join as joinpath
from copy import deepcopy

IMAGE_PIECES = "C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm"
IMAGE_PIECES_2 = "C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm"
IMAGE_JAUGE = "C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm"

SON_CASH = "C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav"
SON_PIECES = "C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav"

DOSSIER = "C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets"

class SDf(tkinter.Tk):
    def __init__(self, nom, parent=None):
        self.racine0=tkinter.Tk()
        self.racine0.attributes('-fullscreen',True)
        self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
        self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
        self.fond0.pack(fill='both')

        self.pieces = PhotoImage(file=IMAGE_PIECES)
        self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

        self.filename = joinpath(DOSSIER, nom, "{}_SpatialeDifficileFaible.xls".format(nom))

        f = open(self.filename, "a")
        f.write("\nTACHE SPATIALE DIFFICILE FAIBLE GAIN\n\n")
        print('TACHE SPATIALE DIFFICILE FAIBLE GAIN')

        self.NR=0
        self.NE=0
        self.ND=0
        self.gain=0
        self.combi=[]
        self.MC=0
        self.AC=0

        self.temps=30

        self.SRT=0
        self.SRTdejafait=0
        self.RTmax=0
        self.RTmin=360

        self.progr = self.w - 925
        self.delta_progression = 2.50

        self.jauge = PhotoImage(file = IMAGE_JAUGE)
        self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)
        self.pb = self.fond0.create_rectangle(self.progr,(self.h/1.2),self.w-425,(self.h/1.2)+30, fill='white', width='1')

        tkinter.Tk.__init__(self,parent, nom)
        self.parent, nom=parent

        self.coords = [[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],
                       [(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],
                       [(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],
                       [(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],
                       [(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],
                       [(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],
                       [(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],
                       [(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],
                       [(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],
                       [(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],
                       [(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],
                       [(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],
                       [(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],
                       [(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],
                       [(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]

        self.ellipses = [
            self.fond0.create_oval(coordfill='grey80', width='5')
            for coord in self.coords]

        self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'ecran pour démarrer", font=('Arial 60 bold'),fill='green')
        self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-300,text='Faites des combinaisons de\n4 cercles gris', font='Arial 20',justify='center')

        self.fond0.bind('<Button-1>',self.attente)

    def attente(self,event):
        self.hasard()
        self.after(180000, self.time)
        self.after(150000, self.debutchrono)

    def debutchrono(self):
        f = open(self.filename, "a")
        print('\nPlus que 30 sec\n')
        f.write('\n30 sec\n')
        self.startchrono()
        
    def startchrono(self):
        self.chrono=self.fond0.create_text(self.w/2,self.h/8,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
        self.lancementsec=self.after(1000, self.sec)
        
    def sec(self):
        self.temps = self.temps-1
        if self.temps>0:
            self.fond0.delete(self.racine0,self.chrono)
            self.startchrono()
        else:
            self.fond0.delete(self.racine0,self.chrono)

    def hasard(self):
        coordcouleur = deepcopy(self.coords)
        
        self.nbred1=random.choice(coordcouleur)
        coordcouleur.remove(self.nbred1)
        print('Red 1:{}'.format(self.nbred1))
        
        self.nbblue1=random.choice(coordcouleur)
        coordcouleur.remove(self.nbblue1)
        print('Blue 1:{}\n'.format(self.nbblue1))
        
        self.nbred2=random.choice(coordcouleur)
        coordcouleur.remove(self.nbred2)
        print('Red 2:{}'.format(self.nbred2))
        
        self.nbblue2=random.choice(coordcouleur)
        coordcouleur.remove(self.nbblue2)
        print('Blue 2:{}\n'.format(self.nbblue2))
        
        self.nbblue3=random.choice(coordcouleur)
        coordcouleur.remove(self.nbblue3)
        print('Blue 3:{}\n'.format(self.nbblue3))

        f = open(self.filename, "a")
        
        f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
        f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
        f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
        f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
        f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))
        
        f.write("Coord Cercle 1,Coord Cercle 2,Coord Cercle 3,Coord Cercle 4,Combi,RT,Temps ecoule\n")

        self.colored_ellipses = [
            self.fond0.create_oval(self.nbred1, fill='red', width='5'),
            self.fond0.create_oval(self.nbblue1, fill='blue', width='5'),
            self.fond0.create_oval(self.nbred2, fill='red', width='5'),
            self.fond0.create_oval(self.nbblue2, fill='blue', width='5'),
            self.fond0.create_oval(self.nbblue3, fill='blue', width='5')
        ]
        
        self.initialize()

    def initialize(self):
        self.fond0.delete(self.racine0,self.start)

        for ellipse in self.ellipses + self.colored_ellipses:
            self.fond0.delete(self.racine0, ellipse)

        self.numclic=0
        self.comb=[]
        
        self.ellipses = [
            self.fond0.create_oval(coordfill='grey80', width='5')
            for coord in self.coords
        ]

        self.colored_ellipses = [
            self.fond0.create_oval(self.nbred1, fill='red', width='5'),
            self.fond0.create_oval(self.nbblue1, fill='blue', width='5'),
            self.fond0.create_oval(self.nbred2, fill='red', width='5'),
            self.fond0.create_oval(self.nbblue2, fill='blue', width='5'),
            self.fond0.create_oval(self.nbblue3, fill='blue', width='5')
        ]

        self.tapp=time.perf_counter()

        self.fond0.bind('<ButtonPress-1>',self.clic)         

    def clic(self,event):
        self.clicx=event.x
        self.clicy=event.y
        f = open(self.filename, "a")
        self.coordclicx=self.fond0.winfo_pointerx()
        self.coordclicy=self.fond0.winfo_pointery()
        print('clic x:{}'.format(self.coordclicx))
        print('clic y:{}'.format(self.coordclicy))
        if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
            self.clicn= self.coord0
            self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicn= self.coord1
            self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicn= self.coord2
            self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
            self.clicn= self.coord3
            self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
            self.clicn= self.coord4
            self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicn= self.coord5
            self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicn= self.coord6
            self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicn= self.coord7
            self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
            self.clicn= self.coord8
            self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicn= self.coord9
            self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicn= self.coord10
            self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicn= self.coord11
            self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicn= self.coord12
            self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
            self.clicn= self.coord13
            self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicn= self.coord14
            self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
            f = open(self.filename, "a")
            f.write('{}'.format(self.clicn))
            self.verifcercle()
        else:
            self.acote()

    def reussite(self):
        self.NR += 1

        self.combi.append(self.comb)
        f = open(self.filename, "a")
    
        f.write('[Nouvelle combi[')
        print('NR={}'.format(self.NR))

        self.gain += 0.10

        print('RT sec={}\n'.format(self.RT))
        f.write('{}\n'.format(self.RT))
        self.SRT += self.RT
        
        self.update_progression()
        
        if self.NR % 5 == 0:
            winsound.PlaySound(SON_PIECES,winsound.SND_FILENAME | SND_ASYNC)

        self.RTmax = max(self.RTmax, self.RT)
        self.RTmin = min(self.RTmin, self.RT)
            
        self.initialize()

    def update_progression(self):
        self.fond0.delete(self.racine0, self.pb)	
        self.progr += self.delta_progression
        self.pb = self.fond0.create_rectangle(self.progr, self.h / 1.2, self.w - 425, self.h / 1.2 + 30, fill='white', width='1')

    def verifcercle(self):
        if self.clicn in self.comb:
            self.after(100,self.memecercle)
        elif self.nbblue1[0]<=self.clicx<=self.nbblue1[2] and self.nbblue1[1]<=self.clicy<=self.nbblue1[3] or self.nbblue2[0]<=self.clicx<=self.nbblue2[2] and self.nbblue2[1]<=self.clicy<=self.nbblue2[3] or self.nbblue3[0]<=self.clicx<=self.nbblue3[2] and self.nbblue3[1]<=self.clicy<=self.nbblue3[3]:
            self.after(100,self.erreurbleu)
        elif self.nbred1[0]<=self.clicx<=self.nbred1[2] and self.nbred1[1]<=self.clicy<=self.nbred1[3] or self.nbred2[0]<=self.clicx<=self.nbred2[2] and self.nbred2[1]<=self.clicy<=self.nbred2[3]:
            self.after(100,self.erreurrouge)
        else:
            self.testcombi()

    def testcombi(self):
        self.comb.append(self.clicn)
        self.comb.sort()
        print('clicn={}'.format(self.clicn))
        self.numclic += 1

        if self.numclic < 4:
            self.fond0.bind('<Button-1>',self.clic)
        else:
            print('Combi:{}'.format(self.comb))
            if self.comb in self.combi:
                self.tclic = time.perf_counter()
                self.RTdejafait = self.tclic - self.tapp
                self.SRTdejafait += self.RTdejafait
                self.after(100,self.dejafait)
            else:
                self.tclic=time.perf_counter()
                self.RT=self.tclic-self.tapp
                self.after(100,self.reussite)
            
    def erreurbleu(self):
        f = open(self.filename, "a")
        print('Bleu touché!')
        self.NE += 1
        print('raté!NE={}\n'.format(self.NE))
        if self.numclic==0:
            f.write('[[[[Distracteur Bleu\n')
        elif self.numclic==1:
            f.write('[[[Distracteur Bleu\n')
        elif self.numclic==2:
            f.write('[[Distracteur Bleu\n')
        elif self.numclic==3:
            f.write('[Distracteur Bleu\n')
        self.initialize()

    def erreurrouge(self):
        f = open(self.filename, "a")
        print('Rouge touché!')
        self.NE += 1
        if self.numclic==0:
            f.write('[[[[Distracteur Rouge\n')
        elif self.numclic==1:
            f.write('[[[Distracteur Rouge\n')
        elif self.numclic==2:
            f.write('[[Distracteur Rouge\n')
        elif self.numclic==3:
            f.write('[Distracteur Rouge\n')
        print('raté!NE={}\n'.format(self.NE))
        self.initialize()

    def dejafait(self):
        f = open(self.filename, "a")
        self.ND += 1
        f.write('[Combi déjà faite[')
        print('Déjà fait:{}\n'.format(self.ND))
        print('RT deja fait sec={}\n'.format(self.RTdejafait))
        f.write('{}\n'.format(self.RTdejafait))
        self.initialize()

    def acote(self):
        f = open(self.filename, "a")
        self.AC += 1
        f.write('[{}, {}'.format(self.coordclicx, self.coordclicy))
        if self.numclic==0:
            f.write('[[[[A cote\n')
        elif self.numclic==1:
            f.write('[[[A cote\n')
        elif self.numclic==2:
            f.write('[[A cote\n')
        elif self.numclic==3:
            f.write('[A cote\n')
        print('A côté:{}\n'.format(self.AC))
        self.initialize()

    def memecercle(self):
        f = open(self.filename, "a")
        self.MC=self.MC+1
        if self.numclic==0:
            f.write('[[[[Meme cercle\n')
        elif self.numclic==1:
            f.write('[[[Meme cercle\n')
        elif self.numclic==2:
            f.write('[[Meme cercle\n')
        elif self.numclic==3:
            f.write('[Meme cercle\n')
        print('clic sur un même cercle:{}\n'.format(self.MC))
        self.initialize()

    def time(self):
        self.racine0.after_cancel(self.lancementsec)                
        
        self.fond0.destroy()
        self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
        self.fond0.pack(fill='both')
        
        print('THE END\n')
        end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')

        self.NET=self.NE+self.ND+self.MC+self.AC
        self.total=self.NR+self.NET

        print('\n\nBonnes reponses:{}'.format(self.NR))
        print('Erreurs couleur:{}'.format(self.NE))
        print('Erreurs repetition:{}'.format(self.ND))
        print('Erreurs même cercle:{}'.format(self.MC))
        print('Erreurs à cote:{}'.format(self.AC))
        print('Erreurs totales:{}'.format(self.NET))
        print('Nombre de reponses:{}'.format(self.total))

        if self.total==0:
            self.taux=0
            self.RTmoyreussi=180
            self.RTmoydejafait=0
            self.RTmoytot=180
        else:
            self.taux=self.NR/self.total*100
            if self.taux==0:
                self.RTmoyreussi=0
            else:
                self.RTmoyreussi=self.SRT/self.NR
                
            if self.ND==0:
                self.RTmoydejafait=0
                self.RTmoytot=self.RTmoyreussi
            else:
                self.RTmoydejafait=self.SRTdejafait/self.ND
                self.RTmoytot=(self.SRT+self.SRTdejafait)/(self.ND+self.NR)

        print('Taux de réussite= %.2f'%self.taux)
        #gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu', font='Arial 50', justify='center')
        print('RTmoy reussi sec= %.3f'%self.RTmoyreussi)
        print('RTmoy deja fait sec= %.3f'%self.RTmoydejafait)
        print('RTmoy tot sec= %.3f'%self.RTmoytot)
        print('RTmax sec= %.3f'%self.RTmax)
        print('RTmin sec= %.3f'%self.RTmin)

        with open(self.filename, "a") as f:
            f.write('\n\nBonnes reponses: %.2f\n'%self.NR)
            f.write('Erreurs couleur: %.2f\n'%self.NE)
            f.write('Erreurs repetition: %.2f\n'%self.ND)
            f.write('Erreurs même cercle: %.2f\n'%self.MC)
            f.write('Erreurs à côte: %.2f\n'%self.AC)
            f.write('Erreurs totales: {}\n'.format(self.NET))
            f.write('Nombre de reponses: {}\n'.format(self.total))
            f.write('Taux de reussite: %.2f\n'%self.taux)
            f.write('RTmoy reussi (sec): %.3f\n'%self.RTmoyreussi)
            f.write('RTmoy deja fait (sec): %.3f\n'%self.RTmoydejafait)
            f.write('RTmoy tot (sec): %.3f\n'%self.RTmoytot)
            f.write('RTmax (sec): %.3f\n'%self.RTmax)
            f.write('RTmin (sec): %.3f\n\n'%self.RTmin)

        self.after(15000,self.fin)
        
    def fin(self):
        self.racine0.destroy()


if __name__ == "__main__":
    nom = input("Nom sujet :")
    maindir = joinpath(DOSSIER, nom)
    os.mkdir(maindir)

    app = SDf(nom, None)
    app.title('My application')
    app.destroy()
    app.mainloop()