import tkinter
from tkinter import *
import winsound
from winsound import *
import random
from timeit import time
import math
import os

nom = input("Nom sujet :")
os.mkdir('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{}'.format(nom))
########################################################################################################################################################################        
class SD(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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

		self.progr=self.w-925

		self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)
		self.pb = self.fond0.create_rectangle(self.progr,(self.h/1.2),self.w-425,(self.h/1.2)+30, fill='white', width='1')

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
		self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-300,text='Faites des combinaisons de\n4 cercles gris', font='Arial 20',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(120000, self.time)
		self.after(90000, self.debutchrono)

	def debutchrono(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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

		self.ellipsered1=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue1=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		self.ellipsered2=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue2=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
		self.ellipseblue3=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')
		
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
		
		self.fond0.delete(self.racine0,self.ellipsered1)
		self.fond0.delete(self.racine0,self.ellipseblue1)
		self.fond0.delete(self.racine0,self.ellipsered2)
		self.fond0.delete(self.racine0,self.ellipseblue2)
		self.fond0.delete(self.racine0,self.ellipseblue3)
		
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

		self.ellipsered1=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue1=self.fond0.create_oval(self.nbblue1, fill='blue', width='5')
		self.ellipsered2=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue2=self.fond0.create_oval(self.nbblue2, fill='blue', width='5')
		self.ellipseblue3=self.fond0.create_oval(self.nbblue3, fill='blue', width='5')

		self.tapp=time.perf_counter()

		self.fond0.bind('<ButtonPress-1>',self.clic)         

	def clic(self,event):
		self.clicx=event.x
		self.clicy=event.y
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
						
		self.gain=self.gain+0.10

		print('RT sec={}\n'.format(self.RT))
		f.write('{}\n'.format(self.RT))
		self.SRT=self.SRT+self.RT
		
		self.fond0.delete(self.racine0,self.pb)	
		self.progr=self.progr+2.50
		self.pb = self.fond0.create_rectangle(self.progr,(self.h/1.2),self.w-425,(self.h/1.2)+30, fill='white', width='1')
		
		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav',winsound.SND_FILENAME | SND_ASYNC)
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
				self.tclic=time.perf_counter()
				self.RTdejafait=self.tclic-self.tapp
				self.SRTdejafait=self.SRTdejafait+self.RTdejafait
				self.after(100,self.dejafait)
			else:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			
	def erreurbleu(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
		self.ND=self.ND+1
		f.write('[Combi déjà faite[')
		print('Déjà fait:{}\n'.format(self.ND))
		print('RT deja fait sec={}\n'.format(self.RTdejafait))
		f.write('{}\n'.format(self.RTdejafait))
		self.initialize()

	def acote(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		
		
		print('THE END\n')
		end=self.fond0.create_text(self.w/2,self.h/2,text='FIN\nAttendez pour la suite...', font='Arial 30', justify='center')
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
		self.total=self.NR+self.NET
		print('Nombre de réponses:{}'.format(self.total))
		f.write('Nombre de réponses:[{}\n'.format(self.total))
		if self.total==0:
			self.taux=0
			self.RTmoyreussi=180
			self.RTmoydejafait=0
			self.RTmoytot=180
		else:
			self.taux=self.NR/self.total*100
			self.RTmoyreussi=self.SRT/self.NR
			if self.ND==0:
				self.RTmoydejafait=0
				self.RTmoytot=self.RTmoyreussi
			else:
				self.RTmoydejafait=self.SRTdejafait/self.ND
				self.RTmoytot=(self.SRT+self.SRTdejafait)/(self.ND+self.NR)
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu', font='Arial 50', justify='center')
		print('RTmoy reussi sec= %.3f'%self.RTmoyreussi)
		f.write('RTmoy reussi sec=[ %.3f\n'%self.RTmoyreussi)
		print('RTmoy deja fait sec= %.3f'%self.RTmoydejafait)
		f.write('RTmoy deja fait sec=[ %.3f\n'%self.RTmoydejafait)
		print('RTmoy tot sec= %.3f'%self.RTmoytot)
		f.write('RTmoy tot sec=[ %.3f\n'%self.RTmoytot)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)

		self.after(15000,self.fin)
		
	def fin(self):
		self.racine0.destroy()

########################################################################################################################################################################        
class hetero(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.imagepieces=self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
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

		self.metro=0

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
		if self.metro==0:
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		
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
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		self.AC=self.AC+1
		print('A côté:{}\n'.format(self.AC))
		self.combinaison.append('A côté')
		self.reaction.append('X')
		self.hasardbleu1()

	def erreurgris(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a") 

		self.CG=self.CG+1
		print('Clic gris:{}\n'.format(self.CG))
		self.combinaison.append('Clic gris')
		self.reaction.append('X')
		self.hasardbleu1()	
		
	def memecercle(self):
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
		self.MC=self.MC+1
		print('clic sur un même cercle:{}\n'.format(self.MC))
		self.combinaison.append('Même cercle')
		self.reaction.append('X')
		self.hasardbleu1()

	def time(self):
		self.metro=1
		f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_HétéroGénéré.xls".format(nom,nom), "a")
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
		
	def fin(self):
		self.racine0.destroy()
########################################################################################################################################################################        
class auto(tkinter.Tk):
    def __init__(self,parent):
        self.racine0=tkinter.Tk()
        self.racine0.attributes('-fullscreen',True)
        self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
        self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
        self.fond0.pack(fill='both')

        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
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
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        self.coordclicx=self.fond0.winfo_pointerx()
        self.coordclicy=self.fond0.winfo_pointery()
        print('clic x:{}'.format(self.coordclicx))
        print('clic y:{}'.format(self.coordclicy))
        if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
            self.clicnauto= self.coord0
            self.ellipseclic0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicnauto= self.coord1
            self.ellipseclic1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord2
            self.ellipseclic2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
            self.clicnauto= self.coord3
            self.ellipseclic3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
            self.clicnauto= self.coord4
            self.ellipseclic4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicnauto= self.coord5
            self.ellipseclic5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
            self.clicnauto= self.coord6
            self.ellipseclic6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord7
            self.ellipseclic7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord8
            self.ellipseclic8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord9
            self.ellipseclic9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord10
            self.ellipseclic10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord11
            self.ellipseclic11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
            self.clicnauto= self.coord12
            self.ellipseclic12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord13
            self.ellipseclic13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
            self.clicnauto= self.coord14
            self.ellipseclic14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
            f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
            f.write('{}'.format(self.clicnauto))
            self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
        else:
            self.acoteauto()

    def reussiteauto(self):
        self.combiauto.append(self.combauto)
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        
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
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
        self.NDauto=self.NDauto+1
        f.write('[Combi déjà faite\n')
        print('Déjà fait:{}\n'.format(self.NDauto))
        self.initializeauto()

    def acoteauto(self):
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
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
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
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
        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_AutoGénéré.xls".format(nom,nom), "a")
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
        
    def fin(self):
        self.racine0.destroy()

ordre=0
ordre2=[1,2]
ordreexercices=[]
ordretaches=[0]
while ordre2!=[]:
        g = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_ordre.xls".format(nom,nom), "a")
        tirage=random.choice(ordre2)
        #print('Tirage {}'.format(tirage))
        if ordre==0:
                ordretaches.append(ordre)
                ordreexercices.append('Spatiale Difficile')
                g.write('Spatiale Difficile\n')
                tirage=random.choice(ordre2)
                ordre=2
                #print('SPATIAL DIFFICILE\n')
                if __name__ == '__main__':
                        app = SD(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        if tirage==1:
                ordre2.remove(tirage)
                ordretaches.append(tirage)
                ordreexercices.append('Hétéro Généré')
                g.write('Hétéro Généré\n')
                #print('Hétéro Généré\n')
                if __name__ == '__main__':
                        app = hetero(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif tirage==2:
                 ordre2.remove(tirage)
                 ordretaches.append(tirage)
                 ordreexercices.append('Auto Généré')
                 g.write('Auto Généré\n')
                 #print('Auto Généré\n')
                 if __name__ == '__main__':
                        app = auto(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()


print('ordre tâches : {}' .format(ordreexercices))
g = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_ordre.xls".format(nom,nom), "a")


