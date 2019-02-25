import tkinter
from tkinter import *
import winsound
from winsound import *
import random
from timeit import time
import math
class SDf(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		#f.write("\nTACHE SPATIALE DIFFICILE FAIBLE GAIN\n\n")
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

		self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)
		self.progr=self.w-925
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
		self.after(60000, self.time)
		self.after(30000, self.debutchrono)

	def debutchrono(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		print('\nPlus que 30 sec\n')
		#f.write('\n30 sec\n')
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
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
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
		
		#f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
		#f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
		#f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
		#f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		#f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))
		
		#f.write('[Coord Cercle 1[')
		#f.write('Coord Cercle 2[')
		#f.write('Coord Cercle 3[')
		#f.write('Coord Cercle 4[')
		#f.write('Combi[')
		#f.write('RT\n')
		
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
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()

	def reussite(self):
		self.combi.append(self.comb)
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
	
		self.NR=self.NR+1
		#f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
						
		self.gain=self.gain+0.10

		print('RT sec={}\n'.format(self.RT))
		#f.write('{}\n'.format(self.RT))
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
				self.after(100,self.dejafait)
			else:
				self.tclic=time.perf_counter()
				self.RT=self.tclic-self.tapp
				self.after(100,self.reussite)
			
	def erreurbleu(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		print('Bleu touché!')
		self.NE=self.NE+1
		print('raté!NE={}\n'.format(self.NE))
		#if self.numclic==0:
			#f.write('[[[[Distracteur Bleu\n')
		#elif self.numclic==1:
			#f.write('[[[Distracteur Bleu\n')
		#elif self.numclic==2:
			#f.write('[[Distracteur Bleu\n')
		#elif self.numclic==3:
			#f.write('[Distracteur Bleu\n')
		self.initialize()

	def erreurrouge(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		print('Rouge touché!')
		self.NE=self.NE+1
		#if self.numclic==0:
			#f.write('[[[[Distracteur Rouge\n')
		#elif self.numclic==1:
			#f.write('[[[Distracteur Rouge\n')
		#elif self.numclic==2:
			#f.write('[[Distracteur Rouge\n')
		#elif self.numclic==3:
			#f.write('[Distracteur Rouge\n')
		print('raté!NE={}\n'.format(self.NE))
		self.initialize()

	def dejafait(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		self.ND=self.ND+1
		#f.write('[Combi déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.initialize()

	def acote(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		self.AC=self.AC+1
		#f.write('[{}, '.format(self.coordclicx))
		#f.write('{}'.format(self.coordclicy))
		#if self.numclic==0:
			#f.write('[[[[A cote\n')
		#elif self.numclic==1:
			#f.write('[[[A cote\n')
		#elif self.numclic==2:
			#f.write('[[A cote\n')
		#elif self.numclic==3:
			#f.write('[A cote\n')
		print('A côté:{}\n'.format(self.AC))
		self.initialize()

	def memecercle(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		self.MC=self.MC+1
		#if self.numclic==0:
			#f.write('[[[[Meme cercle\n')
		#elif self.numclic==1:
			#f.write('[[[Meme cercle\n')
		#elif self.numclic==2:
			#f.write('[[Meme cercle\n')
		#elif self.numclic==3:
			#f.write('[Meme cercle\n')
		print('clic sur un même cercle:{}\n'.format(self.MC))
		self.initialize()

	def time(self):
		self.racine0.after_cancel(self.lancementsec)                
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		
		
		print('THE END\n')
		end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
		print('\n\nBonnes réponses:{}'.format(self.NR))
		#f.write('\n\nBonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		#f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		#f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		#f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		self.total=self.NR+self.NE+self.ND+self.MC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.total
		print('Taux de réussite= %.2f'%self.taux)
		#f.write('Taux de réussite=[ %.2f\n'%self.taux)
		#gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu.', font='Arial 50')
		print('RTmoy sec= %.3f'%self.RTmoy)
		#f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		#f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		#f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)

		self.after(15000,self.fin)
		
	def fin(self):
		self.racine0.destroy()

class SDF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		#f.write("\nTACHE SPATIALE DIFFICILE FORT GAIN\n\n")
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

		self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)
		self.progr=self.w-925
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
		self.after(60000, self.time)
		self.after(30000, self.debutchrono)

	def debutchrono(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		print('\nPlus que 30 sec\n')
		#f.write('\n30 sec\n')
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
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
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
		
		#f.write('Coord distracteur bleu 1 {}\n'.format(self.nbblue1))
		#f.write('Coord distracteur bleu 2 {}\n'.format(self.nbblue2))
		#f.write('Coord distracteur bleu 3 {}\n'.format(self.nbblue3))
		#f.write('Coord distracteur rouge 1 {}\n'.format(self.nbred1))
		#f.write('Coord distracteur rouge 2 {}\n\n'.format(self.nbred2))
		
		#f.write('[Coord Cercle 1[')
		#f.write('Coord Cercle 2[')
		#f.write('Coord Cercle 3[')
		#f.write('Coord Cercle 4[')
		#f.write('Combi[')
		#f.write('RT\n')
		
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
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFaible.xls", "a")
		coordclicx=self.fond0.winfo_pointerx()
		coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(coordclicx))
		print('clic y:{}'.format(coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicn= self.coord0
			self.ellipse0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
			#f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()    

	def reussite(self):
		self.combi.append(self.comb)
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
	
		self.NR=self.NR+1
		#f.write('Nouvelle combi\n')
		print('NR={}'.format(self.NR))
						
		self.gain=self.gain+1.00

		print('RT sec={}\n'.format(self.RT))
		#f.write('{}\n'.format(self.RT))
		self.SRT=self.SRT+self.RT

		self.fond0.delete(self.racine0,self.pb)
		self.progr=self.progr+5.00
		self.pb = self.fond0.create_rectangle(self.progr,(self.h/1.2),self.w-425,(self.h/1.2)+30, fill='white', width='1')
		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav',winsound.SND_FILENAME | SND_ASYNC)
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
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		print('Bleu touché!')
		self.NE=self.NE+1
		#if self.numclic==0:
			#f.write('[[[[Distracteur Bleu\n')
		#elif self.numclic==1:
			#f.write('[[[Distracteur Bleu\n')
		#elif self.numclic==2:
			#f.write('[[Distracteur Bleu\n')
		#elif self.numclic==3:
			#f.write('[Distracteur Bleu\n')
		print('raté!NE={}\n'.format(self.NE))
		self.initialize()

	def erreurrouge(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		print('Rouge touché!')
		self.NE=self.NE+1
		#if self.numclic==0:
			#f.write('[[[[Distracteur Rouge\n')
		#elif self.numclic==1:
			#f.write('[[[Distracteur Rouge\n')
		#elif self.numclic==2:
			#f.write('[[Distracteur Rouge\n')
		#elif self.numclic==3:
			#f.write('[Distracteur Rouge\n')
		print('raté!NE={}\n'.format(self.NE))
		self.initialize()

	def dejafait(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		self.ND=self.ND+1
		#f.write('[Combi déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.initialize()

	def acote(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		self.AC=self.AC+1
		#f.write('[{}, '.format(self.coordclicx))
		#f.write('{}'.format(self.coordclicy))
		#if self.numclic==0:
			#f.write('[[[[A cote\n')
		#elif self.numclic==1:
			#f.write('[[[A cote\n')
		#elif self.numclic==2:
			#f.write('[[A cote\n')
		#elif self.numclic==3:
			#f.write('[A cote\n')
		print('A côté:{}\n'.format(self.AC))
		self.initialize()

	def memecercle(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		self.MC=self.MC+1
		#if self.numclic==0:
			#f.write('[[[[Meme cercle\n')
		#elif self.numclic==1:
			#f.write('[[[Meme cercle\n')
		#elif self.numclic==2:
			#f.write('[[Meme cercle\n')
		#elif self.numclic==3:
			#f.write('[Meme cercle\n')
		print('clic sur un même cercle:{}\n'.format(self.MC))
		self.initialize()

	def time(self):
		self.racine0.after_cancel(self.lancementsec)                
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeDifficileFort.xls", "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		
		
		print('THE END\n')
		end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
		print('\n\nBonnes réponses:{}'.format(self.NR))
		#f.write('Bonnes réponses=[ %.2f\n'%self.NR)
		print('Erreurs couleur:{}'.format(self.NE))
		#f.write('Erreurs couleur:[ %.2f\n'%self.NE)
		print('Erreurs répétition:{}'.format(self.ND))
		#f.write('Erreurs répétition:[ %.2f\n'%self.ND)
		print('Erreurs même cercle:{}'.format(self.MC))
		#f.write('Erreurs même cercle:[ %.2f\n'%self.MC)
		self.total=self.NR+self.NE+self.ND+self.MC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.total
		print('Taux de réussite= %.2f'%self.taux)
		#f.write('Taux de réussite=[ %.2f\n'%self.taux)
		#gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		#f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		#f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		#f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)

		self.after(15000,self.fin)
                
	def fin(self):
		self.racine0.destroy()
class SFf(tkinter.Tk):
        def __init__(self,parent):
                self.racine0=tkinter.Tk()
                self.racine0.attributes('-fullscreen',True)
                self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')

                self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
                self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

                #f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFaible.xls", "a")
                #f.write("\nTACHE SPATIALE FACILE FAIBLE GAIN\n\n")
                print('TACHE SPATIALE FACILE FAIBLE GAIN')

                #f.write('[Coord cible[')
                #f.write('Coord distracteur[')
                #f.write('Cercle choisi[')
                #f.write('Clic X[')
                #f.write('Clic Y[')
                #f.write('RT sec[\n')

                self.NR=0
                self.NER=0
                self.NEG=0
                self.AC=0
                self.gain=0

                self.temps=30

                self.SRT=0
                self.RTmax=0
                self.RTmin=360

                self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
                self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)

                self.progr=self.w-925
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
                self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-300,text='Touchez le cercle bleu',fill='black', font='Arial 20',justify='center')

                self.fond0.bind('<Button-1>',self.attente)

        def attente(self,event):
                self.hasard()
                self.after(60000, self.time)
                self.after(30000, self.debutchrono)

        def debutchrono(self):
                #f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFaible.xls", "a")
                print('\nPlus que 30 sec\n')
                #f.write('\n30 sec\n')
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
                #f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFaible.xls", "a")
                #f.write('{}'.format(self.nbblue))
                #f.write('{}['.format(self.nbred))

                xclic=event.x
                yclic=event.y
                self.coordclicx=self.fond0.winfo_pointerx()
                self.coordclicy=self.fond0.winfo_pointery()
                print('clic x:{}'.format(self.coordclicx))
                print('clic y:{}'.format(self.coordclicy))
                if self.nbblue[0]<=xclic<=self.nbblue[2] and self.nbblue[1]<=yclic<=self.nbblue[3]:
                        self.NR=self.NR+1
                        print('Bien! NR={}'.format(self.NR))
                        #f.write('Cible[')
                        #f.write('{}['.format(self.coordclicx))
                        #f.write('{}['.format(self.coordclicy))

                        self.fond0.delete(self.racine0,self.pb)
                        self.progr=self.progr+0.88
                        self.pb = self.fond0.create_rectangle(self.progr,(self.h/1.2),self.w-425,(self.h/1.2)+30, fill='white', width='1')
                        if self.NR%10==0:
                                self.gain=self.gain+0.10
                                if self.NR%50==0:
                                        winsound.PlaySound('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav', winsound.SND_FILENAME | SND_ASYNC)

                        self.tclic=time.perf_counter()
                        self.RT=self.tclic-self.tapp
                        print('RT={}\n'.format(self.RT))
                        #f.write('{}\n'.format(self.RT))
                        self.SRT=self.SRT+self.RT
                        if self.RT>self.RTmax:
                                self.RTmax=self.RT
                                if self.RT<self.RTmin:
                                        self.RTmin=self.RT
                        elif self.RT<self.RTmin:
                                        self.RTmin=self.RT

                elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
                        print('Rouge touché!')
                        #f.write('Distracteur[')
                        #f.write('{}['.format(self.coordclicx))
                        #f.write('{}[\n'.format(self.coordclicy))
                        
                        self.NER=self.NER+1
                        print('raté!NER={}\n'.format(self.NER))
                        self.initialize()
                else:
                        if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-225<yclic<=(self.h/2)-135 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-45<=yclic<=(self.h/2)+135) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+45 <=yclic<=(self.h/2)+135) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)-135<=yclic<=(self.h/2)+225) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+135<=yclic<=(self.h/2)+225):
                                print('Gris touché!')
                                #f.write('Gris[')
                                #f.write('{}['.format(self.coordclicx))
                                #f.write('{}[\n'.format(self.coordclicy))
                                self.NEG=self.NEG+1
                                print('raté!NEG={}\n'.format(self.NEG))
                
                        else:
                                 print('A côté!')
                                 #f.write('A cote[')
                                 #f.write('{}['.format(self.coordclicx))
                                 #f.write('{}[\n'.format(self.coordclicy))
                                 self.AC=self.AC+1
                                 print('raté!AC={}\n'.format(self.AC))

                self.hasard()

        def time(self):
                self.racine0.after_cancel(self.lancementsec)
                #f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFaible.xls", "a")                
                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                
                
                print('THE END\n')
                end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
                print('Bonnes réponses:{}'.format(self.NR))
                #f.write('\nBonnes réponses:[{}\n'.format(self.NR))
                print('Erreurs rouge:{}'.format(self.NER))
                #f.write('Erreurs rouge:[{}\n'.format(self.NER))
                print('Erreurs gris:{}'.format(self.NEG))
                #f.write('Erreurs gris:[{}\n'.format(self.NEG))
                print('Erreurs à côté:{}'.format(self.AC))
                #f.write('Erreurs à côté:[{}\n'.format(self.AC))
                self.NE=self.NER+self.NEG+self.AC
                print('Erreurs totales:{}'.format(self.NE))
                #f.write('Erreurs totales:[{}\n'.format(self.NE))
                self.total=self.NR+self.NE
                if self.total==0:
                        self.taux=0
                        self.RTmoy=0
                else:
                        self.taux=self.NR/self.total*100
                        self.RTmoy=self.SRT/self.total
                print('Taux de réussite= %.2f'%self.taux)
                #f.write('Taux de réussite=[ %.2f\n'%self.taux)
                #gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné peu.', font='Arial 50')
                print('RTmoy= %.3f'%self.RTmoy)
                #f.write('RTmoy=[ %.3f\n'%self.RTmoy)
                print('RTmax= %.3f'%self.RTmax)
                #f.write('RTmax=[ %.3f\n'%self.RTmax)
                print('RTmin= %.3f'%self.RTmin)
                #f.write('RTmin=[ %.3f\n\n'%self.RTmin)

                self.after(15000,self.fin)
                
        def fin(self):
                self.racine0.destroy()

class SFF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFort.xls", "a")
		#f.write("\nTACHE SPATIALE FACILE FORT GAIN\n\n")
		print('TACHE SPATIALE FACILE FORT GAIN')

		#f.write('[Coord cible[')
		#f.write('Coord distracteur[')
		#f.write('Cercle choisi[')
		#f.write('Clic X[')
		#f.write('Clic Y[')
		#f.write('RT sec[\n')

		self.NR=0
		self.NER=0
		self.NEG=0
		self.AC=0
		self.gain=0

		self.temps=30

		self.SRT=0
		self.RTmax=0
		self.RTmin=360

		self.jauge = PhotoImage(file = 'C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.imagejauge=self.fond0.create_image(self.w-925,(self.h/1.2), image = self.jauge, anchor = NW)

		self.progr=self.w-925
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
		self.consigne=self.fond0.create_text(self.w/1.3,(self.h/1.6)-300,text='Touchez le cercle bleu',fill='black', font='Arial 20',justify='center')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasard()
		self.after(60000, self.time)
		self.after(30000, self.debutchrono)

	def debutchrono(self):
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFort.xls", "a")
		print('\nPlus que 30 sec\n')
		#f.write('\n30 sec\n')
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
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFort.xls", "a")
		#f.write('{}'.format(self.nbblue))
		#f.write('{}['.format(self.nbred))

		xclic=event.x
		yclic=event.y
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if self.nbblue[0]<=xclic<=self.nbblue[2] and self.nbblue[1]<=yclic<=self.nbblue[3]:
			self.NR=self.NR+1
			print('Bien! NR={}'.format(self.NR))
			#f.write('Cible[')
			#f.write('{}['.format(self.coordclicx))
			#f.write('{}['.format(self.coordclicy))

			self.fond0.delete(self.racine0,self.pb)
			self.progr=self.progr+1.66
			self.pb = self.fond0.create_rectangle(self.progr,(self.h/1.2),self.w-425,(self.h/1.2)+30, fill='white', width='1')
			if self.NR%10==0:
				self.gain=self.gain+1.00
				if self.NR%50==0:
					winsound.PlaySound('C:\\Users\\ECOCAPTURE\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Cash.wav', winsound.SND_FILENAME | SND_ASYNC)

			self.tclic=time.perf_counter()
			self.RT=self.tclic-self.tapp
			print('RT={}\n'.format(self.RT))
			#f.write('{}\n'.format(self.RT))
			self.SRT=self.SRT+self.RT
			if self.RT>self.RTmax:
				self.RTmax=self.RT
				if self.RT<self.RTmin:
					self.RTmin=self.RT
			elif self.RT<self.RTmin:
					self.RTmin=self.RT

		elif self.nbred[0]<=xclic<=self.nbred[2] and self.nbred[1]<=yclic<=self.nbred[3]:
			print('Rouge touché!')
			#f.write('Distracteur[')
			#f.write('{}['.format(self.coordclicx))
			#f.write('{}[\n'.format(self.coordclicy))
			
			self.NER=self.NER+1
			print('raté!NER={}\n'.format(self.NER))
			self.initialize()
		else:
			if (self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-225<yclic<=(self.h/2)-135 or ((self.w/2)-45<=xclic<=(self.w/2)+45 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-45<=xclic<=(self.w/2)+135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)-135<=yclic<=(self.h/2)-45) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)-45<=yclic<=(self.h/2)+45) or ((self.w/2)-135<=xclic<=(self.w/2)-45 and (self.h/2)-45<=yclic<=(self.h/2)+135) or ((self.w/2)+45<=xclic<=(self.w/2)+135 and (self.h/2)+45 <=yclic<=(self.h/2)+135) or ((self.w/2)-225<=xclic<=(self.w/2)-135 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)+135<=xclic<=(self.w/2)+225 and (self.h/2)+135<=yclic<=(self.h/2)+225) or ((self.w/2)-315<=xclic<=(self.w/2)-225 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)+225<=xclic<=(self.w/2)+315 and (self.h/2)+45<=yclic<=(self.h/2)+135) or ((self.w/2)-405<=xclic<=(self.w/2)-315 and (self.h/2)-135<=yclic<=(self.h/2)+225) or ((self.w/2)+315<=xclic<=(self.w/2)+405 and (self.h/2)+135<=yclic<=(self.h/2)+225):
				print('Gris touché!')
				#f.write('Gris[')
				#f.write('{}['.format(self.coordclicx))
				#f.write('{}[\n'.format(self.coordclicy))
				self.NEG=self.NEG+1
				print('raté!NEG={}\n'.format(self.NEG))
		
			else:
				 print('A côté!')
				 #f.write('A cote[')
				 #f.write('{}['.format(self.coordclicx))
				 #f.write('{}[\n'.format(self.coordclicy))
				 self.AC=self.AC+1
				 print('raté!AC={}\n'.format(self.AC))

		self.hasard()

	def time(self):
		self.racine0.after_cancel(self.lancementsec)
		#f = open("C:\\Users\\ECOCAPTURE\Desktop\SujetEntrainement_SpatialeFacileFort.xls", "a")
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		
		
		print('THE END\n')
		end=self.fond0.create_text(self.w/2,self.h/2,text='FIN DE CETTE TACHE', font='Arial 30', justify='center')
		print('Bonnes réponses:{}'.format(self.NR))
		#f.write('\nBonnes réponses:[{}\n'.format(self.NR))
		print('Erreurs rouge:{}'.format(self.NER))
		#f.write('Erreurs rouge:[{}\n'.format(self.NER))
		print('Erreurs gris:{}'.format(self.NEG))
		#f.write('Erreurs gris:[{}\n'.format(self.NEG))
		print('Erreurs à côté:{}'.format(self.AC))
		#f.write('Erreurs à côté:[{}\n'.format(self.AC))
		self.NE=self.NER+self.NEG+self.AC
		print('Erreurs totales:{}'.format(self.NE))
		#f.write('Erreurs totales:[{}\n'.format(self.NE))
		self.total=self.NR+self.NE
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.total
		print('Taux de réussite= %.2f'%self.taux)
		#f.write('Taux de réussite=[ %.2f\n'%self.taux)
		#gain=self.fond0.create_text(self.w/2,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 50', justify='center')
		print('RTmoy sec= %.3f'%self.RTmoy)
		#f.write('RTmoy sec=[ %.3f\n'%self.RTmoy)
		print('RTmax sec= %.3f'%self.RTmax)
		#f.write('RTmax sec=[ %.3f\n'%self.RTmax)
		print('RTmin sec= %.3f'%self.RTmin)
		#f.write('RTmin sec=[ %.3f\n\n'%self.RTmin)
		
		self.after(15000,self.fin)
                
	def fin(self):
		self.racine0.destroy()



		                
ordre=1
ordretaches=[]
while ordre!=[]:
        if ordre==1:
                ordre=2
                print('SPATIAL FACILE FAIBLE\n')
                if __name__ == '__main__':
                        app = SFf(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif ordre==2:
                 ordre=3
                 print('SPATIAL FACILE FORTE\n')
                 if __name__ == '__main__':
                        app = SFF(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif ordre==3:
                 ordre=4
                 print('SPATIAL DIFFICILE FAIBLE\n')
                 if __name__ == '__main__':
                        app = SDf(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
        elif ordre==4:
                 ordre=5
                 print('SPATIAL DIFFICILE FORTE\n')
                 if __name__ == '__main__':
                        app = SDF(None)
                        app.title('my application')
                        app.destroy()
                        app.mainloop()
     
      
