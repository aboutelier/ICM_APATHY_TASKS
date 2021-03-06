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

		self.progr=self.w-1075

		self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jaugedouble.ppm')
		self.imagejauge=self.fond0.create_image(self.w-1075,(self.h/5), image = self.jauge, anchor = NW)
		self.pb = self.fond0.create_rectangle(self.w-292,(self.h/5),self.progr,(self.h/5)+95, fill='white', width='1')

		tkinter.Tk.__init__(self,parent)
		self.parent=parent

		self.coord0=[(self.w/2)-45, (self.h/2)-145, (self.w/2)+45, (self.h/2)-55]
		self.coord1=[(self.w/2)-45, (self.h/2)+25, (self.w/2)+45, (self.h/2)+115]
		self.coord2=[(self.w/2)-45, (self.h/2)+205, (self.w/2)+45, (self.h/2)+295]
		self.coord3=[(self.w/2)-135, (self.h/2)-55, (self.w/2)-45, (self.h/2)+35]
		self.coord4=[(self.w/2)+45, (self.h/2)-55, (self.w/2)+135, (self.h/2)+35]
		self.coord5=[(self.w/2)-225, (self.h/2)+25, (self.w/2)-135, (self.h/2)+115]
		self.coord6=[(self.w/2)+135, (self.h/2)+25, (self.w/2)+225, (self.h/2)+115]
		self.coord7=[(self.w/2)-135, (self.h/2)+115, (self.w/2)-45, (self.h/2)+205]
		self.coord8=[(self.w/2)+45, (self.h/2)+115, (self.w/2)+135, (self.h/2)+205]
		self.coord9=[(self.w/2)-225, (self.h/2)+205, (self.w/2)-135, (self.h/2)+295]
		self.coord10=[(self.w/2)+135, (self.h/2)+205, (self.w/2)+225, (self.h/2)+295]
		self.coord11=[(self.w/2)-315, (self.h/2)+115, (self.w/2)-225, (self.h/2)+205]
		self.coord12=[(self.w/2)+225, (self.h/2)+115, (self.w/2)+315, (self.h/2)+205]
		self.coord13=[(self.w/2)-405, (self.h/2)+205, (self.w/2)-315, (self.h/2)+295]
		self.coord14=[(self.w/2)+315, (self.h/2)+205, (self.w/2)+405, (self.h/2)+295]

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
		self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-200,text='Faites des combinaisons de\n4 cercles gris', font='Arial 20',justify='center')

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
		self.coordcouleur=[self.coord0, self.coord1, self.coord2,self.coord3, self.coord4, self.coord5, self.coord6, self.coord7, self.coord8, self.coord9, self.coord10, self.coord11, self.coord12, self.coord13, self.coord14]

		self.nbred1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred1)
		print('Red 1:{}'.format(self.nbred1))
		
		self.nbcoul1=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbcoul1)
		print('Blue 1:{}\n'.format(self.nbcoul1))
		
		self.nbred2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbred2)
		print('Red 2:{}'.format(self.nbred2))
		
		self.nbcoul2=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbcoul2)
		print('Blue 2:{}\n'.format(self.nbcoul2))
		
		self.nbcoul3=random.choice(self.coordcouleur)
		self.coordcouleur.remove(self.nbcoul3)
		print('Blue 3:{}\n'.format(self.nbcoul3))
		
		f.write('Coord distracteur bleu 1 {}\n'.format(self.nbcoul1))
		f.write('Coord distracteur bleu 2 {}\n'.format(self.nbcoul2))
		f.write('Coord distracteur bleu 3 {}\n'.format(self.nbcoul3))
		f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))
		
		f.write('[Coord Cercle 1[')
		f.write('Coord Cercle 2[')
		f.write('Coord Cercle 3[')
		f.write('Coord Cercle 4[')
		f.write('Combi[')
		f.write('RT\n')

		self.ellipsered1=self.fond0.create_oval(self.nbred1, fill='red', width='5')
		self.ellipseblue1=self.fond0.create_oval(self.nbcoul1, fill='blue', width='5')
		self.ellipsered2=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue2=self.fond0.create_oval(self.nbcoul2, fill='blue', width='5')
		self.ellipseblue3=self.fond0.create_oval(self.nbcoul3, fill='blue', width='5')
		
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
		self.ellipseblue1=self.fond0.create_oval(self.nbcoul1, fill='blue', width='5')
		self.ellipsered2=self.fond0.create_oval(self.nbred2, fill='red', width='5')
		self.ellipseblue2=self.fond0.create_oval(self.nbcoul2, fill='blue', width='5')
		self.ellipseblue3=self.fond0.create_oval(self.nbcoul3, fill='blue', width='5')

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
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-155<=self.clicy<=(self.h/2)-65:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+35<=self.clicy<=(self.h/2)+115:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-55<=self.clicy<=(self.h/2)+35:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-55<=self.clicy<=(self.h/2)+35:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+25<=self.clicy<=(self.h/2)+115:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+25<=self.clicy<=(self.h/2)+115:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)+45 and (self.h/2)+115<=self.clicy<=(self.h/2)+205:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+115 <=self.clicy<=(self.h/2)+205:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+115<=self.clicy<=(self.h/2)+205:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+115<=self.clicy<=(self.h/2)+205:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_SpatialeDifficile.xls".format(nom,nom), "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
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
		self.pb = self.fond0.create_rectangle(self.w-292,(self.h/5),self.progr,(self.h/5)+95, fill='white', width='1')
		
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
		elif self.nbcoul1[0]<=self.clicx<=self.nbcoul1[2] and self.nbcoul1[1]<=self.clicy<=self.nbcoul1[3] or self.nbcoul2[0]<=self.clicx<=self.nbcoul2[2] and self.nbcoul2[1]<=self.clicy<=self.nbcoul2[3] or self.nbcoul3[0]<=self.clicx<=self.nbcoul3[2] and self.nbcoul3[1]<=self.clicy<=self.nbcoul3[3]:
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
		end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
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
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		#gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu', font='Arial 50', justify='center')
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

                self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
                self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Hetero.xls".format(nom,nom), "a")
                f.write("\nHETERO GENEREE\n\n")
                print('HETERO GENEREE')

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

                self.NRvert=0
                self.NRbleu=0
                self.NRrouge=0
                self.NRjaune=0

                self.troplent=0

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
                self.SRTerreur=0
                self.RTmax=0
                self.RTmin=360

                self.progr=self.w-292

                self.pb = self.fond0.create_rectangle(self.w-292,(self.h/5),self.progr,(self.h/5)+95, fill='white', width='1')

                self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jaugedouble.ppm')
                self.imagejauge=self.fond0.create_image(self.w-1075,(self.h/5), image = self.jauge, anchor = NW)

                tkinter.Tk.__init__(self,parent)
                self.parent=parent

                self.coord0=[(self.w/2)-45, (self.h/2)-145, (self.w/2)+45, (self.h/2)-55]#rouge
                self.coord1=[(self.w/2)-45, (self.h/2)+25, (self.w/2)+45, (self.h/2)+115]#bleu
                self.coord2=[(self.w/2)-45, (self.h/2)+205, (self.w/2)+45, (self.h/2)+295]#jaune
                self.coord3=[(self.w/2)-135, (self.h/2)-55, (self.w/2)-45, (self.h/2)+35]#rouge
                self.coord4=[(self.w/2)+45, (self.h/2)-55, (self.w/2)+135, (self.h/2)+35]#vert
                self.coord5=[(self.w/2)-225, (self.h/2)+25, (self.w/2)-135, (self.h/2)+115]#rouge
                self.coord6=[(self.w/2)+135, (self.h/2)+25, (self.w/2)+225, (self.h/2)+115]#vert
                self.coord7=[(self.w/2)-135, (self.h/2)+115, (self.w/2)-45, (self.h/2)+205]#bleu
                self.coord8=[(self.w/2)+45, (self.h/2)+115, (self.w/2)+135, (self.h/2)+205]#bleu
                self.coord9=[(self.w/2)-225, (self.h/2)+205, (self.w/2)-135, (self.h/2)+295]#jaune
                self.coord10=[(self.w/2)+135, (self.h/2)+205, (self.w/2)+225, (self.h/2)+295]#jaune
                self.coord11=[(self.w/2)-315, (self.h/2)+115, (self.w/2)-225, (self.h/2)+205]#rouge
                self.coord12=[(self.w/2)+225, (self.h/2)+115, (self.w/2)+315, (self.h/2)+205]#vert
                self.coord13=[(self.w/2)-405, (self.h/2)+205, (self.w/2)-315, (self.h/2)+295]#jaune
                self.coord14=[(self.w/2)+315, (self.h/2)+205, (self.w/2)+405, (self.h/2)+295]#vert

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
                self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-200,text='Touchez le cercle coloré',fill='black', font='Arial 20',justify='center')

                self.fond0.bind('<Button-1>',self.attente)

        def attente(self,event):
                self.hasard()
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
                self.lancementsec=self.racine0.after(1, self.seclimite)
                
        def startlimite2(self):
                self.fond0.delete(self.racine0,self.pb)
                self.progr=self.progr-10
                self.pb = self.fond0.create_rectangle(self.w-292,(self.h/5),self.progr,(self.h/5)+95, fill='white', width='1')
                self.troplent=self.troplent+1
                
                if self.troplent%10==0:
                        winsound.PlaySound('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\BOUH.wav', winsound.SND_FILENAME | SND_ASYNC)
                self.startlimite1()

        def seclimite(self):
                self.tempssecondeslimite=self.tempssecondeslimite+1
                if self.tempssecondeslimite==810:#Temps pour chaque clic + 50ms (810 sains/1370 DFT)
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

                self.coordcouleur=[self.coord0, self.coord1, self.coord2,self.coord3, self.coord4, self.coord5, self.coord6, self.coord7, self.coord8, self.coord9, self.coord10, self.coord11, self.coord12, self.coord13, self.coord14]

                #self.nbred=random.choice(self.coordcouleur)
                #self.couleur.remove(self.nbred)
                #print('Red 1:{}'.format(self.nbred))
                self.nbcoul=random.choice(self.coordcouleur)
                print('Coul:{}'.format(self.nbcoul))
                
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

                if self.nbcoul==self.coord1 or self.nbcoul==self.coord7 or self.nbcoul==self.coord8:
                        self.ellipseblue=self.fond0.create_oval(self.nbcoul, fill='blue', width='5')
                        
                if self.nbcoul==self.coord0 or self.nbcoul==self.coord3 or self.nbcoul==self.coord5 or self.nbcoul==self.coord11:
                        self.ellipsered=self.fond0.create_oval(self.nbcoul, fill='red', width='5')
                        
                if self.nbcoul==self.coord2 or self.nbcoul==self.coord9 or self.nbcoul==self.coord10 or self.nbcoul==self.coord13:
                        self.ellipseblue=self.fond0.create_oval(self.nbcoul, fill='yellow', width='5')
                        
                if self.nbcoul==self.coord4 or self.nbcoul==self.coord6 or self.nbcoul==self.coord12 or self.nbcoul==self.coord14:
                        self.ellipsered=self.fond0.create_oval(self.nbcoul, fill='green', width='5')

                self.tapp=time.perf_counter()

                self.fond0.bind('<Button-1>',self.clic)

        def clic(self,event):
                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Hetero.xls".format(nom,nom), "a")
                f.write('{}'.format(self.nbcoul))
                #f.write('{}['.format(self.nbred))

                xclic=event.x
                yclic=event.y
                self.coordclicx=self.fond0.winfo_pointerx()
                self.coordclicy=self.fond0.winfo_pointery()
                print('clic x:{}'.format(self.coordclicx))
                print('clic y:{}'.format(self.coordclicy))
                if self.nbcoul[0]<=xclic<=self.nbcoul[2] and self.nbcoul[1]<=yclic<=self.nbcoul[3]:
                        self.NR=self.NR+1
                        print('Bien! NR={}'.format(self.NR))
                        f.write('Cible[')
                        f.write('{}['.format(self.coordclicx))
                        f.write('{}['.format(self.coordclicy))

                        self.lim=0
                        self.tempssecondeslimite=0
                        
                        self.tclic=time.perf_counter()
                        self.RT=self.tclic-self.tapp
                        print('RT={}\n'.format(self.RT))
                        f.write('{}\n'.format(self.RT))
                        self.SRT=self.SRT+self.RT

                        if self.nbcoul==self.coord1 or self.nbcoul==self.coord7 or self.nbcoul==self.coord8:
                                self.NRbleu=self.NRbleu+1
                        if self.nbcoul==self.coord0 or self.nbcoul==self.coord3 or self.nbcoul==self.coord5 or self.nbcoul==self.coord11:
                                self.NRrouge=self.NRrouge+1
                        if self.nbcoul==self.coord2 or self.nbcoul==self.coord9 or self.nbcoul==self.coord10 or self.nbcoul==self.coord13:
                                self.NRjaune=self.NRjaune+1
                        if self.nbcoul==self.coord4 or self.nbcoul==self.coord6 or self.nbcoul==self.coord12 or self.nbcoul==self.coord14:
                                self.NRvert=self.NRvert+1

                        if self.RT>self.RTmax:
                                self.RTmax=self.RT
                                if self.RT<self.RTmin:
                                        self.RTmin=self.RT
                        elif self.RT<self.RTmin:
                                        self.RTmin=self.RT

