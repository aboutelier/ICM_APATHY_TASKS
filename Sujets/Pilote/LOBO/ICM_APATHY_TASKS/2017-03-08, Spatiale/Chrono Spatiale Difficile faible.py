import tkinter
from tkinter import *
import winsound
from winsound import *
import math
from timeit import time
import random
class SDf(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
						
		self.gain=self.gain+0.10

		self.tclic=time.perf_counter()
		self.RT=self.tclic-self.tapp
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
			
		self.after(100,self.initialize)

	def verifcercle(self):
		if self.clicn in self.comb:
			self.memecercle()
		elif self.nbblue1[0]<=self.clicx<=self.nbblue1[2] and self.nbblue1[1]<=self.clicy<=self.nbblue1[3] or self.nbblue2[0]<=self.clicx<=self.nbblue2[2] and self.nbblue2[1]<=self.clicy<=self.nbblue2[3] or self.nbblue3[0]<=self.clicx<=self.nbblue3[2] and self.nbblue3[1]<=self.clicy<=self.nbblue3[3]:
			self.erreurbleu()
		elif self.nbred1[0]<=self.clicx<=self.nbred1[2] and self.nbred1[1]<=self.clicy<=self.nbred1[3] or self.nbred2[0]<=self.clicx<=self.nbred2[2] and self.nbred2[1]<=self.clicy<=self.nbred2[3]:
			self.erreurrouge()
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
				self.dejafait()
			else:
				self.reussite()
			
	def erreurbleu(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		self.after(100,self.initialize)

	def erreurrouge(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		self.after(100,self.initialize)

	def dejafait(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
		self.ND=self.ND+1
		f.write('[Combi déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.after(100,self.initialize)

	def acote(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		self.after(100,self.initialize)

	def memecercle(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
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
		self.after(100,self.initialize)

	def time(self):                
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeDifficileFaible.xls", "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois pour continuer...', font='Arial 50')
		
		print('THE END\n')
		print('\n\nBonnes réponses:{}'.format(self.NR))
		f.write('Bonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		self.total=self.NR+self.NE+self.ND+self.MC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.total
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/4,self.h/4,text='Vous avez gagné peu.', font='Arial 20')
		print('RTmoy sec= %.3f'%self.RTmoy)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)

		self.fond0.bind('<Triple-Button-1>',self.fin)
		
	def fin(self, event):
		self.racine0.destroy()
		
if __name__ == '__main__':
	app = SDf(None)
	app.title('my application')
	app.destroy()
	app.mainloop()
