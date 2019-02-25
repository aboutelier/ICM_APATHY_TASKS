import tkinter
from tkinter import *
import winsound
from winsound import *
import random
from timeit import time
import math
import os

nom = input("Nom sujet :")
os.mkdir('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{}'.format(nom))
        
class SDf(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
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
		self.RTmax=0
		self.RTmin=360

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)
		self.progr=(self.h/2)+250
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

		self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
		consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Faites des combinaisons de 4 cercles gris', font='Arial 30',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(180000, self.time)
		self.after(150000, self.debutchrono)

	def debutchrono(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		print('\nPlus que 30 sec\n')
		f.write('\n30 sec\n')
		self.startchrono()
		
	def startchrono(self):
		self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
		self.after(1000, self.sec)
		
	def sec(self):
		self.temps = self.temps-1
		if self.temps>0:
			self.fond0.delete(self.racine0,self.chrono)
			self.startchrono()
		else:
			self.fond0.delete(self.racine0,self.chrono)

	def hasard(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		self.coordcouleur=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]
		
		self.nbred1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred1)
		print('Red 1:{}'.format(self.nbred1))
		
		self.nbblue1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue1)
		print('Blue 1:{}\n'.format(self.nbblue1))
		
		self.nbred2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred2)
		print('Red 2:{}'.format(self.nbred2))
		
		self.nbblue2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue2)
		print('Blue 2:{}\n'.format(self.nbblue2))
		
		self.nbblue3=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue3)
		print('Blue 3:{}\n'.format(self.nbblue3))
		
		f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
		f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
		f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
		f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))
		
		f.write('[Coord Cercle 1[')
		f.write('Coord Cercle 2[')
		f.write('Coord Cercle 3[')
		f.write('Coord Cercle 4[')
		f.write('Combi[')
		f.write('RT\n')
		
		self.initialize()

	def initialize(self):
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
		
		self.numclic=0
		self.comb=[]
		
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

		self.ellipsered=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		self.ellipsered=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')

		self.tapp=time.perf_counter()

		self.fond0.bind('<ButtonPress-1>',self.clic)         

	def clic(self,event):
		self.clicx=event.x
		self.clicy=event.y
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
						
		self.gain=self.gain+0.10

		print('RT sec={}\n'.format(self.RT))
		f.write('{}\n'.format(self.RT))
		self.SRT=self.SRT+self.RT
		
		self.fond0.delete(self.racine0,self.pb)	
		self.progr=self.progr-2.50
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav',winsound.SND_FILENAME | SND_ASYNC)
		if self.RT>self.RTmax:
			self.RTmax=self.RT
			if self.RT<self.RTmin:
				self.RTmin=self.RT
		elif self.RT<self.RTmin:
			self.RTmin=self.RT
			
		self.initialize()

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
		self.numclic=self.numclic+1
		if self.numclic<4:
			self.fond0.bind('<Button-1>',self.clic)
		else:
			print('Combi:{}'.format(self.comb))
			if self.comb in self.combi:
				self.after(100,self.dejafait)
			else:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			
	def erreurbleu(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		print('Bleu touché!')
		self.NE=self.NE+1
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		print('Rouge touché!')
		self.NE=self.NE+1
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		self.ND=self.ND+1
		f.write('[Combi déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.initialize()

	def acote(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		self.AC=self.AC+1
		f.write('[{}, '.format(self.coordclicx))
		f.write('{}'.format(self.coordclicy))
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
		
		print('THE END\n')
		print('\n\nBonnes réponses:{}'.format(self.NR))
		f.write('\n\nBonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		print('Erreurs à coté:{}'.format(self.AC))
		f.write('Erreurs à côté:[ %.2f\n'%self.AC)
		self.NET=self.NE+self.ND+self.MC+self.AC
		print('Erreurs totales:{}'.format(self.NET))
		f.write('Erreurs totales:[{}\n'.format(self.NET))
		self.total=self.NR+self.NE+self.ND+self.MC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.NR
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)

		self.fond0.bind('<Triple-Button-1>',self.fin)
		
	def fin(self, event):
		self.racine0.destroy()

class SDF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		f.write("\nTACHE SPATIALE DIFFICILE FORT GAIN\n\n")
		print('TACHE SPATIALE DIFFICILE FORT GAIN')

		self.NR=0
		self.NE=0
		self.ND=0
		self.gain=0
		self.combi=[]
		self.MC=0
		self.AC=0

		self.temps=30

		self.SRT=0
		self.RTmax=0
		self.RTmin=360

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)
		self.progr=(self.h/2)+250
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

		self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
		consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Faites des combinaisons de 4 cercles gris', font='Arial 30',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(180000, self.time)
		self.after(150000, self.debutchrono)

	def debutchrono(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		print('\nPlus que 30 sec\n')
		f.write('\n30 sec\n')
		self.startchrono()
		
	def startchrono(self):
		self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
		self.after(1000, self.sec)
		
	def sec(self):
		self.temps = self.temps-1
		if self.temps>0:
			self.fond0.delete(self.racine0,self.chrono)
			self.startchrono()
		else:
			self.fond0.delete(self.racine0,self.chrono)

	def hasard(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		self.coordcouleur=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]
		
		self.nbred1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred1)
		print('Red 1:{}'.format(self.nbred1))
		
		self.nbblue1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue1)
		print('Blue 1:{}\n'.format(self.nbblue1))
		
		self.nbred2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred2)
		print('Red 2:{}'.format(self.nbred2))
		
		self.nbblue2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue2)
		print('Blue 2:{}\n'.format(self.nbblue2))
		
		self.nbblue3=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue3)
		print('Blue 3:{}\n'.format(self.nbblue3))
		
		f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
		f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
		f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
		f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))
		
		f.write('[Coord Cercle 1[')
		f.write('Coord Cercle 2[')
		f.write('Coord Cercle 3[')
		f.write('Coord Cercle 4[')
		f.write('Combi[')
		f.write('RT\n')
		
		self.initialize()

	def initialize(self):
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
		
		self.numclic=0
		self.comb=[]
		
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

		self.ellipsered=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		self.ellipsered=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')

		self.tapp=time.perf_counter()

		self.fond0.bind('<Button-1>',self.clic)       

	def clic(self,event):
		self.clicx=event.x
		self.clicy=event.y
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFaible.xls".format(nom,nom), "a")
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()    

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi')
		print('NR={}'.format(self.NR))
						
		self.gain=self.gain+1.00

		print('RT sec={}\n'.format(self.RT))
		f.write('[{}\n'.format(self.RT))
		self.SRT=self.SRT+self.RT

		self.fond0.delete(self.racine0,self.pb)
		self.progr=self.progr-5.00
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav',winsound.SND_FILENAME | SND_ASYNC)
		if self.RT>self.RTmax:
			self.RTmax=self.RT
			if self.RT<self.RTmin:
				self.RTmin=self.RT
		elif self.RT<self.RTmin:
			self.RTmin=self.RT
			
		self.initialize()

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
		self.numclic=self.numclic+1
		if self.numclic<4:
			self.fond0.bind('<Button-1>',self.clic)
		else:
			print('Combi:{}'.format(self.comb))
			if self.comb in self.combi:
				self.after(100,self.dejafait)
			else:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			
	def erreurbleu(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		print('Bleu touché!')
		self.NE=self.NE+1
		if self.numclic==0:
			f.write('[[[[Distracteur Bleu\n')
		elif self.numclic==1:
			f.write('[[[Distracteur Bleu\n')
		elif self.numclic==2:
			f.write('[[Distracteur Bleu\n')
		elif self.numclic==3:
			f.write('[Distracteur Bleu\n')
		print('raté!NE={}\n'.format(self.NE))
		self.initialize()

	def erreurrouge(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		print('Rouge touché!')
		self.NE=self.NE+1
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		self.ND=self.ND+1
		f.write('[Combi déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.initialize()

	def acote(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		self.AC=self.AC+1
		f.write('[{}, '.format(self.coordclicx))
		f.write('{}'.format(self.coordclicy))
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeDifficileFort.xls".format(nom,nom), "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
		
		print('THE END\n')
		print('\n\nBonnes réponses:{}'.format(self.NR))
		f.write('\n\nBonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		print('Erreurs à coté:{}'.format(self.AC))
		f.write('Erreurs à côté:[ %.2f\n'%self.AC)
		self.NET=self.NE+self.ND+self.MC+self.AC
		print('Erreurs totales:{}'.format(self.NET))
		f.write('Erreurs totales:[{}\n'.format(self.NET))
		self.total=self.NR+self.NE+self.ND+self.MC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.NR
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)

		self.fond0.bind('<Triple-Button-1>',self.fin)
                
	def fin(self, event):
		self.racine0.destroy()
class SFf(tkinter.Tk):
        def __init__(self,parent):
                self.racine0=tkinter.Tk()
                self.racine0.attributes('-fullscreen',True)
                self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')

                self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
                self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFaible.xls".format(nom,nom), "a")
                f.write("\nTACHE SPATIALE FACILE FAIBLE GAIN\n\n")
                print('TACHE SPATIALE FACILE FAIBLE GAIN')

                f.write('[Coord cible[')
                f.write('Coord distracteur[')
                f.write('Cercle choisi[')
                f.write('Clic X[')
                f.write('Clic Y[')
                f.write('RT sec[\n')

                self.NR=0
                self.NER=0
                self.NEG=0
                self.AC=0
                self.gain=0

                self.temps=30

                self.SRT=0
                self.RTmax=0
                self.RTmin=360

                self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
                self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)

                self.progr=(self.h/2)+250
                self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

                self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
                consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Touchez le cercle bleu',fill='blue', font='Arial 40',justify='center')

                self.fond0.bind('<Button-1>',self.attente)

        def attente(self,event):
                self.hasard()
                self.after(180000, self.time)
                self.after(150000, self.debutchrono)

        def debutchrono(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFaible.xls".format(nom,nom), "a")
                print('\nPlus que 30 sec\n')
                f.write('\n30 sec\n')
                self.startchrono()
		
        def startchrono(self):
                self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
                self.after(1000, self.sec)
                
        def sec(self):
                self.temps = self.temps-1
                if self.temps>0:
                        self.fond0.delete(self.racine0,self.chrono)
                        self.startchrono()
                else:
                        self.fond0.delete(self.racine0,self.chrono)
                        
        def hasard(self):
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

                self.couleur=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]
                
                self.nbred=random.choice(self.couleur)
                self.couleur.remove(self.nbred)
                print('Red 1:{}'.format(self.nbred))
                self.nbblue=random.choice(self.couleur)
                print('Blue:{}'.format(self.nbblue))
                
                self.initialize()

        def initialize(self):
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

                self.ellipsered=self.fond0.create_oval(self.nbred, fill='red', width='5')
                self.ellipseblue=self.fond0.create_oval(self.nbblue, fill='blue', width='5')

                self.tapp=time.perf_counter()

                self.fond0.bind('<Button-1>',self.clic)

        def clic(self,event):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFaible.xls".format(nom,nom), "a")
                f.write('{}'.format(self.nbblue))
                f.write('{}['.format(self.nbred))

                xclic=event.x
                yclic=event.y
                self.coordclicx=self.fond0.winfo_pointerx()
                self.coordclicy=self.fond0.winfo_pointery()
                print('clic x:{}'.format(self.coordclicx))
                print('clic y:{}'.format(self.coordclicy))
                if self.nbblue[0]<=xclic<=self.nbblue[2] and self.nbblue[1]<=yclic<=self.nbblue[3]:
                        self.NR=self.NR+1
                        print('Bien! NR={}'.format(self.NR))
                        f.write('Cible[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}['.format(self.coordclicy))

                        self.fond0.delete(self.racine0,self.pb)
                        self.progr=self.progr-0.88
                        self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
                        if self.NR%10==0:
                                self.gain=self.gain+0.10
                                if self.NR%50==0:
                                        winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav', winsound.SND_FILENAME | SND_ASYNC)

                        self.tclic=time.perf_counter()
                        self.RT=self.tclic-self.tapp
                        print('RT={}\n'.format(self.RT))
                        f.write('{}\n'.format(self.RT))
                        self.SRT=self.SRT+self.RT
                        if self.RT>self.RTmax:
                                self.RTmax=self.RT
                                if self.RT<self.RTmin:
                                        self.RTmin=self.RT
                        elif self.RT<self.RTmin:
                                        self.RTmin=self.RT

                elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
                        print('Rouge touché!')
                        f.write('Distracteur[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}[\n'.format(self.coordclicy))
                        
                        self.NER=self.NER+1
                        print('raté!NER={}\n'.format(self.NER))
                        self.initialize()
                else:
                        if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-225<yclic<=(self.h/2)-135 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-45<=yclic<=(self.h/2)+135) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+45 <=yclic<=(self.h/2)+135) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)-135<=yclic<=(self.h/2)+225) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+135<=yclic<=(self.h/2)+225):
                                print('Gris touché!')
                                f.write('Gris[')
                                f.write('{}['.format(self.coordclicx))
                                f.write('{}[\n'.format(self.coordclicy))
                                self.NEG=self.NEG+1
                                print('raté!NEG={}\n'.format(self.NEG))
                
                        else:
                                 print('A côté!')
                                 f.write('A cote[')
                                 f.write('{}['.format(self.coordclicx))
                                 f.write('{}[\n'.format(self.coordclicy))
                                 self.AC=self.AC+1
                                 print('raté!AC={}\n'.format(self.AC))

                self.hasard()

        def time(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFaible.xls".format(nom,nom), "a")                
                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
                
                print('THE END\n')
                print('Bonnes réponses:{}'.format(self.NR))
                f.write('\nBonnes réponses:[{}\n'.format(self.NR))
                print('Erreurs rouge:{}'.format(self.NER))
                f.write('Erreurs rouge:[{}\n'.format(self.NER))
                print('Erreurs gris:{}'.format(self.NEG))
                f.write('Erreurs gris:[{}\n'.format(self.NEG))
                print('Erreurs à côté:{}'.format(self.AC))
                f.write('Erreurs à côté:[{}\n'.format(self.AC))
                self.NE=self.NER+self.NEG+self.AC
                print('Erreurs totales:{}'.format(self.NE))
                f.write('Erreurs totales:[{}\n'.format(self.NE))
                self.total=self.NR+self.NE
                if self.total==0:
                        self.taux=0
                        self.RTmoy=0
                else:
                        self.taux=self.NR/self.total*100
                        self.RTmoy=self.SRT/self.NR
                print('Taux de réussite= %.2f'%self.taux)
                f.write('Taux de réussite=[ %.2f\n'%self.taux)
                gain=self.fond0.create_text(self.w/4,self.h/4,text='Vous avez gagné peu.', font='Arial 50', justify='center')
                print('RTmoy= %.3f'%self.RTmoy)
                f.write('RTmoy=[ %.3f\n'%self.RTmoy)
                print('RTmax= %.3f'%self.RTmax)
                f.write('RTmax=[ %.3f\n'%self.RTmax)
                print('RTmin= %.3f'%self.RTmin)
                f.write('RTmin=[ %.3f\n\n'%self.RTmin)

                self.fond0.bind('<Triple-Button-1>',self.fin)
                
        def fin(self, event):
                self.racine0.destroy()

class SFF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFort.xls".format(nom,nom), "a")
		f.write("\nTACHE SPATIALE FACILE FORT GAIN\n\n")
		print('TACHE SPATIALE FACILE FORT GAIN')

		f.write('[Coord cible[')
		f.write('Coord distracteur[')
		f.write('Cercle choisi[')
		f.write('Clic X[')
		f.write('Clic Y[')
		f.write('RT sec[\n')

		self.NR=0
		self.NER=0
		self.NEG=0
		self.AC=0
		self.gain=0

		self.temps=30

		self.SRT=0
		self.RTmax=0
		self.RTmin=360

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)

		self.progr=(self.h/2)+250
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

		self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
		consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Touchez le cercle bleu',fill='blue', font='Arial 40',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(180000, self.time)
		self.after(150000, self.debutchrono)

	def debutchrono(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFort.xls".format(nom,nom), "a")
		print('\nPlus que 30 sec\n')
		f.write('\n30 sec\n')
		self.startchrono()
		
	def startchrono(self):
		self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
		self.after(1000, self.sec)
		
	def sec(self):
		self.temps = self.temps-1
		if self.temps>0:
			self.fond0.delete(self.racine0,self.chrono)
			self.startchrono()
		else:
			self.fond0.delete(self.racine0,self.chrono)
	def hasard(self):
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

		self.couleur=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]
		
		self.nbred=random.choice(self.couleur)
		self.couleur.remove(self.nbred)
		print('Red 1:{}'.format(self.nbred))
		self.nbblue=random.choice(self.couleur)
		print('Blue:{}'.format(self.nbblue))
		
		self.initialize()

	def initialize(self):
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

		self.ellipsered=self.fond0.create_oval(self.nbred, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue, fill='blue', width='5')

		self.tapp=time.perf_counter()

		self.fond0.bind('<Button-1>',self.clic)

	def clic(self,event):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFort.xls".format(nom,nom), "a")
		f.write('{}'.format(self.nbblue))
		f.write('{}['.format(self.nbred))

		xclic=event.x
		yclic=event.y
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if self.nbblue[0]<=xclic<=self.nbblue[2] and self.nbblue[1]<=yclic<=self.nbblue[3]:
			self.NR=self.NR+1
			print('Bien! NR={}'.format(self.NR))
			f.write('Cible[')
			f.write('{}['.format(self.coordclicx))
			f.write('{}['.format(self.coordclicy))

			self.fond0.delete(self.racine0,self.pb)
			self.progr=self.progr-1.66
			self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
			if self.NR%10==0:
				self.gain=self.gain+1.00
				if self.NR%50==0:
					winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav', winsound.SND_FILENAME | SND_ASYNC)

			self.tclic=time.perf_counter()
			self.RT=self.tclic-self.tapp
			print('RT={}\n'.format(self.RT))
			f.write('{}\n'.format(self.RT))
			self.SRT=self.SRT+self.RT
			if self.RT>self.RTmax:
				self.RTmax=self.RT
				if self.RT<self.RTmin:
					self.RTmin=self.RT
			elif self.RT<self.RTmin:
					self.RTmin=self.RT

		elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
			print('Rouge touché!')
			f.write('Distracteur[')
			f.write('{}['.format(self.coordclicx))
			f.write('{}[\n'.format(self.coordclicy))
			
			self.NER=self.NER+1
			print('raté!NER={}\n'.format(self.NER))
			self.initialize()
		else:
			if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-225<yclic<=(self.h/2)-135 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-45<=yclic<=(self.h/2)+135) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+45 <=yclic<=(self.h/2)+135) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)-135<=yclic<=(self.h/2)+225) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+135<=yclic<=(self.h/2)+225):
				print('Gris touché!')
				f.write('Gris[')
				f.write('{}['.format(self.coordclicx))
				f.write('{}[\n'.format(self.coordclicy))
				self.NEG=self.NEG+1
				print('raté!NEG={}\n'.format(self.NEG))
		
			else:
				 print('A côté!')
				 f.write('A cote[')
				 f.write('{}['.format(self.coordclicx))
				 f.write('{}[\n'.format(self.coordclicy))
				 self.AC=self.AC+1
				 print('raté!AC={}\n'.format(self.AC))

		self.hasard()

	def time(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_SpatialeFacileFort.xls".format(nom,nom), "a")
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
		
		print('THE END\n')
		print('Bonnes réponses:{}'.format(self.NR))
		f.write('\nBonnes réponses:[{}\n'.format(self.NR))
		print('Erreurs rouge:{}'.format(self.NER))
		f.write('Erreurs rouge:[{}\n'.format(self.NER))
		print('Erreurs gris:{}'.format(self.NEG))
		f.write('Erreurs gris:[{}\n'.format(self.NEG))
		print('Erreurs à côté:{}'.format(self.AC))
		f.write('Erreurs à côté:[{}\n'.format(self.AC))
		self.NE=self.NER+self.NEG+self.AC
		print('Erreurs totales:{}'.format(self.NE))
		f.write('Erreurs totales:[{}\n'.format(self.NE))
		self.total=self.NR+self.NE
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.NR
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)
		
		self.fond0.bind('<Triple-Button-1>',self.fin)
                
	def fin(self, event):
		self.racine0.destroy()
		
