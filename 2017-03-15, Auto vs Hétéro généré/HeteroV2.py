import tkinter
from tkinter import *
import winsound
from winsound import *
import math
from timeit import time
import random
##########################################DEBUT HETERO-GENERE##############################################################################################################################
class hetero(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces.ppm')
		self.imagepieces=self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_HétéroGénéréFaible.xls", "a")
		f.write("\nHétéro Généré Faible Gain\n\n")
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

		self.lim=0

		self.hetero=1

		self.tempsminutes=4
		self.tempssecondes=0

		self.tempssecondeslimite=0

		self.SRT=0
		self.RTmax=0
		self.RTmin=120

		self.progr=(self.h/2)-250
		self.pb = self.fond0.create_rectangle(self.w-100,(self.h/2)+250,self.w-130,self.progr, fill='white', width='1')

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.imagejauge=self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)
		

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
		self.consigne=self.fond0.create_text(self.w/2,(self.h/2)-300,text='Faites des combinaisons de 4 cercles', font='Arial 30')

		self.fond0.bind('<Button-1>',self.attente)

	def attente(self,event):
		self.hasardbleu1()
		self.startchrono()
		self.startlimite1()

	def startlimite1(self):
		self.lancementsec=self.racine0.after(1000, self.seclimite)
		
	def startlimite2(self):
		self.fond0.delete(self.racine0,self.pb)
		self.progr=self.progr+5.00
		self.pb = self.fond0.create_rectangle(self.w-100,(self.h/2)-250,self.w-130,self.progr, fill='white', width='1')
		self.startlimite1()
		
	def seclimite(self):
		self.tempssecondeslimite=self.tempssecondeslimite+1
		if self.tempssecondeslimite==3:
			self.tempssecondeslimite=0
			print('descente')
			self.startlimite2()
		else:
			self.startlimite1()
			
	def startchrono(self):
		if self.tempssecondes<10:
			self.chronosecondes=self.fond0.create_text(self.w/4.25,self.h/2.5,text="0{}".format(self.tempssecondes), font=('Arial 120 bold'),fill='black')
		else:
			self.chronosecondes=self.fond0.create_text(self.w/4.25,self.h/2.5,text="{}".format(self.tempssecondes), font=('Arial 120 bold'),fill='black')
			
		self.chronominutes=self.fond0.create_text(self.w/12,self.h/2.5,text="0{}:".format(self.tempsminutes), font=('Arial 120 bold'),fill='black')
		self.after(1000, self.sec)
		
	def sec(self):
		if self.tempssecondes==0 and self.tempsminutes==2 and self.hetero==1:
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

	def destroyhetero(self):
		self.racine0.destroy()
                
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_HétéroGénéréFaible.xls", "a")
		
		print('RT={}\n'.format(self.RT))
		self.reaction.append(self.RT)
		self.SRT=self.SRT+self.RT

		self.NR=self.NR+1
		print('Réussies={}'.format(self.NR))
		self.combinaison.append('Nouvelle')

		self.lim=0

		if self.NR%5==0:
			winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav',winsound.SND_FILENAME | SND_ASYNC)
	
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_HétéroGénéréFaible.xls", "a")
		self.AC=self.AC+1
		print('A côté:{}\n'.format(self.AC))
		self.combinaison.append('A côté')
		self.reaction.append('X')
		self.hasardbleu1()

	def erreurgris(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_HétéroGénéréFaible.xls", "a") 

		self.CG=self.CG+1
		print('Clic gris:{}\n'.format(self.CG))
		self.combinaison.append('Clic gris')
		self.reaction.append('X')
		self.hasardbleu1()	
		
	def memecercle(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_HétéroGénéréFaible.xls", "a")
		self.MC=self.MC+1
		print('clic sur un même cercle:{}\n'.format(self.MC))
		self.combinaison.append('Même cercle')
		self.reaction.append('X')
		self.hasardbleu1()

	def time(self):                
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_HétéroGénéréFaible.xls", "a")
		f.write('Combinaison {}\n'.format(self.combinaison))
		f.write('Temps réponse {}\n'.format(self.reaction))
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.chronosecondes=self.fond0.create_text(self.w/4.25,self.h/2.5,text="00".format(self.tempssecondes), font=('Arial 120 bold'),fill='black')
		self.chronominutes=self.fond0.create_text(self.w/12,self.h/2.5,text="02:".format(self.tempsminutes), font=('Arial 120 bold'),fill='black')

		self.pause=self.fond0.create_text(self.w/2,self.h/2,text="PAUSE", font=('Arial 70 bold'),fill='black')
			
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

		self.hetero=0
		self.racine0.after_cancel(self.lancementsec)

		self.after(30000, self.prepaauto)
		
##########################################DEBUT AUTO-GENERE##############################################################################################################################
	def prepaauto(self):
		self.startlimite1()
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
		print('\nDébut auto-généré\n')
		
		f.write("\nTACHE SPATIALE DIFFICILE FAIBLE GAIN\n\n")
		print('TACHE SPATIALE DIFFICILE FAIBLE GAIN')

		self.fond0.delete(self.racine0,self.chronominutes)
		self.fond0.delete(self.racine0,self.chronosecondes)
		self.fond0.delete(self.racine0,self.pause)

		self.NRauto=0
		self.NEauto=0
		self.NDauto=0
		self.gainauto=0
		self.combiauto=[]
		self.combauto=[]
		self.MCauto=0
		self.ACauto=0

		self.SRTauto=0
		self.RTmaxauto=0
		self.RTminauto=120

		self.tempsminutes=2
		self.tempssecondes=0

		self.progr=(self.h/2)-250
		self.pb = self.fond0.create_rectangle(self.w-100,(self.h/2)+250,self.w-130,self.progr, fill='white', width='1')

		self.jauge = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\jauge.ppm')
		self.imagejauge=self.fond0.create_image(self.w-131,(self.h/2)-250, image = self.jauge, anchor = NW)

		f.write('[Coord Cercle 1[')
		f.write('Coord Cercle 2[')
		f.write('Coord Cercle 3[')
		f.write('Coord Cercle 4[')
		f.write('Coord Cercle 5[')
		f.write('Combi[')
		f.write('RT\n')

		self.initializeauto()
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
		self.clicx=event.x
		self.clicy=event.y
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
		self.coordclicx=self.fond0.winfo_pointerx()
		self.coordclicy=self.fond0.winfo_pointery()
		print('clic x:{}'.format(self.coordclicx))
		print('clic y:{}'.format(self.coordclicy))
		if (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-225<=self.clicy<=(self.h/2)-135:
			self.clicnauto= self.coord0
			self.ellipseclic0=self.fond0.create_oval(self.coord0, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicnauto= self.coord1
			self.ellipseclic1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicnauto= self.coord2
			self.ellipseclic2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicnauto= self.coord3
			self.ellipseclic3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicnauto= self.coord4
			self.ellipseclic4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicnauto= self.coord5
			self.ellipseclic5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicnauto= self.coord6
			self.ellipseclic6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicnauto= self.coord7
			self.ellipseclic7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicnauto= self.coord8
			self.ellipseclic8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicnauto= self.coord9
			self.ellipseclic9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicnauto= self.coord10
			self.ellipseclic10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicnauto= self.coord11
			self.ellipseclic11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicnauto= self.coord12
			self.ellipseclic12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicnauto= self.coord13
			self.ellipseclic13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicnauto= self.coord14
			self.ellipseclic14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
			f.write('{}'.format(self.clicnauto))
			self.fond0.bind('<ButtonRelease-1>',self.verifcercleauto)
		else:
			self.acoteauto()

	def reussiteauto(self):
		self.combiauto.append(self.combauto)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
		
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
			if self.NRauto%5==0:
				winsound.PlaySound('C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Son\Pièces.wav',winsound.SND_FILENAME | SND_ASYNC)

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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
		self.NDauto=self.NDauto+1
		f.write('[Combi déjà faite\n')
		print('Déjà fait:{}\n'.format(self.NDauto))
		self.initializeauto()

	def acoteauto(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_AutoGénéréFaible.xls", "a")
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END', font='Arial 50')
		
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
		gain=self.fond0.create_text(self.w/4,self.h/4,text='Vous avez gagné peu.', font='Arial 20')
		print('RTmoy sec= %.3f'%self.RTmoyauto)
		f.write('RTmoy sec=[ %.3f\n'%self.RTmoyauto)
		print('RTmax sec= %.3f'%self.RTmaxauto)
		f.write('RTmax sec=[ %.3f\n'%self.RTmaxauto)
		print('RTmin sec= %.3f'%self.RTminauto)
		f.write('RTmin sec=[ %.3f\n\n'%self.RTminauto)

		self.fond0.bind('<Triple-Button-1>',self.fin)
		
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