#                elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
#                        print('Rouge touché!')
#                        f.write('Distracteur[')
#                        f.write('{}['.format(self.coordclicx))
#                        f.write('{}['.format(self.coordclicy))
#                        self.tclic=time.perf_counter()
#                        self.RTerreur=self.tclic-self.tapp
#                        print('RT erreur={}\n'.format(self.RTerreur))
#                        f.write('{}\n'.format(self.RTerreur))
#                        self.SRTerreur=self.SRTerreur+self.RTerreur
#                        
#                        self.NER=self.NER+1
#                        print('raté!NER={}\n'.format(self.NER))
#                        self.initialize()
                else:
                        if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-155<yclic<=(self.h/2)-65 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)+25<=yclic<=(self.h/2)+115) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+205<=yclic<=(self.h/2)+295) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-55<=yclic<=(self.h/2)+35) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-55<=yclic<=(self.h/2)+35) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+25<=yclic<=(self.h/2)+115) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+25<=yclic<=(self.h/2)+115) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)+115<=yclic<=(self.h/2)+205) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+115 <=yclic<=(self.h/2)+205) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+205<=yclic<=(self.h/2)+295) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+205<=yclic<=(self.h/2)+295) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+115<=yclic<=(self.h/2)+205) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+115<=yclic<=(self.h/2)+205) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)+205<=yclic<=(self.h/2)+295) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+205<=yclic<=(self.h/2)+295):
                                print('Gris touché!')
                                f.write('Gris[')
                                f.write('{}['.format(self.coordclicx))
                                f.write('{}['.format(self.coordclicy))
                                self.tclic=time.perf_counter()
                                self.RTerreur=self.tclic-self.tapp
                                print('RT erreur={}\n'.format(self.RTerreur))
                                f.write('{}\n'.format(self.RTerreur))
                                self.SRTerreur=self.SRTerreur+self.RTerreur
                                self.NEG=self.NEG+1
                                print('raté!NEG={}\n'.format(self.NEG))
                
                        else:
                                 print('A côté!')
                                 f.write('A cote[')
                                 f.write('{}['.format(self.coordclicx))
                                 f.write('{}['.format(self.coordclicy))
                                 self.tclic=time.perf_counter()
                                 self.RTerreur=self.tclic-self.tapp
                                 print('RT erreur={}\n'.format(self.RTerreur))
                                 f.write('{}\n'.format(self.RTerreur))
                                 self.SRTerreur=self.SRTerreur+self.RTerreur
                                 self.AC=self.AC+1
                                 print('raté!AC={}\n'.format(self.AC))

                self.hasard()

        def time(self):
                self.racine0.after_cancel(self.lancementsec)
                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Hetero.xls".format(nom,nom), "a")                
                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                
                
                print('THE END\n')
                end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
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
                print('Nombre de réponses:{}'.format(self.total))
                f.write('Nombre de réponses:[{}\n'.format(self.total))
                if self.total==0:
                        self.taux=0
                        self.RTmoyreussi=180
                        self.RTmoyerreur=0
                        self.RTmoytot=180
                else:
                        self.taux=self.NR/self.total*100
                        if self.taux==0:
                                self.RTmoyreussi=0
                        else:
                                self.RTmoyreussi=self.SRT/self.NR
                                
                        if self.NE==0:
                                self.RTmoyerreur=0
                                self.RTmoytot=self.RTmoyreussi
                        else:
                                self.RTmoyerreur=self.SRTerreur/self.NE
                                self.RTmoytot=(self.SRT+self.SRTerreur)/(self.NR+self.NE)
                print('Taux de réussite= %.2f'%self.taux)
                f.write('Taux de réussite=[ %.2f\n'%self.taux)
                #gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu.', font='Arial 50', justify='center')
                print('RTmoy reussi= %.3f'%self.RTmoyreussi)
                f.write('RTmoy reussi=[ %.3f\n'%self.RTmoyreussi)
                print('RTmoy erreur= %.3f'%self.RTmoyerreur)
                f.write('RTmoy erreur=[ %.3f\n'%self.RTmoyerreur)
                print('RTmoy tot= %.3f'%self.RTmoytot)
                f.write('RTmoy tot=[ %.3f\n'%self.RTmoytot)
                print('RTmax= %.3f'%self.RTmax)
                f.write('RTmax=[ %.3f\n'%self.RTmax)
                print('RTmin= %.3f'%self.RTmin)
                f.write('RTmin=[ %.3f\n\n'%self.RTmin)
                print('Bonnes bleues:{}'.format(self.NRbleu))
                f.write('\nBonnes bleues:[{}\n'.format(self.NRbleu))
                print('Bonnes rouges:{}'.format(self.NRrouge))
                f.write('\nBonnes rouges:[{}\n'.format(self.NRrouge))
                print('Bonnes jaunes:{}'.format(self.NRjaune))
                f.write('\nBonnes jaunes:[{}\n'.format(self.NRjaune))
                print('Bonnes vertes:{}'.format(self.NRvert))
                f.write('\nBonnes vertes:[{}\n'.format(self.NRvert))

                self.after(15000,self.fin)
                
        def fin(self):
                self.racine0.destroy()
