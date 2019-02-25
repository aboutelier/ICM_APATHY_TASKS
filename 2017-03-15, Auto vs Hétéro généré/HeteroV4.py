#ATTENTION !!!!! Vérifiez le Temps pour chaque clic (810 sains/1370 DFT)

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
##########################################DEBUT HETERO-GENERE##############################################################################################################################
class hetero(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.imagepieces=self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		f.write("\nHétéro Généré Forte Perte\n\n")
		self.reaction=[]
		self.combinaison=[]

		self.NR=0
		self.CG=0
		self.CPT=0
		self.RTT=0
		self.gain=0
		self.comb=[]
		self.combi=[]
		self.MC=0
		self.AC=0
		self.PS=0
		self.veriftour=0

		self.premierclic=-5

		self.demarrage=0
		self.tempsmetronome=0

		self.lim=0

		self.hetero=1

		self.tempsminutes=2
		self.tempssecondes=0

		self.tempssecondeslimite=0

		self.SRT=0
		self.RTmax=0
		self.RTmin=120

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

		self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
		self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-300,text='Faites des combinaisons de 4 cercles\nen sélectionnant le cercle bleu', font='Arial 20',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasardbleu1()
		self.startchrono()
		self.startlimite1()
		self.lancementmetronome()

	def lancementmetronome(self):
		self.racine0.after(760, self.metronome)#Temps pour chaque clic (760 sains/1320 DFT)
		
	def metronome(self):                
		winsound.PlaySound('C:\\Users\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Metronome.wav',winsound.SND_FILENAME | SND_ASYNC)
		self.lancementmetronome()

	def startlimite1(self):
		self.lancementsec=self.racine0.after(810, self.seclimite)#Temps pour chaque clic + 50ms (810 sains/1370 DFT)
		
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
		self.lancementsec2=self.racine0.after(1000, self.sec)
		
	def sec(self):
		if self.tempssecondes==0 and self.tempsminutes==0 and self.hetero==1:
			self.tempssecondes=self.tempssecondes-1
			self.time()

		elif self.tempssecondes==0 and self.tempsminutes==0:
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
                
	def hasardbleu1(self):
		self.fond0.delete(self.racine0,self.start)
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

		self.fond0.delete(self.racine0,self.ellipseblue1)
		self.fond0.delete(self.racine0,self.ellipseblue2)
		self.fond0.delete(self.racine0,self.ellipseblue3)
		self.fond0.delete(self.racine0,self.ellipseblue4)


		self.numclic=0
		self.comb=[]

		self.tourverif=0
		
		self.numberblue1=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]

		self.nbblue1=random.choice(self.numberblue1)
		self.numberblue1.remove(self.nbblue1)

		self.nbblue2=random.choice(self.numberblue1)
		self.numberblue1.remove(self.nbblue2)

		self.nbblue3=random.choice(self.numberblue1)
		self.numberblue1.remove(self.nbblue3)

		self.nbblue4=random.choice(self.numberblue1)

		self.verifbleu4()

	def initialize(self):
		print('Blue 1:{}'.format(self.nbblue1))
		print('Blue 2:{}'.format(self.nbblue2))
		print('Blue 3:{}'.format(self.nbblue3))
		print('Blue 4:{}'.format(self.nbblue4))
		
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

		self.ellipseblue1=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		
		self.tapp=time.perf_counter()

		self.fond0.bind('<Button-1>',self.clic1)
		
	def clic1(self,event):
		if self.premierclic==-5:
			self.tclic=time.perf_counter()
			self.premierclic=self.tclic-self.tapp
		self.clicx=event.x
		self.clicy=event.y
		coordclicx=self.fond0.winfo_pointerx()
		coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(coordclicx))
		print('clic y:{}'.format(coordclicy))

		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipseclic0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipseclic1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipseclic2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipseclic3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipseclic4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipseclic5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipseclic6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipseclic7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipseclic8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipseclic9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipseclic10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipseclic11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipseclic12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipseclic13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipseclic14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			self.fond0.bind('<ButtonRelease-1>',self.verifclicbleu)
		else:
			self.fond0.bind('<ButtonRelease-1>',self.acote)
                        
	def reussite(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		
		print('RT={}\n'.format(self.RT))
		self.reaction.append(self.RT)
		self.SRT=self.SRT+self.RT

		self.NR=self.NR+1
		print('Réussies={}'.format(self.NR))
		self.combinaison.append('Nouvelle')

		self.lim=0

		if self.RT>self.RTmax:
			self.RTmax=self.RT
			if self.RT<self.RTmin:
				self.RTmin=self.RT
		elif self.RT<self.RTmin:
			self.RTmin=self.RT
			
		self.hasardbleu1()

		self.tempssecondeslimite=0
		self.racine0.after_cancel(self.lancementsec)
		self.startlimite1()
		
	def verifbleu3(self):
		if self.nbblue3==self.nbblue1 or self.nbblue3==self.nbblue2:
			self.coordpossibles.remove(self.nbblue3)
			self.veriftour=self.veriftour+1
			self.hasardbleu3()
		else:
			self.veriftour=0
			self.hasardbleu4()

	def verifbleu4(self):
		if self.nbblue4==self.nbblue1 or self.nbblue4==self.nbblue2 or self.nbblue4==self.nbblue3:
			self.coordpossibles.remove(self.nbblue4)
			self.veriftour=self.veriftour+1
			self.hasardbleu4()
		else:
			self.veriftour=0
			self.initialize()
	def verifclicbleu(self,event):
		if self.numclic==0:
			if self.clicn==self.nbblue1:
				self.comb.append(self.clicn)
				print('clicn={}'.format(self.clicn))
				self.numclic=self.numclic+1
				self.ellipseblue2=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
				self.fond0.bind('<Button-1>',self.clic1)
			else:
				self.after(100,self.erreur)
		elif self.numclic==1:
			if self.clicn==self.nbblue2:
				self.comb.append(self.clicn)
				print('clicn={}'.format(self.clicn))
				self.numclic=self.numclic+1
				self.ellipseblue3=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')
				self.fond0.bind('<Button-1>',self.clic1)
			else:
				self.after(100,self.erreur)
		elif self.numclic==2:
			if self.clicn==self.nbblue3:
				self.comb.append(self.clicn)
				print('clicn={}'.format(self.clicn))
				self.numclic=self.numclic+1
				self.ellipseblue4=self.fond0.create_oval(self.nbblue4, fill='blue', width='5')
				self.fond0.bind('<Button-1>',self.clic1)
			else:
				self.after(100,self.erreur)
		elif self.numclic==3:
			if self.clicn==self.nbblue4:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			else:
				self.erreur()

	def erreur(self):
		if self.clicn in self.comb:
			self.memecercle()
		else:
			self.erreurgris()

	def acote(self,event):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		self.AC=self.AC+1
		print('A côté:{}\n'.format(self.AC))
		self.combinaison.append('A côté')
		self.reaction.append('X')
		self.hasardbleu1()

	def erreurgris(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a") 

		self.CG=self.CG+1
		print('Clic gris:{}\n'.format(self.CG))
		self.combinaison.append('Clic gris')
		self.reaction.append('X')
		self.hasardbleu1()	
		
	def memecercle(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		self.MC=self.MC+1
		print('clic sur un même cercle:{}\n'.format(self.MC))
		self.combinaison.append('Même cercle')
		self.reaction.append('X')
		self.hasardbleu1()

	def time(self):                
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		f.write('Combinaison {}\n'.format(self.combinaison))
		f.write('Temps réponse {}\n'.format(self.reaction))
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		self.racine0.after_cancel(self.lancementsec)

		fin=self.fond0.create_text(self.w/4,self.h/4,text='FIN de cette tâche.', font='Arial 20')

		print('THE END\n')
		print('HETERO-GENERE\n')
		print('\nBonnes réponses:{}'.format(self.NR))
		f.write('Bonnes réponses=[ %.2f\n'%self.NR)
		print('Clic gris:{}'.format(self.CG))
		f.write('Clic gris:[ %.2f\n'%self.CG)
		print('Erreurs même cercle:{}'.format(self.MC))
		f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		self.total=self.NR+self.RTT+self.MC+self.CPT+self.PS+self.CG
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.total
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		print('RTmoy= %.3f secondes'%self.RTmoy)
		f.write('RTmoy=[ %.3f secondes\n'%self.RTmoy)
		print('RTmax= %.3f secondes'%self.RTmax)
		f.write('RTmax=[ %.3f secondes\n'%self.RTmax)
		print('RTmin= %.3f secondes'%self.RTmin)
		f.write('RTmin=[ %.3f secondes\n'%self.RTmin)
		print('Temps avant 1er clic= %.3f'%self.premierclic)
		f.write('Temps avant 1er clic=[ %.3f\n\n'%self.premierclic)

		self.hetero=0
		self.racine0.after_cancel(self.lancementsec)

		self.after(15000, self.fin)
		
	def fin(self, event):
		self.racine0.destroy()

ordre=1
ordretaches=[]
while ordre!=[]:
	if ordre==1:
		ordre=2
		print('HETERO\n')
		if __name__ == '__main__':
			app = hetero(None)
			app.title('my application')
			app.destroy()
			app.mainloop()
