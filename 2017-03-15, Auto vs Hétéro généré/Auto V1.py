#ATTENTION !!!!! Vérifiez le Temps pour chaque clic (475 sains/7253 DFT)

import tkinter
from tkinter import *
import winsound
from winsound import *
import math
from timeit import time
import random
import os

nom = input("Nom sujet :")
os.mkdir('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{}'.format(nom))
##########################################DEBUT AUTO-GENERE##############################################################################################################################
class auto(tkinter.Tk):
    def __init__(self,parent):
        self.racine0=tkinter.Tk()
        self.racine0.attributes('-fullscreen',True)
        self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
        self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
        self.fond0.pack(fill='both')

        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        print('\nDébut auto-généré\n')    
        f.write("\Auto Généré\n\n")
        self.reaction=[]
        self.combinaison=[]

        f.write('[Coord Cercle 1[')
        f.write('Coord Cercle 2[')
        f.write('Coord Cercle 3[')
        f.write('Coord Cercle 4[')
        f.write('Coord Cercle 5[')
        f.write('Combi[')
        f.write('RT\n')

        self.NRauto=0
        self.NEauto=0
        self.NDauto=0
        self.gainauto=0
        self.combiauto=[]
        self.combauto=[]
        self.MCauto=0
        self.ACauto=0
        self.numclicauto=0

        self.premierclic=-5

        self.SRTauto=0
        self.RTmaxauto=0
        self.RTminauto=120

        self.MC=0
        self.AC=0
        self.PS=0
        self.veriftour=0

        self.lim=0

        self.hetero=1

        self.tempsminutes=2
        self.tempssecondes=0

        self.tempssecondeslimite=0

        self.progr=self.w-425
        self.pb = self.fond0.create_rectangle(self.w-425,(self.h/1.2),self.progr,(self.h/1.2)+30, fill='white', width='1')

        self.jauge = PhotoImage(file = 'C:\\Users\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
        self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)

        tkinter.Tk.__init__(self,parent)
        self.parent=parent

        self.coord0=[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135]
        self.coord1=[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45]
        self.coord2=[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225]
        self.coord3=[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45]
        self.coord4=[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45]
        self.coord5=[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45]
        self.coord6=[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45]
        self.coord7=[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135]
        self.coord8=[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135]
        self.coord9=[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225]
        self.coord10=[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225]
        self.coord11=[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135]
        self.coord12=[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135]
        self.coord13=[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225]
        self.coord14=[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]

        self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey80', width='5')
        self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey80', width='5')
        self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey80', width='5')
        self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey80', width='5')
        self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey80', width='5')
        self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey80', width='5')
        self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey80', width='5')
        self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey80', width='5')
        self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey80', width='5')
        self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey80', width='5')
        self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey80', width='5')
        self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey80', width='5')
        self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey80', width='5')
        self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey80', width='5')
        self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey80', width='5')

        self.ellipseclic0=self.fond0.create_oval(self.coord0, fill='grey80', width='5')
        self.ellipseclic1=self.fond0.create_oval(self.coord1, fill='grey80', width='5')
        self.ellipseclic2=self.fond0.create_oval(self.coord2, fill='grey80', width='5')
        self.ellipseclic3=self.fond0.create_oval(self.coord3, fill='grey80', width='5')
        self.ellipseclic4=self.fond0.create_oval(self.coord4, fill='grey80', width='5')
        self.ellipseclic5=self.fond0.create_oval(self.coord5, fill='grey80', width='5')
        self.ellipseclic6=self.fond0.create_oval(self.coord6, fill='grey80', width='5')
        self.ellipseclic7=self.fond0.create_oval(self.coord7, fill='grey80', width='5')
        self.ellipseclic8=self.fond0.create_oval(self.coord8, fill='grey80', width='5')
        self.ellipseclic9=self.fond0.create_oval(self.coord9, fill='grey80', width='5')
        self.ellipseclic10=self.fond0.create_oval(self.coord10, fill='grey80', width='5')
        self.ellipseclic11=self.fond0.create_oval(self.coord11, fill='grey80', width='5')
        self.ellipseclic12=self.fond0.create_oval(self.coord12, fill='grey80', width='5')
        self.ellipseclic13=self.fond0.create_oval(self.coord13, fill='grey80', width='5')
        self.ellipseclic14=self.fond0.create_oval(self.coord14, fill='grey80', width='5')

        self.ellipseblue1=self.fond0.create_oval(self.coord10, fill='grey80', width='5')
        self.ellipseblue2=self.fond0.create_oval(self.coord11, fill='grey80', width='5')
        self.ellipseblue3=self.fond0.create_oval(self.coord12, fill='grey80', width='5')
        self.ellipseblue4=self.fond0.create_oval(self.coord13, fill='grey80', width='5')

        self.attente()

    def attente(self):        
        self.startchrono()
        self.startlimite1()
        self.tapp=time.perf_counter()
        
        self.fond0.bind('<Button-1>',self.clicauto)

    def startlimite1(self):
        self.lancementsec=self.racine0.after(475,self.seclimite)#Temps pour chaque clic (475 sains/1253 DFT)
		
    def startlimite2(self):
        self.fond0.delete(self.racine0,self.pb)
        self.progr=self.progr-10.00
        self.pb = self.fond0.create_rectangle(self.w-425,(self.h/1.2),self.progr,(self.h/1.2)+30, fill='white', width='1')
        self.startlimite1()
		
    def seclimite(self):
        self.tempssecondeslimite=self.tempssecondeslimite+1
        if self.tempssecondeslimite==4:
            self.tempssecondeslimite=0
            self.startlimite2()
        else:
            self.startlimite1()
			
    def startchrono(self):
        if self.tempssecondes<10:
            self.chronosecondes=self.fond0.create_text(self.w/1.7,self.h/8,text="0{}".format(self.tempssecondes), font=('Arial 120 bold'),fill='black')
        else:
            self.chronosecondes=self.fond0.create_text(self.w/1.7,self.h/8,text="{}".format(self.tempssecondes), font=('Arial 120 bold'),fill='black')
            
        self.chronominutes=self.fond0.create_text(self.w/2.3,self.h/8,text="0{}:".format(self.tempsminutes), font=('Arial 120 bold'),fill='black')
        self.lancementsec2=self.racine0.after(1000,self.sec)
		
    def sec(self):
        if self.tempssecondes==0 and self.tempsminutes==0:
            self.tempssecondes=self.tempssecondes-1
            self.timeauto()
            
        elif self.tempssecondes==0:
            self.tempsminutes=self.tempsminutes-1
            self.tempssecondes=59
            if self.tempsminutes!=-1:
                self.fond0.delete(self.racine0,self.chronominutes)
                self.fond0.delete(self.racine0,self.chronosecondes)
                self.startchrono()
            elif self.tempsminutes==-1:
                self.fond0.delete(self.racine0,self.chronominutes)
                self.fond0.delete(self.racine0,self.chronosecondes)                      
        else:
            self.tempssecondes=self.tempssecondes-1
            self.fond0.delete(self.racine0,self.chronominutes)
            self.fond0.delete(self.racine0,self.chronosecondes)
            self.startchrono()

    def initializeauto(self):
        self.fond0.delete(self.racine0,self.ellipse0)
        self.fond0.delete(self.racine0,self.ellipse1)
        self.fond0.delete(self.racine0,self.ellipse2)
        self.fond0.delete(self.racine0,self.ellipse3)
        self.fond0.delete(self.racine0,self.ellipse4)
        self.fond0.delete(self.racine0,self.ellipse5)
        self.fond0.delete(self.racine0,self.ellipse6)
        self.fond0.delete(self.racine0,self.ellipse7)
        self.fond0.delete(self.racine0,self.ellipse8)
        self.fond0.delete(self.racine0,self.ellipse9)
        self.fond0.delete(self.racine0,self.ellipse10)
        self.fond0.delete(self.racine0,self.ellipse11)
        self.fond0.delete(self.racine0,self.ellipse12)
        self.fond0.delete(self.racine0,self.ellipse13)
        self.fond0.delete(self.racine0,self.ellipse14)

        self.fond0.delete(self.racine0,self.ellipseclic0)
        self.fond0.delete(self.racine0,self.ellipseclic1)
        self.fond0.delete(self.racine0,self.ellipseclic2)
        self.fond0.delete(self.racine0,self.ellipseclic3)
        self.fond0.delete(self.racine0,self.ellipseclic4)
        self.fond0.delete(self.racine0,self.ellipseclic5)
        self.fond0.delete(self.racine0,self.ellipseclic6)
        self.fond0.delete(self.racine0,self.ellipseclic7)
        self.fond0.delete(self.racine0,self.ellipseclic8)
        self.fond0.delete(self.racine0,self.ellipseclic9)
        self.fond0.delete(self.racine0,self.ellipseclic10)
        self.fond0.delete(self.racine0,self.ellipseclic11)
        self.fond0.delete(self.racine0,self.ellipseclic12)
        self.fond0.delete(self.racine0,self.ellipseclic13)
        self.fond0.delete(self.racine0,self.ellipseclic14)
        
        self.numclicauto=0
        self.combauto=[]
        
        self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey80', width='5')
        self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey80', width='5')
        self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey80', width='5')
        self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey80', width='5')
        self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey80', width='5')
        self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey80', width='5')
        self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey80', width='5')
        self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey80', width='5')
        self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey80', width='5')
        self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey80', width='5')
        self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey80', width='5')
        self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey80', width='5')
        self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey80', width='5')
        self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey80', width='5')
        self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey80', width='5')

        self.ellipseclic0=self.fond0.create_oval(self.coord0, fill='grey80', width='5')
        self.ellipseclic1=self.fond0.create_oval(self.coord1, fill='grey80', width='5')
        self.ellipseclic2=self.fond0.create_oval(self.coord2, fill='grey80', width='5')
        self.ellipseclic3=self.fond0.create_oval(self.coord3, fill='grey80', width='5')
        self.ellipseclic4=self.fond0.create_oval(self.coord4, fill='grey80', width='5')
        self.ellipseclic5=self.fond0.create_oval(self.coord5, fill='grey80', width='5')
        self.ellipseclic6=self.fond0.create_oval(self.coord6, fill='grey80', width='5')
        self.ellipseclic7=self.fond0.create_oval(self.coord7, fill='grey80', width='5')
        self.ellipseclic8=self.fond0.create_oval(self.coord8, fill='grey80', width='5')
        self.ellipseclic9=self.fond0.create_oval(self.coord9, fill='grey80', width='5')
        self.ellipseclic10=self.fond0.create_oval(self.coord10, fill='grey80', width='5')
        self.ellipseclic11=self.fond0.create_oval(self.coord11, fill='grey80', width='5')
        self.ellipseclic12=self.fond0.create_oval(self.coord12, fill='grey80', width='5')
        self.ellipseclic13=self.fond0.create_oval(self.coord13, fill='grey80', width='5')
        self.ellipseclic14=self.fond0.create_oval(self.coord14, fill='grey80', width='5')

        self.tapp=time.perf_counter()

        self.fond0.bind('<Button-1>',self.clicauto)        

    def clicauto(self,event):
        if self.premierclic==-5:
            self.tclic=time.perf_counter()
            self.premierclic=self.tclic-self.tapp
        self.clicx=event.x
        self.clicy=event.y
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        self.coordclicx=self.fond0.winfo_pointerx()
        self.coordclicy=self.fond0.winfo_pointery()
        print('clic x:{}'.format(self.coordclicx))
        print('clic y:{}'.format(self.coordclicy))
        if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
            self.clicnauto= self.coord0
            self.ellipseclic0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicnauto= self.coord1
            self.ellipseclic1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord2
            self.ellipseclic2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
            self.clicnauto= self.coord3
            self.ellipseclic3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
            self.clicnauto= self.coord4
            self.ellipseclic4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicnauto= self.coord5
            self.ellipseclic5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicnauto= self.coord6
            self.ellipseclic6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord7
            self.ellipseclic7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord8
            self.ellipseclic8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord9
            self.ellipseclic9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord10
            self.ellipseclic10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord11
            self.ellipseclic11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord12
            self.ellipseclic12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord13
            self.ellipseclic13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord14
            self.ellipseclic14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        else:
            self.acoteauto()

    def reussiteauto(self):
        self.combiauto.append(self.combauto)
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        
        print('RT sec={}\n'.format(self.RTauto))
        f.write('{}\n'.format(self.RTauto))
        self.SRTauto=self.SRTauto+self.RTauto


        if self.RTauto>3:
            f.write('[Trop lent[')
            print('NR={}'.format(self.NRauto))
        else:
            self.NRauto=self.NRauto+1
            f.write('[Nouvelle combi[')
            print('NR={}'.format(self.NRauto))

        if self.RTauto>self.RTmaxauto:
            self.RTmaxauto=self.RTauto
            if self.RTauto<self.RTminauto:
                self.RTminauto=self.RTauto
        elif self.RTauto<self.RTminauto:
            self.RTminauto=self.RTauto

        self.tempssecondeslimite=0
        self.racine0.after_cancel(self.lancementsec)
        self.startlimite1()
            
        self.initializeauto()

    def verifcercleauto(self,event):
        if self.clicnauto in self.combauto:
            self.after(100,self.memecercleauto)
        else:
            self.testcombiauto()

    def testcombiauto(self):
        self.combauto.append(self.clicnauto)
        self.combauto.sort()
        print('clicn={}'.format(self.clicnauto))
        self.numclicauto=self.numclicauto+1
        if self.numclicauto<4:
            self.fond0.bind('<Button-1>',self.clicauto)
        else:
            print('Combi:{}'.format(self.combauto))
            if self.combauto in self.combiauto:
                self.after(100,self.dejafaitauto)
            else:
                self.tclic=time.perf_counter()
                self.RTauto=self.tclic-self.tapp
                self.after(100,self.reussiteauto)
			
    def dejafaitauto(self):
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        self.NDauto=self.NDauto+1
        f.write('[Combi déjà faite\n')
        print('Déjà fait:{}\n'.format(self.NDauto))
        self.initializeauto()

    def acoteauto(self):
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        self.ACauto=self.ACauto+1
        f.write('[{}, '.format(self.coordclicx))
        f.write('{}'.format(self.coordclicy))
        if self.numclicauto==0:
            f.write('[[[[[A cote\n')
        elif self.numclicauto==1:
            f.write('[[[[A cote\n')
        elif self.numclicauto==2:
            f.write('[[[A cote\n')
        elif self.numclicauto==3:
            f.write('[[A cote\n')
        elif self.numclicauto==4:
            f.write('[A cote\n')
        print('A côté:{}\n'.format(self.ACauto))
        self.initializeauto()

    def memecercleauto(self):
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        self.MCauto=self.MCauto+1
        if self.numclicauto==0:
            f.write('[[[[[Meme cercle\n')
        elif self.numclicauto==1:
            f.write('[[[[Meme cercle\n')
        elif self.numclicauto==2:
            f.write('[[[Meme cercle\n')
        elif self.numclicauto==3:
            f.write('[[Meme cercle\n')
        elif self.numclicauto==4:
            f.write('[Meme cercle\n')
        print('clic sur un même cercle:{}\n'.format(self.MCauto))
        self.initializeauto()
		
    def timeauto(self):                
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        end=self.fond0.create_text(self.w/2,self.h/2,text='THE END', font='Arial 50')

        self.fond0.destroy()
        self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
        self.fond0.pack(fill='both')
        self.racine0.after_cancel(self.lancementsec)
        
        print('\nAUTO-GENERE')
        print('\n\nBonnes réponses:{}'.format(self.NRauto))
        f.write('Bonnes réponses=[ %.2f\n'%self.NRauto)
        print('Erreurs couleur:{}'.format(self.NEauto))
        f.write('Erreurs couleur:[ %.2f\n'%self.NEauto)
        print('Erreurs répétition:{}'.format(self.NDauto))
        f.write('Erreurs répétition:[ %.2f\n'%self.NDauto)
        print('Erreurs même cercle:{}'.format(self.MCauto))
        f.write('Erreurs même cercle:[ %.2f\n'%self.MCauto)
        self.totalauto=self.NRauto+self.NEauto+self.NDauto+self.MCauto
        if self.totalauto==0:
            self.tauxauto=0
            self.RTmoyauto=0
        else:
            self.tauxauto=self.NRauto/self.totalauto*100
            self.RTmoyauto=self.SRTauto/self.totalauto
        print('Taux de réussite= %.2f'%self.tauxauto)
        f.write('Taux de réussite=[ %.2f\n'%self.tauxauto)
        
        fin=self.fond0.create_text(self.w/4,self.h/4,text='FIN de cette tâche.', font='Arial 20')

        print('RTmoy sec= %.3f'%self.RTmoyauto)
        f.write('RTmoy sec=[ %.3f\n'%self.RTmoyauto)
        print('RTmax sec= %.3f'%self.RTmaxauto)
        f.write('RTmax sec=[ %.3f\n'%self.RTmaxauto)
        print('RTmin sec= %.3f'%self.RTminauto)
        f.write('RTmin sec=[ %.3f\n\n'%self.RTminauto)
        print('Temps avant 1er clic= %.3f'%self.premierclic)
        f.write('Temps avant 1er clic=[ %.3f\n\n'%self.premierclic)

        self.after(15000, self.fin)
        
    def fin(self, event):
        self.racine0.destroy()

ordre=1
ordretaches=[]
while ordre!=[]:
	if ordre==1:
		ordre=2
		print('AUTO\n')
		if __name__ == '__main__':
			app = auto(None)
			app.title('my application')
			app.destroy()
			app.mainloop()