#######################################################################################################################################################################
class auto(tkinter.Tk):
        def __init__(self,parent):
                self.racine0=tkinter.Tk()
                self.racine0.attributes('-fullscreen',True)
                self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')

                #self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
                #self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                f.write("\nAUTO GENEREEn\n")
                print('AUTO GENEREE')

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

                self.NRvert=0
                self.NRbleu=0
                self.NRrouge=0
                self.NRjaune=0

                premierclic=0

                self.troplent=0

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
                self.SRTacote=0
                self.RTmax=0
                self.RTmin=360

                self.progr=self.w-292

                self.pb = self.fond0.create_rectangle(self.w-292,(self.h/5),self.progr,(self.h/5)+95, fill='white', width='1')

                self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jaugedouble.ppm')
                self.imagejauge=self.fond0.create_image(self.w-1075,(self.h/5), image = self.jauge, anchor = NW)

                tkinter.Tk.__init__(self,parent)
                self.parent=parent

                self.coord0=[(self.w/2)-45, (self.h/2)-145, (self.w/2)+45, (self.h/2)-55]#rouge
                self.coord1=[(self.w/2)-45, (self.h/2)+25, (self.w/2)+45, (self.h/2)+115]#bleu
                self.coord2=[(self.w/2)-45, (self.h/2)+205, (self.w/2)+45, (self.h/2)+295]#jaune
                self.coord3=[(self.w/2)-135, (self.h/2)-55, (self.w/2)-45, (self.h/2)+35]#rouge
                self.coord4=[(self.w/2)+45, (self.h/2)-55, (self.w/2)+135, (self.h/2)+35]#vert
                self.coord5=[(self.w/2)-225, (self.h/2)+25, (self.w/2)-135, (self.h/2)+115]#rouge
                self.coord6=[(self.w/2)+135, (self.h/2)+25, (self.w/2)+225, (self.h/2)+115]#vert
                self.coord7=[(self.w/2)-135, (self.h/2)+115, (self.w/2)-45, (self.h/2)+205]#bleu
                self.coord8=[(self.w/2)+45, (self.h/2)+115, (self.w/2)+135, (self.h/2)+205]#bleu
                self.coord9=[(self.w/2)-225, (self.h/2)+205, (self.w/2)-135, (self.h/2)+295]#jaune
                self.coord10=[(self.w/2)+135, (self.h/2)+205, (self.w/2)+225, (self.h/2)+295]#jaune
                self.coord11=[(self.w/2)-315, (self.h/2)+115, (self.w/2)-225, (self.h/2)+205]#rouge
                self.coord12=[(self.w/2)+225, (self.h/2)+115, (self.w/2)+315, (self.h/2)+205]#vert
                self.coord13=[(self.w/2)-405, (self.h/2)+205, (self.w/2)-315, (self.h/2)+295]#jaune
                self.coord14=[(self.w/2)+315, (self.h/2)+205, (self.w/2)+405, (self.h/2)+295]#vert

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

                #self.start=self.fond0.create_text(self.w/2,self.h/2,text="Touchez l'écran pour démarrer", font=('Arial 60 bold'),fill='green')
                #self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-200,text='Touchez le cercle coloré',fill='black', font='Arial 20',justify='center')

                self.attente()

        def attente(self):
                self.initialize()
                self.startchrono()
                self.startlimite1()
                
        def startlimite1(self):
                self.lancementsec=self.racine0.after(1, self.seclimite)
                
        def startlimite2(self):
                self.fond0.delete(self.racine0,self.pb)
                self.progr=self.progr-10
                self.pb = self.fond0.create_rectangle(self.w-292,(self.h/5),self.progr,(self.h/5)+95, fill='white', width='1')
                self.troplent=self.troplent+1
                
                self.startlimite1()

        def seclimite(self):
                self.tempssecondeslimite=self.tempssecondeslimite+1
                if self.tempssecondeslimite==810:#Temps pour chaque clic + 50ms (810 sains/1370 DFT)
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

        def initialize(self):
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

                #if self.nbcoul==self.coord1 or self.nbcoul==self.coord7 or self.nbcoul==self.coord8:
                #        self.ellipseblue=self.fond0.create_oval(self.nbcoul, fill='blue', width='5')
                        
                #if self.nbcoul==self.coord0 or self.nbcoul==self.coord3 or self.nbcoul==self.coord5 or self.nbcoul==self.coord11:
                #        self.ellipsered=self.fond0.create_oval(self.nbcoul, fill='red', width='5')
                        
                #if self.nbcoul==self.coord2 or self.nbcoul==self.coord9 or self.nbcoul==self.coord10 or self.nbcoul==self.coord13:
                #        self.ellipseblue=self.fond0.create_oval(self.nbcoul, fill='yellow', width='5')
                        
                #if self.nbcoul==self.coord4 or self.nbcoul==self.coord6 or self.nbcoul==self.coord12 or self.nbcoul==self.coord14:
                #        self.ellipsered=self.fond0.create_oval(self.nbcoul, fill='green', width='5')

                self.tapp=time.perf_counter()

                self.fond0.bind('<Button-1>',self.clic)

        def clic(self,event):
                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                #f.write('{}'.format(self.nbcoul))
                #f.write('{}['.format(self.nbred))

                self.clicx=event.x
                self.clicy=event.y
                self.coordclicx=self.fond0.winfo_pointerx()
                self.coordclicy=self.fond0.winfo_pointery()
                print('clic x:{}'.format(self.coordclicx))
                print('clic y:{}'.format(self.coordclicy))
                if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-155<=self.clicy<=(self.h/2)-65:
                        self.clicn= self.coord0
                        self.ellipse0=self.fond0.create_oval(self.coord0, fill='red', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicrouge()
                elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+35<=self.clicy<=(self.h/2)+115:
                        self.clicn= self.coord1
                        self.ellipse1=self.fond0.create_oval(self.coord1, fill='blue', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicbleu()
                elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
                        self.clicn= self.coord2
                        self.ellipse2=self.fond0.create_oval(self.coord2, fill='yellow', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicjaune()
                elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-55<=self.clicy<=(self.h/2)+35:
                        self.clicn= self.coord3
                        self.ellipse3=self.fond0.create_oval(self.coord3, fill='red', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicrouge()
                elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-55<=self.clicy<=(self.h/2)+35:
                        self.clicn= self.coord4
                        self.ellipse4=self.fond0.create_oval(self.coord4, fill='green', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicvert()
                elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+25<=self.clicy<=(self.h/2)+115:
                        self.clicn= self.coord5
                        self.ellipse5=self.fond0.create_oval(self.coord5, fill='red', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicrouge()
                elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+25<=self.clicy<=(self.h/2)+115:
                        self.clicn= self.coord6
                        self.ellipse6=self.fond0.create_oval(self.coord6, fill='green', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicvert()
                elif (self.w/2)-135<=self.clicx<=(self.w/2)+45 and (self.h/2)+115<=self.clicy<=(self.h/2)+205:
                        self.clicn= self.coord7
                        self.ellipse7=self.fond0.create_oval(self.coord7, fill='blue', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicbleu()
                elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+115 <=self.clicy<=(self.h/2)+205:
                        self.clicn= self.coord8
                        self.ellipse8=self.fond0.create_oval(self.coord8, fill='blue', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicbleu()
                elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
                        self.clicn= self.coord9
                        self.ellipse9=self.fond0.create_oval(self.coord9, fill='yellow', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicjaune()
                elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
                        self.clicn= self.coord10
                        self.ellipse10=self.fond0.create_oval(self.coord10, fill='yellow', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicjaune()
                elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+115<=self.clicy<=(self.h/2)+205:
                        self.clicn= self.coord11
                        self.ellipse11=self.fond0.create_oval(self.coord11, fill='red', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicrouge()
                elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+115<=self.clicy<=(self.h/2)+205:
                        self.clicn= self.coord12
                        self.ellipse12=self.fond0.create_oval(self.coord12, fill='green', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicvert()
                elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
                        self.clicn= self.coord13
                        self.ellipse13=self.fond0.create_oval(self.coord13, fill='yellow', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicjaune()
                elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+205<=self.clicy<=(self.h/2)+295:
                        self.clicn= self.coord14
                        self.ellipse14=self.fond0.create_oval(self.coord14, fill='green', width='5')
                        f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                        f.write('{}'.format(self.clicn))
                        self.clicvert()
                else:
                        self.acote()

        def clicrouge(self):
                self.NRrouge=self.NRrouge+1
                self.reactionreussi()

        def clicbleu(self):
                self.NRbleu=self.NRbleu+1
                self.reactionreussi()

        def clicvert(self):
                self.NRvert=self.NRvert+1
                self.reactionreussi()

        def clicjaune(self):
                self.NRjaune=self.NRjaune+1
                self.reactionreussi()

        def acote(self):
                self.AC=self.AC+1
                self.reactionacote()

        def reactionreussi(self):
                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                self.tclic=time.perf_counter()
                self.RT=self.tclic-self.tapp
                print('RT sec={}\n'.format(self.RT))
                f.write('{}\n'.format(self.RT))
                self.SRT=self.SRT+self.RT

                self.NR=self.NR+1
                self.tempssecondeslimite=0
                
                if self.RT>self.RTmax:
                        self.RTmax=self.RT
                        if self.RT<self.RTmin:
                                self.RTmin=self.RT
                elif self.RT<self.RTmin:
                        self.RTmin=self.RT

                if self.premierclic==0:
                        self.RTpremierclic=self.RT
                        self.premierclic=1
                        
                self.after(100, self.initialize)

        def reactionacote(self):
                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")
                self.AC=self.AC+1
                
                self.tclic=time.perf_counter()
                self.RTacote=self.tclic-self.tapp
                print('RT sec={}\n'.format(self.RTacote))
                f.write('{}\n'.format(self.RTacote))
                self.SRTacote=self.SRTacote+self.RTacote

                if self.premierclic==0:
                        self.RTpremierclic=self.RT
                        self.premierclic=1
                        
                self.after(100, self.initialize)
                
        def time(self):
                self.racine0.after_cancel(self.lancementsec)
                f = open("C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\SujetsAutoHetero\{0}\{1}_Auto.xls".format(nom,nom), "a")                
                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                
                
                print('THE END\n')
                end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
                print('Bonnes réponses:{}'.format(self.NR))
                f.write('\nBonnes réponses:[{}\n'.format(self.NR))
                print('Erreurs à côté:{}'.format(self.AC))
                f.write('Erreurs à côté:[{}\n'.format(self.AC))
                self.total=self.NR+self.AC
                print('Nombre de réponses:{}'.format(self.total))
                f.write('Nombre de réponses:[{}\n'.format(self.total))
                if self.total==0:
                        self.taux=0
                        self.RTmoyreussi=180
                        self.RTmoyerreur=0
                        self.RTmoytot=180
                else:
                        self.taux=self.NR/self.total*100
                        if self.taux==0:
                                self.RTmoyreussi=0
                        else:
                                self.RTmoyreussi=self.SRT/self.NR
                                
                        if self.AC==0:
                                self.RTmoyerreur=0
                                self.RTmoytot=self.RTmoyreussi
                        else:
                                self.RTmoyerreur=self.SRTacote/self.AC
                                self.RTmoytot=(self.SRT+self.SRTacote)/(self.NR+self.AC)
                print('Taux de réussite= %.2f'%self.taux)
                f.write('Taux de réussite=[ %.2f\n'%self.taux)
                #gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu.', font='Arial 50', justify='center')
                print('RTmoy reussi= %.3f'%self.RTmoyreussi)
                f.write('RTmoy reussi=[ %.3f\n'%self.RTmoyreussi)
                print('RTmoy a cote= %.3f'%self.RTmoyerreur)
                f.write('RTmoy a cote=[ %.3f\n'%self.RTmoyerreur)
                print('RTmoy tot= %.3f'%self.RTmoytot)
                f.write('RTmoy tot=[ %.3f\n'%self.RTmoytot)
                print('RTmax= %.3f'%self.RTmax)
                f.write('RTmax=[ %.3f\n'%self.RTmax)
                print('RTmin= %.3f'%self.RTmin)
                f.write('RTmin=[ %.3f\n\n'%self.RTmin)
                print('Bonnes bleues:{}'.format(self.NRbleu))
                f.write('\nBonnes bleues:[{}\n'.format(self.NRbleu))
                print('Bonnes rouges:{}'.format(self.NRrouge))
                f.write('\nBonnes rouges:[{}\n'.format(self.NRrouge))
                print('Bonnes jaunes:{}'.format(self.NRjaune))
                f.write('\nBonnes jaunes:[{}\n'.format(self.NRjaune))
                print('Bonnes vertes:{}'.format(self.NRvert))
                f.write('\nBonnes vertes:[{}\n'.format(self.NRvert))

                self.after(15000,self.fin)
                
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