class VDf(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		f.write("\nTACHE VERBALE DIFFICILE FAIBLE GAIN\n\n")
		print('TACHE VERBALE DIFFICILE FAIBLE GAIN')

		self.NR=0
		self.PC=0
		self.PV=0
		self.NE=0
		self.ND=0
		self.gain=0
		self.combi=[]
		self.MC=0
		self.AC=0

		self.temps=30

		self.SRT=0
		self.RTmax=0
		self.RTmin=180

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)
		self.progr=(self.h/2)+250
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

		self.coord0texte=[(self.w/2), (self.h/2)-180]
		self.coord1texte=[(self.w/2), (self.h/2)]
		self.coord2texte=[(self.w/2), (self.h/2)+180]
		self.coord3texte=[(self.w/2)-90, (self.h/2)-90]
		self.coord4texte=[(self.w/2)+90, (self.h/2)-90]
		self.coord5texte=[(self.w/2)-180, (self.h/2)]
		self.coord6texte=[(self.w/2)+180, (self.h/2)]
		self.coord7texte=[(self.w/2)-90, (self.h/2)+90]
		self.coord8texte=[(self.w/2)+90, (self.h/2)+90]
		self.coord9texte=[(self.w/2)-180, (self.h/2)+180]
		self.coord10texte=[(self.w/2)+180, (self.h/2)+180]
		self.coord11texte=[(self.w/2)-270, (self.h/2)+90]
		self.coord12texte=[(self.w/2)+270, (self.h/2)+90]
		self.coord13texte=[(self.w/2)-360, (self.h/2)+180]
		self.coord14texte=[(self.w/2)+360, (self.h/2)+180]

		self.coordtexte=[self.coord0texte, self.coord1texte, self.coord2texte, self.coord3texte, self.coord4texte, self.coord5texte, self.coord6texte, self.coord7texte, self.coord8texte, self.coord9texte, self.coord10texte, self.coord11texte, self.coord12texte, self.coord13texte, self.coord14texte]

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

		self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
		consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='  Faites des combinaisons de 4 lettres\n  en alternant consonnes et voyelles', font='Arial 30',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(180000, self.time)
		self.after(150000, self.debutchrono)

	def debutchrono(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		print('\nPlus que 30 sec\n')
		f.write('\n30 sec\n')
		self.startchrono()
		
	def startchrono(self):
		self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
		self.after(1000, self.sec)
		
	def sec(self):
		self.temps = self.temps-1
		if self.temps>0:
			self.fond0.delete(self.racine0,self.chrono)
			self.startchrono()
		else:
			self.fond0.delete(self.racine0,self.chrono)

	def hasard(self):               
		self.coordcouleur=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		
		self.coordconsonne1=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne1)
		self.coordconsonne2=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne2)
		self.coordconsonne3=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne3)
		self.coordconsonne4=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne4)
		self.coordconsonne5=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne5)
		self.coordconsonne6=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne6)
		self.coordconsonne7=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne7)
		self.coordconsonne8=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne8)
		self.coordconsonne9=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne9)
		self.coordconsonne10=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne10)

		self.coordvoyelle1=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle1)
		self.coordvoyelle2=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle2)
		self.coordvoyelle3=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle3)
		self.coordvoyelle4=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle4)
		self.coordvoyelle5=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle5)

		if self.coordvoyelle1==self.coord0texte or self.coordvoyelle2==self.coord0texte or self.coordvoyelle3==self.coord0texte or self.coordvoyelle4==self.coord0texte or self.coordvoyelle5==self.coord0texte:
			self.coordcouleur.remove(self.coord0)
		if self.coordvoyelle1==self.coord1texte or self.coordvoyelle2==self.coord1texte or self.coordvoyelle3==self.coord1texte or self.coordvoyelle4==self.coord1texte or self.coordvoyelle5==self.coord1texte:
			self.coordcouleur.remove(self.coord1)
		if self.coordvoyelle1==self.coord2texte or self.coordvoyelle2==self.coord2texte or self.coordvoyelle3==self.coord2texte or self.coordvoyelle4==self.coord2texte or self.coordvoyelle5==self.coord2texte:
			self.coordcouleur.remove(self.coord2)
		if self.coordvoyelle1==self.coord3texte or self.coordvoyelle2==self.coord3texte or self.coordvoyelle3==self.coord3texte or self.coordvoyelle4==self.coord3texte or self.coordvoyelle5==self.coord3texte:
			self.coordcouleur.remove(self.coord3)
		if self.coordvoyelle1==self.coord4texte or self.coordvoyelle2==self.coord4texte or self.coordvoyelle3==self.coord4texte or self.coordvoyelle4==self.coord4texte or self.coordvoyelle5==self.coord4texte:
			self.coordcouleur.remove(self.coord4)
		if self.coordvoyelle1==self.coord5texte or self.coordvoyelle2==self.coord5texte or self.coordvoyelle3==self.coord5texte or self.coordvoyelle4==self.coord5texte or self.coordvoyelle5==self.coord5texte:
			self.coordcouleur.remove(self.coord5)
		if self.coordvoyelle1==self.coord6texte or self.coordvoyelle2==self.coord6texte or self.coordvoyelle3==self.coord6texte or self.coordvoyelle4==self.coord6texte or self.coordvoyelle5==self.coord6texte:
			self.coordcouleur.remove(self.coord6)
		if self.coordvoyelle1==self.coord7texte or self.coordvoyelle2==self.coord7texte or self.coordvoyelle3==self.coord7texte or self.coordvoyelle4==self.coord7texte or self.coordvoyelle5==self.coord7texte:
			self.coordcouleur.remove(self.coord7)
		if self.coordvoyelle1==self.coord8texte or self.coordvoyelle2==self.coord8texte or self.coordvoyelle3==self.coord8texte or self.coordvoyelle4==self.coord8texte or self.coordvoyelle5==self.coord8texte:
			self.coordcouleur.remove(self.coord8)
		if self.coordvoyelle1==self.coord9texte or self.coordvoyelle2==self.coord9texte or self.coordvoyelle3==self.coord9texte or self.coordvoyelle4==self.coord9texte or self.coordvoyelle5==self.coord9texte:
			self.coordcouleur.remove(self.coord9)
		if self.coordvoyelle1==self.coord10texte or self.coordvoyelle2==self.coord10texte or self.coordvoyelle3==self.coord10texte or self.coordvoyelle4==self.coord10texte or self.coordvoyelle5==self.coord10texte:
			self.coordcouleur.remove(self.coord10)
		if self.coordvoyelle1==self.coord11texte or self.coordvoyelle2==self.coord11texte or self.coordvoyelle3==self.coord11texte or self.coordvoyelle4==self.coord11texte or self.coordvoyelle5==self.coord11texte:
			self.coordcouleur.remove(self.coord11)
		if self.coordvoyelle1==self.coord12texte or self.coordvoyelle2==self.coord12texte or self.coordvoyelle3==self.coord12texte or self.coordvoyelle4==self.coord12texte or self.coordvoyelle5==self.coord12texte:
			self.coordcouleur.remove(self.coord12)
		if self.coordvoyelle1==self.coord13texte or self.coordvoyelle2==self.coord13texte or self.coordvoyelle3==self.coord13texte or self.coordvoyelle4==self.coord13texte or self.coordvoyelle5==self.coord13texte:
			self.coordcouleur.remove(self.coord13)
		if self.coordvoyelle1==self.coord14texte or self.coordvoyelle2==self.coord14texte or self.coordvoyelle3==self.coord14texte or self.coordvoyelle4==self.coord14texte or self.coordvoyelle5==self.coord14texte:
			self.coordcouleur.remove(self.coord14)

		self.nbred1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred1)
		print('Red 1:{}'.format(self.nbred1))

		self.nbblue1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue1)
		print('Blue 1:{}\n'.format(self.nbblue1))
		
		self.nbred2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred2)
		print('Red 2:{}'.format(self.nbred2))
		
		self.nbblue2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue2)
		print('Blue 2:{}\n'.format(self.nbblue2))
		
		self.nbblue3=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue3)
		print('Blue 3:{}\n'.format(self.nbblue3))

		f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
		f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
		f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
		f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))

		self.consonne1=self.fond0.create_text(self.coordconsonne1,text='X', font='Arial 50')
		self.consonne2=self.fond0.create_text(self.coordconsonne2,text='C', font='Arial 50')
		self.consonne3=self.fond0.create_text(self.coordconsonne3,text='V', font='Arial 50')
		self.consonne4=self.fond0.create_text(self.coordconsonne4,text='G', font='Arial 50')
		self.consonne5=self.fond0.create_text(self.coordconsonne5,text='H', font='Arial 50')
		self.consonne6=self.fond0.create_text(self.coordconsonne6,text='M', font='Arial 50')
		self.consonne7=self.fond0.create_text(self.coordconsonne7,text='P', font='Arial 50')
		self.consonne8=self.fond0.create_text(self.coordconsonne8,text='Z', font='Arial 50')
		self.consonne9=self.fond0.create_text(self.coordconsonne9,text='S', font='Arial 50')
		self.consonne10=self.fond0.create_text(self.coordconsonne10,text='T', font='Arial 50')

		self.voyelle1=self.fond0.create_text(self.coordvoyelle1,text='A', font='Arial 50')
		self.voyelle2=self.fond0.create_text(self.coordvoyelle2,text='E', font='Arial 50')
		self.voyelle3=self.fond0.create_text(self.coordvoyelle3,text='I', font='Arial 50')
		self.voyelle4=self.fond0.create_text(self.coordvoyelle4,text='O', font='Arial 50')
		self.voyelle5=self.fond0.create_text(self.coordvoyelle5,text='U', font='Arial 50')

		f.write('Coord voyelle 1 {}\n'.format(self.coordvoyelle1))
		f.write('Coord voyelle 2 {}\n'.format(self.coordvoyelle2))
		f.write('Coord voyelle 3 {}\n'.format(self.coordvoyelle3))
		f.write('Coord voyelle 4 {}\n'.format(self.coordvoyelle4))
		f.write('Coord voyelle 5 {}\n\n'.format(self.coordvoyelle5))

		f.write('Coord consonne 1 {}\n'.format(self.coordconsonne1))
		f.write('Coord consonne 2 {}\n'.format(self.coordconsonne2))
		f.write('Coord consonne 3 {}\n'.format(self.coordconsonne3))
		f.write('Coord consonne 4 {}\n'.format(self.coordconsonne4))
		f.write('Coord consonne 5 {}\n'.format(self.coordconsonne5))
		f.write('Coord consonne 6 {}\n'.format(self.coordconsonne6))
		f.write('Coord consonne 7 {}\n'.format(self.coordconsonne7))
		f.write('Coord consonne 8 {}\n'.format(self.coordconsonne8))
		f.write('Coord consonne 9 {}\n'.format(self.coordconsonne9))
		f.write('Coord consonne 10 {}\n\n'.format(self.coordconsonne10))

		f.write('[Coord Lettre 1[')
		f.write('Coord Lettre 2[')
		f.write('Coord Lettre 3[')
		f.write('Coord Lettre 4[')
		f.write('Combi[')
		f.write('RT\n')
		
		self.initialize()

	def initialize(self):
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
		
		self.numclic=0
		self.comb=[]
		self.clicprecedent=0

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		
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

		self.consonne1=self.fond0.create_text(self.coordconsonne1,text='X', font='Arial 50')
		self.consonne2=self.fond0.create_text(self.coordconsonne2,text='C', font='Arial 50')
		self.consonne3=self.fond0.create_text(self.coordconsonne3,text='V', font='Arial 50')
		self.consonne4=self.fond0.create_text(self.coordconsonne4,text='G', font='Arial 50')
		self.consonne5=self.fond0.create_text(self.coordconsonne5,text='H', font='Arial 50')
		self.consonne6=self.fond0.create_text(self.coordconsonne6,text='M', font='Arial 50')
		self.consonne7=self.fond0.create_text(self.coordconsonne7,text='P', font='Arial 50')
		self.consonne8=self.fond0.create_text(self.coordconsonne8,text='Z', font='Arial 50')
		self.consonne9=self.fond0.create_text(self.coordconsonne9,text='S', font='Arial 50')
		self.consonne10=self.fond0.create_text(self.coordconsonne10,text='T', font='Arial 50')

		self.voyelle1=self.fond0.create_text(self.coordvoyelle1,text='A', font='Arial 50')
		self.voyelle2=self.fond0.create_text(self.coordvoyelle2,text='E', font='Arial 50')
		self.voyelle3=self.fond0.create_text(self.coordvoyelle3,text='I', font='Arial 50')
		self.voyelle4=self.fond0.create_text(self.coordvoyelle4,text='O', font='Arial 50')
		self.voyelle5=self.fond0.create_text(self.coordvoyelle5,text='U', font='Arial 50')

		self.ellipsered=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		self.ellipsered=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')
		
		self.tapp=time.perf_counter()

		self.fond0.bind('<Button-1>',self.clic)         

	def clic(self,event):
		self.clicx=event.x
		self.clicy=event.y
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0texte
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1texte
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2texte
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3texte
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4texte
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5texte
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6texte
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7texte
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8texte
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9texte
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10texte
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11texte
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12texte
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13texte
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14texte
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()    

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
							
		self.gain=self.gain+0.10

		print('RT sec={}\n'.format(self.RT))
		f.write('{}\n'.format(self.RT))
		self.SRT=self.SRT+self.RT

		self.fond0.delete(self.racine0,self.pb)			
		self.progr=self.progr-2.50
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav',winsound.SND_FILENAME | SND_ASYNC)
			
		if self.RT>self.RTmax:
			self.RTmax=self.RT
			if self.RT<self.RTmin:
				self.RTmin=self.RT
		elif self.RT<self.RTmin:
			self.RTmin=self.RT      
		self.initialize()

	def verifcercle(self):
		if self.clicn in self.comb:
			self.after(100,self.memecercle)
		elif self.nbblue1[0]<=self.clicx<=self.nbblue1[2] and self.nbblue1[1]<=self.clicy<=self.nbblue1[3]or self.nbblue2[0]<=self.clicx<=self.nbblue2[2] and self.nbblue2[1]<=self.clicy<=self.nbblue2[3] or self.nbblue3[0]<=self.clicx<=self.nbblue3[2] and self.nbblue3[1]<=self.clicy<=self.nbblue3[3]:
			self.after(100,self.erreurbleu)
		elif self.nbred1[0]<=self.clicx<=self.nbred1[2] and self.nbred1[1]<=self.clicy<=self.nbred1[3] or self.nbred2[0]<=self.clicx<=self.nbred2[2] and self.nbred2[1]<=self.clicy<=self.nbred2[3]:
			self.after(100,self.erreurrouge)
		else:
			self.veriftypelettre()

	def veriftypelettre(self):
		if self.clicprecedent==0:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.clicprecedent=1
				self.testcombi()
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.clicprecedent=2
				self.testcombi()
		elif self.clicprecedent==1:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.after(100,self.pasvoyelle)
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.clicprecedent=2
				self.testcombi()
		elif self.clicprecedent==2:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.clicprecedent=1
				self.testcombi()
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.after(100,self.pasconsonne)

	def pasconsonne(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		self.PC=self.PC+1
		if self.numclic==0:
			f.write('[[[[Pas consonne\n')
		elif self.numclic==1:
			f.write('[[[Pas consonne\n')
		elif self.numclic==2:
			f.write('[[Pas consonne\n')
		elif self.numclic==3:
			f.write('[Pas consonne\n')
		print('Pas consonne={}\n'.format(self.PC))
		self.initialize()

	def pasvoyelle(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		self.PV=self.PV+1
		if self.numclic==0:
			f.write('[[[[Pas voyelle\n')
		elif self.numclic==1:
			f.write('[[[Pas voyelle\n')
		elif self.numclic==2:
			f.write('[[Pas voyelle\n')
		elif self.numclic==3:
			f.write('[Pas voyelle\n')
		print('Pas voyelle={}\n'.format(self.PV))
		self.initialize()

	def testcombi(self):
		self.comb.append(self.clicn)
		print('clicn={}'.format(self.clicn))
		self.numclic=self.numclic+1		
		if self.numclic<4:
			self.fond0.bind('<Button-1>',self.clic)
		else:
			print('Combi:{}'.format(self.comb))
			if self.comb in self.combi:
				self.after(100,self.dejafait)
			else:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			
	def erreurbleu(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		print('Bleu touché!')
		self.NE=self.NE+1
		if self.numclic==0:
			f.write('[[[[Distracteur Bleu\n')
		elif self.numclic==1:
			f.write('[[[Distracteur Bleu\n')
		elif self.numclic==2:
			f.write('[[Distracteur Bleu\n')
		elif self.numclic==3:
			f.write('[Distracteur Bleu\n')
		print('raté!NE={}\n'.format(self.NE))
		self.initialize()

	def erreurrouge(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		print('Rouge touché!')
		self.NE=self.NE+1
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		self.ND=self.ND+1
		f.write('[Déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.initialize()

	def acote(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		self.AC=self.AC+1
		f.write('[{}, '.format(self.coordclicx))
		f.write('{}'.format(self.coordclicy))
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFaible.xls".format(nom,nom), "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
		
		print('THE END\n')
		print('\nBonnes réponses:{}'.format(self.NR))
		f.write('\nBonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		print('Erreurs pas consonne:{}'.format(self.PC))
		f.write('Erreurs pas consonne:[ %.2f\n'%self.PC)
		print('Erreurs pas voyelle:{}'.format(self.PV))
		f.write('Erreurs pas voyelle:[ %.2f\n'%self.PV)
		print('Erreurs à coté:{}'.format(self.AC))
		f.write('Erreurs à côté:[ %.2f\n'%self.AC)
		self.NET=self.NE+self.ND+self.MC+self.PC+self.PV+self.AC
		print('Erreurs totales:{}'.format(self.NET))
		f.write('Erreurs totales:[{}\n'.format(self.NET))
		self.total=self.NR+self.NE+self.ND+self.MC+self.PC+self.PV+self.AC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.NR
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/4,self.h/4,text='Vous avez gagné peu.', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)
		
		self.fond0.bind('<Triple-Button-1>',self.fin)
                
	def fin(self, event):
		self.racine0.destroy()

class VDF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces2 = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces2, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		f.write("\nTACHE VERBALE DIFFICILE FORT GAIN\n\n")
		print('TACHE VERBALE DIFFICILE FORT GAIN')

		self.NR=0
		self.PC=0
		self.PV=0
		self.NE=0
		self.ND=0
		self.gain=0
		self.combi=[]
		self.MC=0
		self.AC=0

		self.temps=30

		self.SRT=0
		self.RTmax=0
		self.RTmin=180
		self.clicprécédent=0

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)
		self.progr=(self.h/2)+250
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

		self.coord0texte=[(self.w/2), (self.h/2)-180]
		self.coord1texte=[(self.w/2), (self.h/2)]
		self.coord2texte=[(self.w/2), (self.h/2)+180]
		self.coord3texte=[(self.w/2)-90, (self.h/2)-90]
		self.coord4texte=[(self.w/2)+90, (self.h/2)-90]
		self.coord5texte=[(self.w/2)-180, (self.h/2)]
		self.coord6texte=[(self.w/2)+180, (self.h/2)]
		self.coord7texte=[(self.w/2)-90, (self.h/2)+90]
		self.coord8texte=[(self.w/2)+90, (self.h/2)+90]
		self.coord9texte=[(self.w/2)-180, (self.h/2)+180]
		self.coord10texte=[(self.w/2)+180, (self.h/2)+180]
		self.coord11texte=[(self.w/2)-270, (self.h/2)+90]
		self.coord12texte=[(self.w/2)+270, (self.h/2)+90]
		self.coord13texte=[(self.w/2)-360, (self.h/2)+180]
		self.coord14texte=[(self.w/2)+360, (self.h/2)+180]

		self.coordtexte=[self.coord0texte, self.coord1texte, self.coord2texte, self.coord3texte, self.coord4texte, self.coord5texte, self.coord6texte, self.coord7texte, self.coord8texte, self.coord9texte, self.coord10texte, self.coord11texte, self.coord12texte, self.coord13texte, self.coord14texte]

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

		self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
		consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='  Faites des combinaisons de 4 lettres\nen alternant consonnes et voyelles', font='Arial 30',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(180000, self.time)
		self.after(150000, self.debutchrono)

	def debutchrono(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		print('\nPlus que 30 sec\n')
		f.write('\n30 sec\n')
		self.startchrono()
		
	def startchrono(self):
		self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
		self.after(1000, self.sec)
		
	def sec(self):
		self.temps = self.temps-1
		if self.temps>0:
			self.fond0.delete(self.racine0,self.chrono)
			self.startchrono()
		else:
			self.fond0.delete(self.racine0,self.chrono)

	def hasard(self):               
		self.coordcouleur=[[(self.w/2)-45, (self.h/2)-225, (self.w/2)+45, (self.h/2)-135],[(self.w/2)-45, (self.h/2)-45, (self.w/2)+45, (self.h/2)+45],[(self.w/2)-45, (self.h/2)+135, (self.w/2)+45, (self.h/2)+225],[(self.w/2)-135, (self.h/2)-135, (self.w/2)-45, (self.h/2)-45],[(self.w/2)+45, (self.h/2)-135, (self.w/2)+135, (self.h/2)-45],[(self.w/2)-225, (self.h/2)-45, (self.w/2)-135, (self.h/2)+45],[(self.w/2)+135, (self.h/2)-45, (self.w/2)+225, (self.h/2)+45],[(self.w/2)-135, (self.h/2)+45, (self.w/2)-45, (self.h/2)+135],[(self.w/2)+45, (self.h/2)+45, (self.w/2)+135, (self.h/2)+135],[(self.w/2)-225, (self.h/2)+135, (self.w/2)-135, (self.h/2)+225],[(self.w/2)+135, (self.h/2)+135, (self.w/2)+225, (self.h/2)+225],[(self.w/2)-315, (self.h/2)+45, (self.w/2)-225, (self.h/2)+135],[(self.w/2)+225, (self.h/2)+45, (self.w/2)+315, (self.h/2)+135],[(self.w/2)-405, (self.h/2)+135, (self.w/2)-315, (self.h/2)+225],[(self.w/2)+315, (self.h/2)+135, (self.w/2)+405, (self.h/2)+225]]

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		
		self.coordconsonne1=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne1)
		self.coordconsonne2=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne2)
		self.coordconsonne3=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne3)
		self.coordconsonne4=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne4)
		self.coordconsonne5=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne5)
		self.coordconsonne6=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne6)
		self.coordconsonne7=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne7)
		self.coordconsonne8=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne8)
		self.coordconsonne9=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne9)
		self.coordconsonne10=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordconsonne10)

		self.coordvoyelle1=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle1)
		self.coordvoyelle2=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle2)
		self.coordvoyelle3=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle3)
		self.coordvoyelle4=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle4)
		self.coordvoyelle5=random.choice(self.coordtexte)
		self.coordtexte.remove(self.coordvoyelle5)

		if self.coordvoyelle1==self.coord0texte or self.coordvoyelle2==self.coord0texte or self.coordvoyelle3==self.coord0texte or self.coordvoyelle4==self.coord0texte or self.coordvoyelle5==self.coord0texte:
			self.coordcouleur.remove(self.coord0)
		if self.coordvoyelle1==self.coord1texte or self.coordvoyelle2==self.coord1texte or self.coordvoyelle3==self.coord1texte or self.coordvoyelle4==self.coord1texte or self.coordvoyelle5==self.coord1texte:
			self.coordcouleur.remove(self.coord1)
		if self.coordvoyelle1==self.coord2texte or self.coordvoyelle2==self.coord2texte or self.coordvoyelle3==self.coord2texte or self.coordvoyelle4==self.coord2texte or self.coordvoyelle5==self.coord2texte:
			self.coordcouleur.remove(self.coord2)
		if self.coordvoyelle1==self.coord3texte or self.coordvoyelle2==self.coord3texte or self.coordvoyelle3==self.coord3texte or self.coordvoyelle4==self.coord3texte or self.coordvoyelle5==self.coord3texte:
			self.coordcouleur.remove(self.coord3)
		if self.coordvoyelle1==self.coord4texte or self.coordvoyelle2==self.coord4texte or self.coordvoyelle3==self.coord4texte or self.coordvoyelle4==self.coord4texte or self.coordvoyelle5==self.coord4texte:
			self.coordcouleur.remove(self.coord4)
		if self.coordvoyelle1==self.coord5texte or self.coordvoyelle2==self.coord5texte or self.coordvoyelle3==self.coord5texte or self.coordvoyelle4==self.coord5texte or self.coordvoyelle5==self.coord5texte:
			self.coordcouleur.remove(self.coord5)
		if self.coordvoyelle1==self.coord6texte or self.coordvoyelle2==self.coord6texte or self.coordvoyelle3==self.coord6texte or self.coordvoyelle4==self.coord6texte or self.coordvoyelle5==self.coord6texte:
			self.coordcouleur.remove(self.coord6)
		if self.coordvoyelle1==self.coord7texte or self.coordvoyelle2==self.coord7texte or self.coordvoyelle3==self.coord7texte or self.coordvoyelle4==self.coord7texte or self.coordvoyelle5==self.coord7texte:
			self.coordcouleur.remove(self.coord7)
		if self.coordvoyelle1==self.coord8texte or self.coordvoyelle2==self.coord8texte or self.coordvoyelle3==self.coord8texte or self.coordvoyelle4==self.coord8texte or self.coordvoyelle5==self.coord8texte:
			self.coordcouleur.remove(self.coord8)
		if self.coordvoyelle1==self.coord9texte or self.coordvoyelle2==self.coord9texte or self.coordvoyelle3==self.coord9texte or self.coordvoyelle4==self.coord9texte or self.coordvoyelle5==self.coord9texte:
			self.coordcouleur.remove(self.coord9)
		if self.coordvoyelle1==self.coord10texte or self.coordvoyelle2==self.coord10texte or self.coordvoyelle3==self.coord10texte or self.coordvoyelle4==self.coord10texte or self.coordvoyelle5==self.coord10texte:
			self.coordcouleur.remove(self.coord10)
		if self.coordvoyelle1==self.coord11texte or self.coordvoyelle2==self.coord11texte or self.coordvoyelle3==self.coord11texte or self.coordvoyelle4==self.coord11texte or self.coordvoyelle5==self.coord11texte:
			self.coordcouleur.remove(self.coord11)
		if self.coordvoyelle1==self.coord12texte or self.coordvoyelle2==self.coord12texte or self.coordvoyelle3==self.coord12texte or self.coordvoyelle4==self.coord12texte or self.coordvoyelle5==self.coord12texte:
			self.coordcouleur.remove(self.coord12)
		if self.coordvoyelle1==self.coord13texte or self.coordvoyelle2==self.coord13texte or self.coordvoyelle3==self.coord13texte or self.coordvoyelle4==self.coord13texte or self.coordvoyelle5==self.coord13texte:
			self.coordcouleur.remove(self.coord13)
		if self.coordvoyelle1==self.coord14texte or self.coordvoyelle2==self.coord14texte or self.coordvoyelle3==self.coord14texte or self.coordvoyelle4==self.coord14texte or self.coordvoyelle5==self.coord14texte:
			self.coordcouleur.remove(self.coord14)

		self.nbred1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred1)
		print('Red 1:{}'.format(self.nbred1))

		self.nbblue1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue1)
		print('Blue 1:{}\n'.format(self.nbblue1))
		
		self.nbred2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred2)
		print('Red 2:{}'.format(self.nbred2))
		
		self.nbblue2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue2)
		print('Blue 2:{}\n'.format(self.nbblue2))
		
		self.nbblue3=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbblue3)
		print('Blue 3:{}\n'.format(self.nbblue3))

		f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
		f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
		f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
		f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))

		self.consonne1=self.fond0.create_text(self.coordconsonne1,text='X', font='Arial 50')
		self.consonne2=self.fond0.create_text(self.coordconsonne2,text='C', font='Arial 50')
		self.consonne3=self.fond0.create_text(self.coordconsonne3,text='V', font='Arial 50')
		self.consonne4=self.fond0.create_text(self.coordconsonne4,text='G', font='Arial 50')
		self.consonne5=self.fond0.create_text(self.coordconsonne5,text='H', font='Arial 50')
		self.consonne6=self.fond0.create_text(self.coordconsonne6,text='M', font='Arial 50')
		self.consonne7=self.fond0.create_text(self.coordconsonne7,text='P', font='Arial 50')
		self.consonne8=self.fond0.create_text(self.coordconsonne8,text='Z', font='Arial 50')
		self.consonne9=self.fond0.create_text(self.coordconsonne9,text='S', font='Arial 50')
		self.consonne10=self.fond0.create_text(self.coordconsonne10,text='T', font='Arial 50')

		self.voyelle1=self.fond0.create_text(self.coordvoyelle1,text='A', font='Arial 50')
		self.voyelle2=self.fond0.create_text(self.coordvoyelle2,text='E', font='Arial 50')
		self.voyelle3=self.fond0.create_text(self.coordvoyelle3,text='I', font='Arial 50')
		self.voyelle4=self.fond0.create_text(self.coordvoyelle4,text='O', font='Arial 50')
		self.voyelle5=self.fond0.create_text(self.coordvoyelle5,text='U', font='Arial 50')

		f.write('Coord voyelle 1 {}\n'.format(self.coordvoyelle1))
		f.write('Coord voyelle 2 {}\n'.format(self.coordvoyelle2))
		f.write('Coord voyelle 3 {}\n'.format(self.coordvoyelle3))
		f.write('Coord voyelle 4 {}\n'.format(self.coordvoyelle4))
		f.write('Coord voyelle 5 {}\n\n'.format(self.coordvoyelle5))

		f.write('Coord consonne 1 {}\n'.format(self.coordconsonne1))
		f.write('Coord consonne 2 {}\n'.format(self.coordconsonne2))
		f.write('Coord consonne 3 {}\n'.format(self.coordconsonne3))
		f.write('Coord consonne 4 {}\n'.format(self.coordconsonne4))
		f.write('Coord consonne 5 {}\n'.format(self.coordconsonne5))
		f.write('Coord consonne 6 {}\n'.format(self.coordconsonne6))
		f.write('Coord consonne 7 {}\n'.format(self.coordconsonne7))
		f.write('Coord consonne 8 {}\n'.format(self.coordconsonne8))
		f.write('Coord consonne 9 {}\n'.format(self.coordconsonne9))
		f.write('Coord consonne 10 {}\n\n'.format(self.coordconsonne10))

		f.write('[Coord Lettre 1[')
		f.write('Coord Lettre 2[')
		f.write('Coord Lettre 3[')
		f.write('Coord Lettre 4[')
		f.write('Combi[')
		f.write('RT\n')
		
		self.initialize()
	def initialize(self):
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
		
		self.numclic=0
		self.comb=[]
		self.clicprecedent=0

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		
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

		self.consonne1=self.fond0.create_text(self.coordconsonne1,text='X', font='Arial 50')
		self.consonne2=self.fond0.create_text(self.coordconsonne2,text='C', font='Arial 50')
		self.consonne3=self.fond0.create_text(self.coordconsonne3,text='V', font='Arial 50')
		self.consonne4=self.fond0.create_text(self.coordconsonne4,text='G', font='Arial 50')
		self.consonne5=self.fond0.create_text(self.coordconsonne5,text='H', font='Arial 50')
		self.consonne6=self.fond0.create_text(self.coordconsonne6,text='M', font='Arial 50')
		self.consonne7=self.fond0.create_text(self.coordconsonne7,text='P', font='Arial 50')
		self.consonne8=self.fond0.create_text(self.coordconsonne8,text='Z', font='Arial 50')
		self.consonne9=self.fond0.create_text(self.coordconsonne9,text='S', font='Arial 50')
		self.consonne10=self.fond0.create_text(self.coordconsonne10,text='T', font='Arial 50')

		self.voyelle1=self.fond0.create_text(self.coordvoyelle1,text='A', font='Arial 50')
		self.voyelle2=self.fond0.create_text(self.coordvoyelle2,text='E', font='Arial 50')
		self.voyelle3=self.fond0.create_text(self.coordvoyelle3,text='I', font='Arial 50')
		self.voyelle4=self.fond0.create_text(self.coordvoyelle4,text='O', font='Arial 50')
		self.voyelle5=self.fond0.create_text(self.coordvoyelle5,text='U', font='Arial 50')

		self.ellipsered=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		self.ellipsered=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
		self.ellipseblue=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')
		
		self.tapp=time.perf_counter()

		self.fond0.bind('<Button-1>',self.clic)         

	def clic(self,event):
		self.clicx=event.x
		self.clicy=event.y
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0texte
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1texte
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2texte
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3texte
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4texte
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5texte
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6texte
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7texte
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8texte
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9texte
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10texte
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11texte
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12texte
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13texte
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14texte
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()    

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
							
		self.gain=self.gain+1.00

		print('RT sec={}\n'.format(self.RT))
		f.write('{}\n'.format(self.RT))
		self.SRT=self.SRT+self.RT

		self.fond0.delete(self.racine0,self.pb)			
		self.progr=self.progr-5.00
		self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav',winsound.SND_FILENAME | SND_ASYNC)
		if self.RT>self.RTmax:
			self.RTmax=self.RT
			if self.RT<self.RTmin:
				self.RTmin=self.RT
		elif self.RT<self.RTmin:
			self.RTmin=self.RT      
		self.initialize()

	def verifcercle(self):
		if self.clicn in self.comb:
			self.after(100,self.memecercle)
		elif self.nbblue1[0]<=self.clicx<=self.nbblue1[2] and self.nbblue1[1]<=self.clicy<=self.nbblue1[3]or self.nbblue2[0]<=self.clicx<=self.nbblue2[2] and self.nbblue2[1]<=self.clicy<=self.nbblue2[3] or self.nbblue3[0]<=self.clicx<=self.nbblue3[2] and self.nbblue3[1]<=self.clicy<=self.nbblue3[3]:
			self.after(100,self.erreurbleu)
		elif self.nbred1[0]<=self.clicx<=self.nbred1[2] and self.nbred1[1]<=self.clicy<=self.nbred1[3] or self.nbred2[0]<=self.clicx<=self.nbred2[2] and self.nbred2[1]<=self.clicy<=self.nbred2[3]:
			self.after(100,self.erreurrouge)
		else:
			self.veriftypelettre()

	def veriftypelettre(self):
		if self.clicprecedent==0:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.clicprecedent=1
				self.testcombi()
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.clicprecedent=2
				self.testcombi()
		elif self.clicprecedent==1:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.after(100,self.pasvoyelle)
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.clicprecedent=2
				self.testcombi()
		elif self.clicprecedent==2:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.clicprecedent=1
				self.testcombi()
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.after(100,self.pasconsonne)

	def pasconsonne(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		self.PC=self.PC+1
		if self.numclic==0:
			f.write('[[[[Pas consonne\n')
		elif self.numclic==1:
			f.write('[[[Pas consonne\n')
		elif self.numclic==2:
			f.write('[[Pas consonne\n')
		elif self.numclic==3:
			f.write('[Pas consonne\n')
		print('Pas consonne={}\n'.format(self.PC))
		self.initialize()

	def pasvoyelle(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		self.PV=self.PV+1
		if self.numclic==0:
			f.write('[[[[Pas voyelle\n')
		elif self.numclic==1:
			f.write('[[[Pas voyelle\n')
		elif self.numclic==2:
			f.write('[[Pas voyelle\n')
		elif self.numclic==3:
			f.write('[Pas voyelle\n')
		print('Pas voyelle={}\n'.format(self.PV))
		self.initialize()

	def testcombi(self):
		self.comb.append(self.clicn)
		print('clicn={}'.format(self.clicn))
		self.numclic=self.numclic+1		
		if self.numclic<4:
			self.fond0.bind('<Button-1>',self.clic)
		else:
			print('Combi:{}'.format(self.comb))
			if self.comb in self.combi:
				self.after(100,self.dejafait)
			else:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			
	def erreurbleu(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		print('Bleu touché!')
		self.NE=self.NE+1
		if self.numclic==0:
			f.write('[[[[Distracteur Bleu\n')
		elif self.numclic==1:
			f.write('[[[Distracteur Bleu\n')
		elif self.numclic==2:
			f.write('[[Distracteur Bleu\n')
		elif self.numclic==3:
			f.write('[Distracteur Bleu\n')
		print('raté!NE={}\n'.format(self.NE))
		self.initialize()

	def erreurrouge(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		print('Rouge touché!')
		self.NE=self.NE+1
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		self.ND=self.ND+1
		f.write('[Déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.initialize()

	def acote(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		self.AC=self.AC+1
		f.write('[{}, '.format(self.coordclicx))
		f.write('{}'.format(self.coordclicy))
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleDifficileFort.xls".format(nom,nom), "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
		
		print('THE END\n')
		print('\nBonnes réponses:{}'.format(self.NR))
		f.write('\nBonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		print('Erreurs pas consonne:{}'.format(self.PC))
		f.write('Erreurs pas consonne:[ %.2f\n'%self.PC)
		print('Erreurs pas voyelle:{}'.format(self.PV))
		f.write('Erreurs pas voyelle:[ %.2f\n'%self.PV)
		print('Erreurs à coté:{}'.format(self.AC))
		f.write('Erreurs à côté:[ %.2f\n'%self.AC)
		self.NET=self.NE+self.ND+self.MC+self.PC+self.PV+self.AC
		print('Erreurs totales:{}'.format(self.NET))
		f.write('Erreurs totales:[{}\n'.format(self.NET))
		self.total=self.NR+self.NE+self.ND+self.MC+self.PC+self.PV+self.AC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.NR
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)
		
		self.fond0.bind('<Triple-Button-1>',self.fin)
                
	def fin(self, event):
		self.racine0.destroy()

class VFf(tkinter.Tk):
        def __init__(self,parent):
                self.racine0=tkinter.Tk()
                self.racine0.attributes('-fullscreen',True)
                self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')

                self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
                self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFaible.xls".format(nom,nom), "a")
                f.write("\nTACHE VERBALE FACILE FAIBLE GAIN\n\n")
                print('TACHE VERBALE FACILE FAIBLE GAIN')

                f.write('Mot cible[')
                f.write('Coord cible[')
                f.write('Mot distracteur[')
                f.write('Coord distracteur[')
                f.write('Cercle choisi[')
                f.write('Clic X[')
                f.write('Clic Y[')
                f.write('RT sec[\n')
                
                self.NR=0
                self.NED=0
                self.NEG=0
                self.AC=0
                self.gain=0

                self.temps=30

                self.SRT=0
                self.RTmax=0
                self.RTmin=360

                self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
                self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)

                self.progr=(self.h/2)+250
                self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

                self.coord0texte=[(self.w/2), (self.h/2)-180]
                self.coord1texte=[(self.w/2), (self.h/2)]
                self.coord2texte=[(self.w/2), (self.h/2)+180]
                self.coord3texte=[(self.w/2)-90, (self.h/2)-90]
                self.coord4texte=[(self.w/2)+90, (self.h/2)-90]
                self.coord5texte=[(self.w/2)-180, (self.h/2)]
                self.coord6texte=[(self.w/2)+180, (self.h/2)]
                self.coord7texte=[(self.w/2)-90, (self.h/2)+90]
                self.coord8texte=[(self.w/2)+90, (self.h/2)+90]
                self.coord9texte=[(self.w/2)-180, (self.h/2)+180]
                self.coord10texte=[(self.w/2)+180, (self.h/2)+180]
                self.coord11texte=[(self.w/2)-270, (self.h/2)+90]
                self.coord12texte=[(self.w/2)+270, (self.h/2)+90]
                self.coord13texte=[(self.w/2)-360, (self.h/2)+180]
                self.coord14texte=[(self.w/2)+360, (self.h/2)+180]

                self.coordtexte=[self.coord0texte, self.coord1texte, self.coord2texte, self.coord3texte, self.coord4texte, self.coord5texte, self.coord6texte, self.coord7texte, self.coord8texte, self.coord9texte, self.coord10texte, self.coord11texte, self.coord12texte, self.coord13texte, self.coord14texte]

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

                self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
                consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Touchez le mot commençant\npar "M" ou "m"',fill='black', font='Arial 40',justify='center')

                self.fond0.bind('<Button-1>',self.attente)

        def attente(self,event):
                self.hasard()
                self.after(180000, self.time)
                self.after(150000, self.debutchrono)

        def debutchrono(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFort.xls".format(nom,nom), "a")
                print('\nPlus que 30 sec\n')
                f.write('\n30 sec\n')
                self.startchrono()
                
        def startchrono(self):
                self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
                self.after(1000, self.sec)
                
        def sec(self):
                self.temps = self.temps-1
                if self.temps>0:
                        self.fond0.delete(self.racine0,self.chrono)
                        self.startchrono()
                else:
                        self.fond0.delete(self.racine0,self.chrono)

        def hasard(self):
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

                self.lettre1cible=["M", "m"]
                self.voyelle=["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
                self.consonne1=["X", "T", "P", "S", "V", "G", "H", "C", "Z", "x", "t", "p", "s", "v", "g", "h", "c", "z"]
                self.consonne2=["M", "X", "T", "P", "S", "V", "G", "H", "C", "Z", "m", "x", "t", "p", "s", "v", "g", "h", "c", "z"]
                self.motcible=random.choice(self.lettre1cible)+random.choice(self.voyelle)+random.choice(self.consonne2)+random.choice(self.voyelle)
                self.motdistracteur=random.choice(self.consonne1)+random.choice(self.voyelle)+random.choice(self.consonne2)+random.choice(self.voyelle)

                self.initialize()

        def initialize(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFaible.xls".format(nom,nom), "a")

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

                self.coordmot=[self.coord0texte, self.coord1texte, self.coord2texte, self.coord3texte, self.coord4texte, self.coord5texte, self.coord6texte, self.coord7texte, self.coord8texte, self.coord9texte, self.coord10texte, self.coord11texte, self.coord12texte, self.coord13texte, self.coord14texte]

                self.coordmotdistracteur=random.choice(self.coordmot)
                self.coordmot.remove(self.coordmotdistracteur)
                self.textedistracteur=self.fond0.create_text(self.coordmotdistracteur,text=self.motdistracteur,fill='black', font='Arial 20 bold')
                print('Distracteur:{}'.format(self.coordmotdistracteur))
                
                self.coordmotcible=random.choice(self.coordmot)
                self.textecible=self.fond0.create_text(self.coordmotcible,text=self.motcible,fill='black', font='Arial 20 bold')
                print('Cible:{}'.format(self.coordmotdistracteur))

                if self.coordmotcible==self.coord0texte :
                        self.nbblue=self.coord0
                elif self.coordmotcible==self.coord1texte :
                        self.nbblue=self.coord1
                elif self.coordmotcible==self.coord2texte :
                        self.nbblue=self.coord2
                elif self.coordmotcible==self.coord3texte :
                        self.nbblue=self.coord3
                elif self.coordmotcible==self.coord4texte :
                        self.nbblue=self.coord4
                elif self.coordmotcible==self.coord5texte :
                        self.nbblue=self.coord5
                elif self.coordmotcible==self.coord6texte :
                        self.nbblue=self.coord6
                elif self.coordmotcible==self.coord7texte :
                        self.nbblue=self.coord7
                elif self.coordmotcible==self.coord8texte :
                        self.nbblue=self.coord8
                elif self.coordmotcible==self.coord9texte :
                        self.nbblue=self.coord9
                elif self.coordmotcible==self.coord10texte :
                        self.nbblue=self.coord10
                elif self.coordmotcible==self.coord11texte :
                        self.nbblue=self.coord11
                elif self.coordmotcible==self.coord12texte :
                        self.nbblue=self.coord12
                elif self.coordmotcible==self.coord13texte :
                        self.nbblue=self.coord13
                elif self.coordmotcible==self.coord14texte :
                        self.nbblue=self.coord14

                if self.coordmotdistracteur==self.coord0texte :
                        self.nbred=self.coord0
                elif self.coordmotdistracteur==self.coord1texte :
                        self.nbred=self.coord1
                elif self.coordmotdistracteur==self.coord2texte :
                        self.nbred=self.coord2
                elif self.coordmotdistracteur==self.coord3texte :
                        self.nbred=self.coord3
                elif self.coordmotdistracteur==self.coord4texte :
                        self.nbred=self.coord4
                elif self.coordmotdistracteur==self.coord5texte :
                        self.nbred=self.coord5
                elif self.coordmotdistracteur==self.coord6texte :
                        self.nbred=self.coord6
                elif self.coordmotdistracteur==self.coord7texte :
                        self.nbred=self.coord7
                elif self.coordmotdistracteur==self.coord8texte :
                        self.nbred=self.coord8
                elif self.coordmotdistracteur==self.coord9texte :
                        self.nbred=self.coord9
                elif self.coordmotdistracteur==self.coord10texte :
                        self.nbred=self.coord10
                elif self.coordmotdistracteur==self.coord11texte :
                        self.nbred=self.coord11
                elif self.coordmotdistracteur==self.coord12texte :
                        self.nbred=self.coord12
                elif self.coordmotdistracteur==self.coord13texte :
                        self.nbred=self.coord13
                elif self.coordmotdistracteur==self.coord14texte :
                        self.nbred=self.coord14
                
                self.tapp=time.perf_counter()

                self.fond0.bind('<Button-1>',self.clic)

        def clic(self,event):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFaible.xls".format(nom,nom), "a")

                f.write('{}'.format(self.motcible))
                f.write('{}['.format(self.nbblue))
                f.write('{}'.format(self.motdistracteur))
                f.write('{}['.format(self.nbred))

                xclic=event.x
                yclic=event.y
                self.coordclicx=self.fond0.winfo_pointerx()
                self.coordclicy=self.fond0.winfo_pointery()
                print('clic x:{}'.format(self.coordclicx))
                print('clic y:{}'.format(self.coordclicy))
                if self.nbblue[0]<=xclic<=self.nbblue[2] and self.nbblue[1]<=yclic<=self.nbblue[3]:
                        self.NR=self.NR+1
                        print('Bien! NR={}'.format(self.NR))
                        f.write('Cible[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}['.format(self.coordclicy))

                        self.fond0.delete(self.racine0,self.pb)
                        self.progr=self.progr-0.83
                        self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
                        if self.NR%10==0:
                                self.gain=self.gain+0.10
                                if self.NR%50==0:
                                        winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav', winsound.SND_FILENAME | SND_ASYNC)

                        self.tclic=time.perf_counter()
                        self.RT=self.tclic-self.tapp
                        print('RT={}\n'.format(self.RT))
                        f.write('{}\n'.format(self.RT))
                        self.SRT=self.SRT+self.RT
                        if self.RT>self.RTmax:
                                self.RTmax=self.RT
                                if self.RT<self.RTmin:
                                        self.RTmin=self.RT
                        elif self.RT<self.RTmin:
                                        self.RTmin=self.RT

                elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
                        print('Distracteur touché!')
                        f.write('Distracteur[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}[\n'.format(self.coordclicy))
                        self.NED=self.NED+1
                        print('raté!NED={}\n'.format(self.NED))
                        self.initialize()
                else:
                        if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-225<yclic<=(self.h/2)-135 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-45<=yclic<=(self.h/2)+135) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+45 <=yclic<=(self.h/2)+135) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)-135<=yclic<=(self.h/2)+225) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+135<=yclic<=(self.h/2)+225):
                                print('Gris touché!')
                                f.write('Gris[')
                                f.write('{}['.format(self.coordclicx))
                                f.write('{}[\n'.format(self.coordclicy))
                                self.NEG=self.NEG+1
                                print('raté!NEG={}\n'.format(self.NEG))
                
                        else:
                                 print('A côté!')
                                 f.write('A cote[')
                                 f.write('{}['.format(self.coordclicx))
                                 f.write('{}[\n'.format(self.coordclicy))
                                 self.AC=self.AC+1
                                 print('raté!AC={}\n'.format(self.AC))

                self.hasard()

        def time(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFaible.xls".format(nom,nom), "a")
                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
                
                print('THE END\n')
                print('Bonnes réponses:{}'.format(self.NR))
                f.write('\nBonnes réponses:[{}\n'.format(self.NR))
                print('Erreurs distracteur:{}'.format(self.NED))
                f.write('Erreurs distracteur:[{}\n'.format(self.NED))
                print('Erreurs gris:{}'.format(self.NEG))
                f.write('Erreurs gris:[{}\n'.format(self.NEG))
                print('Erreurs à côté:{}'.format(self.AC))
                f.write('Erreurs à côté:[{}\n'.format(self.AC))
                self.NE=self.NEG+self.NED+self.AC
                print('Erreurs totales:{}'.format(self.NE))
                f.write('Erreurs totales:[{}\n'.format(self.NE))
                self.total=self.NR+self.NE
                if self.total==0:
                        self.taux=0
                        self.RTmoy=0
                else:
                        self.taux=self.NR/self.total*100
                        self.RTmoy=self.SRT/self.NR
                print('Taux de réussite= %.2f'%self.taux)
                f.write('Taux de réussite=[ %.2f\n'%self.taux)
                gain=self.fond0.create_text(self.w/4,self.h/4,text='Vous avez gagné peu.', font='Arial 50', justify='center')
                print('RTmoy sec= %.3f'%self.RTmoy)
                f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
                print('RTmax sec= %.3f'%self.RTmax)
                f.write('RTmax sec=[ %.3f\n'%self.RTmax)
                print('RTmin sec= %.3f'%self.RTmin)
                f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)
		
                self.fond0.bind('<Triple-Button-1>',self.fin)
                
        def fin(self, event):
                self.racine0.destroy()

class VFF(tkinter.Tk):
        def __init__(self,parent):
                self.racine0=tkinter.Tk()
                self.racine0.attributes('-fullscreen',True)
                self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')

                self.pieces2 = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
                self.fond0.create_image(50, 10, image = self.pieces2, anchor = NW)

                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFort.xls".format(nom,nom), "a")
                f.write("\nTACHE VERBALE FACILE FORT GAIN\n\n")
                print('TACHE VERBALE FACILE FORT GAIN')

                f.write('Mot cible[')
                f.write('Coord cible[')
                f.write('Mot distracteur[')
                f.write('Coord distracteur[')
                f.write('Cercle choisi[')
                f.write('Clic X[')
                f.write('Clic Y[')
                f.write('RT sec[\n')
                
                self.NR=0
                self.NED=0
                self.NEG=0
                self.AC=0
                self.gain=0

                self.temps=30

                self.SRT=0
                self.RTmax=0
                self.RTmin=360

                self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
                self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)

                self.progr=(self.h/2)+250
                self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')

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

                self.coord0texte=[(self.w/2), (self.h/2)-180]
                self.coord1texte=[(self.w/2), (self.h/2)]
                self.coord2texte=[(self.w/2), (self.h/2)+180]
                self.coord3texte=[(self.w/2)-90, (self.h/2)-90]
                self.coord4texte=[(self.w/2)+90, (self.h/2)-90]
                self.coord5texte=[(self.w/2)-180, (self.h/2)]
                self.coord6texte=[(self.w/2)+180, (self.h/2)]
                self.coord7texte=[(self.w/2)-90, (self.h/2)+90]
                self.coord8texte=[(self.w/2)+90, (self.h/2)+90]
                self.coord9texte=[(self.w/2)-180, (self.h/2)+180]
                self.coord10texte=[(self.w/2)+180, (self.h/2)+180]
                self.coord11texte=[(self.w/2)-270, (self.h/2)+90]
                self.coord12texte=[(self.w/2)+270, (self.h/2)+90]
                self.coord13texte=[(self.w/2)-360, (self.h/2)+180]
                self.coord14texte=[(self.w/2)+360, (self.h/2)+180]

                self.coordtexte=[self.coord0texte, self.coord1texte, self.coord2texte, self.coord3texte, self.coord4texte, self.coord5texte, self.coord6texte, self.coord7texte, self.coord8texte, self.coord9texte, self.coord10texte, self.coord11texte, self.coord12texte, self.coord13texte, self.coord14texte]

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

                self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
                consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Touchez le mot commençant\npar "P" ou "p"',fill='black', font='Arial 40',justify='center')

                self.fond0.bind('<Button-1>',self.attente)

        def attente(self,event):
                self.hasard()
                self.after(180000, self.time)
                self.after(150000, self.debutchrono)

        def debutchrono(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFort.xls".format(nom,nom), "a")
                print('\nPlus que 30 sec\n')
                f.write('\n30 sec\n')
                self.startchrono()
                
        def startchrono(self):
                self.chrono=self.fond0.create_text(self.w/6,self.h/2,text="{}".format(self.temps), font=('Arial 120 bold'),fill='black')
                self.after(1000, self.sec)
                
        def sec(self):
                self.temps = self.temps-1
                if self.temps>0:
                        self.fond0.delete(self.racine0,self.chrono)
                        self.startchrono()
                else:
                        self.fond0.delete(self.racine0,self.chrono)

        def hasard(self):
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

                self.lettre1cible=["P", "p"]
                self.voyelle=["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
                self.consonne1=["X", "T", "M", "S", "V", "G", "H", "C", "Z", "x", "t", "m", "s", "v", "g", "h", "c", "z"]
                self.consonne2=["M", "X", "T", "P", "S", "V", "G", "H", "C", "Z", "m", "x", "t", "p", "s", "v", "g", "h", "c", "z"]
                self.motcible=random.choice(self.lettre1cible)+random.choice(self.voyelle)+random.choice(self.consonne2)+random.choice(self.voyelle)
                self.motdistracteur=random.choice(self.consonne1)+random.choice(self.voyelle)+random.choice(self.consonne2)+random.choice(self.voyelle)

                self.initialize()

        def initialize(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFort.xls".format(nom,nom), "a")

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

                self.coordmot=[self.coord0texte, self.coord1texte, self.coord2texte, self.coord3texte, self.coord4texte, self.coord5texte, self.coord6texte, self.coord7texte, self.coord8texte, self.coord9texte, self.coord10texte, self.coord11texte, self.coord12texte, self.coord13texte, self.coord14texte]

                self.coordmotdistracteur=random.choice(self.coordmot)
                self.coordmot.remove(self.coordmotdistracteur)
                self.textedistracteur=self.fond0.create_text(self.coordmotdistracteur,text=self.motdistracteur,fill='black', font='Arial 20 bold')
                print('Distracteur:{}'.format(self.coordmotdistracteur))
                
                self.coordmotcible=random.choice(self.coordmot)
                self.textecible=self.fond0.create_text(self.coordmotcible,text=self.motcible,fill='black', font='Arial 20 bold')
                print('Cible:{}'.format(self.coordmotdistracteur))

                if self.coordmotcible==self.coord0texte :
                        self.nbblue=self.coord0
                elif self.coordmotcible==self.coord1texte :
                        self.nbblue=self.coord1
                elif self.coordmotcible==self.coord2texte :
                        self.nbblue=self.coord2
                elif self.coordmotcible==self.coord3texte :
                        self.nbblue=self.coord3
                elif self.coordmotcible==self.coord4texte :
                        self.nbblue=self.coord4
                elif self.coordmotcible==self.coord5texte :
                        self.nbblue=self.coord5
                elif self.coordmotcible==self.coord6texte :
                        self.nbblue=self.coord6
                elif self.coordmotcible==self.coord7texte :
                        self.nbblue=self.coord7
                elif self.coordmotcible==self.coord8texte :
                        self.nbblue=self.coord8
                elif self.coordmotcible==self.coord9texte :
                        self.nbblue=self.coord9
                elif self.coordmotcible==self.coord10texte :
                        self.nbblue=self.coord10
                elif self.coordmotcible==self.coord11texte :
                        self.nbblue=self.coord11
                elif self.coordmotcible==self.coord12texte :
                        self.nbblue=self.coord12
                elif self.coordmotcible==self.coord13texte :
                        self.nbblue=self.coord13
                elif self.coordmotcible==self.coord14texte :
                        self.nbblue=self.coord14

                if self.coordmotdistracteur==self.coord0texte :
                        self.nbred=self.coord0
                elif self.coordmotdistracteur==self.coord1texte :
                        self.nbred=self.coord1
                elif self.coordmotdistracteur==self.coord2texte :
                        self.nbred=self.coord2
                elif self.coordmotdistracteur==self.coord3texte :
                        self.nbred=self.coord3
                elif self.coordmotdistracteur==self.coord4texte :
                        self.nbred=self.coord4
                elif self.coordmotdistracteur==self.coord5texte :
                        self.nbred=self.coord5
                elif self.coordmotdistracteur==self.coord6texte :
                        self.nbred=self.coord6
                elif self.coordmotdistracteur==self.coord7texte :
                        self.nbred=self.coord7
                elif self.coordmotdistracteur==self.coord8texte :
                        self.nbred=self.coord8
                elif self.coordmotdistracteur==self.coord9texte :
                        self.nbred=self.coord9
                elif self.coordmotdistracteur==self.coord10texte :
                        self.nbred=self.coord10
                elif self.coordmotdistracteur==self.coord11texte :
                        self.nbred=self.coord11
                elif self.coordmotdistracteur==self.coord12texte :
                        self.nbred=self.coord12
                elif self.coordmotdistracteur==self.coord13texte :
                        self.nbred=self.coord13
                elif self.coordmotdistracteur==self.coord14texte :
                        self.nbred=self.coord14
                
                self.tapp=time.perf_counter()

                self.fond0.bind('<Button-1>',self.clic)

        def clic(self,event):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFort.xls".format(nom,nom), "a")

                f.write('{}'.format(self.motcible))
                f.write('{}['.format(self.nbblue))
                f.write('{}'.format(self.motdistracteur))
                f.write('{}['.format(self.nbred))

                xclic=event.x
                yclic=event.y
                self.coordclicx=self.fond0.winfo_pointerx()
                self.coordclicy=self.fond0.winfo_pointery()
                print('clic x:{}'.format(self.coordclicx))
                print('clic y:{}'.format(self.coordclicy))
                if self.nbblue[0]<=xclic<=self.nbblue[2] and self.nbblue[1]<=yclic<=self.nbblue[3]:
                        self.NR=self.NR+1
                        print('Bien! NR={}'.format(self.NR))
                        f.write('Cible[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}['.format(self.coordclicy))

                        self.fond0.delete(self.racine0,self.pb)
                        self.progr=self.progr-1.66
                        self.pb = self.fond0.create_rectangle(self.w-100,self.progr,self.w-130,(self.h/2)-250, fill='white', width='1')
                        if self.NR%10==0:
                                self.gain=self.gain+1.00
                                if self.NR%50==0:
                                        winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav', winsound.SND_FILENAME | SND_ASYNC)

                        self.tclic=time.perf_counter()
                        self.RT=self.tclic-self.tapp
                        print('RT={}\n'.format(self.RT))
                        f.write('{}\n'.format(self.RT))
                        self.SRT=self.SRT+self.RT
                        if self.RT>self.RTmax:
                                self.RTmax=self.RT
                                if self.RT<self.RTmin:
                                        self.RTmin=self.RT
                        elif self.RT<self.RTmin:
                                        self.RTmin=self.RT

                elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
                        print('Distracteur touché!')
                        f.write('Distracteur[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}[\n'.format(self.coordclicy))
                        self.NED=self.NED+1
                        print('raté!NED={}\n'.format(self.NED))
                        self.initialize()
                else:
                        if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-225<yclic<=(self.h/2)-135 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-45<=yclic<=(self.h/2)+135) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+45 <=yclic<=(self.h/2)+135) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)-135<=yclic<=(self.h/2)+225) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+135<=yclic<=(self.h/2)+225):
                                print('Gris touché!')
                                f.write('Gris[')
                                f.write('{}['.format(self.coordclicx))
                                f.write('{}[\n'.format(self.coordclicy))
                                self.NEG=self.NEG+1
                                print('raté!NEG={}\n'.format(self.NEG))
                
                        else:
                                 print('A côté!')
                                 f.write('A cote[')
                                 f.write('{}['.format(self.coordclicx))
                                 f.write('{}[\n'.format(self.coordclicy))
                                 self.AC=self.AC+1
                                 print('raté!AC={}\n'.format(self.AC))

                self.hasard()

        def time(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_VerbaleFacileFort.xls".format(nom,nom), "a")

                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois de suite avec la souris pour continuer...', font='Arial 30', justify='center')
                print('THE END\n')
                print('Bonnes réponses:{}'.format(self.NR))
                f.write('\nBonnes réponses:[{}\n'.format(self.NR))
                print('Erreurs distracteur:{}'.format(self.NED))
                f.write('Erreurs distracteur:[{}\n'.format(self.NED))
                print('Erreurs gris:{}'.format(self.NEG))
                f.write('Erreurs gris:[{}\n'.format(self.NEG))
                print('Erreurs à côté:{}'.format(self.AC))
                f.write('Erreurs à côté:[{}\n'.format(self.AC))
                self.NE=self.NEG+self.NED+self.AC
                print('Erreurs totales:{}'.format(self.NE))
                f.write('Erreurs totales:[{}\n'.format(self.NE))
                self.total=self.NR+self.NE
                if self.total==0:
                        self.taux=0
                        self.RTmoy=0
                else:
                        self.taux=self.NR/self.total*100
                        self.RTmoy=self.SRT/self.NR
                print('Taux de réussite= %.2f'%self.taux)
                f.write('Taux de réussite=[ %.2f\n'%self.taux)
                gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 50', justify='center')
                print('RTmoy sec= %.3f'%self.RTmoy)
                f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
                print('RTmax sec= %.3f'%self.RTmax)
                f.write('RTmax sec=[ %.3f\n'%self.RTmax)
                print('RTmin sec= %.3f'%self.RTmin)
                f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)
		
                self.fond0.bind('<Triple-Button-1>',self.fin)
                
        def fin(self, event):
                self.racine0.destroy()
		                
ordre=[1,2,3,4,5,6,7,8]
ordreexercices=[]
ordretaches=[0]
while ordre!=[]:
        g = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_ordre.xls".format(nom,nom), "a")
        tirage=random.choice(ordre)
        #print('Tirage {}'.format(tirage))
        if tirage==1:
                ordre.remove(tirage)
                ordretaches.append(tirage)
                ordreexercices.append('Spatiale Facile Faible')
                g.write('Spatiale Facile Faible\n')
                #print('SPATIAL FACILE FAIBLE\n')
                if __name__ == '__main__':
                        app = SFf(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==2:
                 ordre.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Spatiale Facile Fort')
                 g.write('Spatiale Facile Forte\n')
                 #print('SPATIAL FACILE FORTE\n')
                 if __name__ == '__main__':
                        app = SFF(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==3:
                 ordre.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Spatiale Difficile Faible')
                 g.write('Spatiale Difficile Faible\n')
                 #print('SPATIAL DIFFICILE FAIBLE\n')
                 if __name__ == '__main__':
                        app = SDf(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==4:
                 ordre.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Spatiale Difficile Fort')
                 g.write('Spatiale Difficile Forte\n')
                 #print('SPATIAL DIFFICILE FORTE\n')
                 if __name__ == '__main__':
                        app = SDF(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        if tirage==5:
                ordre.remove(tirage)
                ordretaches.append(tirage)
                ordreexercices.append('Verbale Facile Facile')
                g.write('Verbale Facile Faible\n')
                #print('VERBAL FACILE FAIBLE\n')
                if __name__ == '__main__':
                        app = VFf(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==6:
                 ordre.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Verbale Facile Forte')
                 g.write('Verbale Facile Forte\n')
                 #print('VERBAL FACILE FORTE\n')
                 if __name__ == '__main__':
                        app = VFF(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==7:
                 ordre.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Verbale Difficile Faible')
                 g.write('Verbale Difficile Faible\n')
                 #print('VERBAL DIFFICILE FAIBLE\n')
                 if __name__ == '__main__':
                        app = VDf(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==8:
                 ordre.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Verbale Difficile Fort')
                 g.write('Verbale Difficile Forte\n')
                 #print('VERBAL DIFFICILE FORTE\n')
                 if __name__ == '__main__':
                        app = VDF(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()

print('ordre tâches : {}' .format(ordreexercices))
g = open("C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Sujets\{0}\{1}_ordre.xls".format(nom,nom), "a")
