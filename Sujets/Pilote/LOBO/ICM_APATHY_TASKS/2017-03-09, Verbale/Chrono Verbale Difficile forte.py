import tkinter
from tkinter import *
import winsound
from winsound import *
import math
from timeit import time
import random
class VDF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces2 = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces2, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileFort.xls", "a")
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

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
		
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

		self.consonne1=self.fond0.create_text(self.coordconsonne1,text='B', font='Arial 50')
		self.consonne2=self.fond0.create_text(self.coordconsonne2,text='C', font='Arial 50')
		self.consonne3=self.fond0.create_text(self.coordconsonne3,text='F', font='Arial 50')
		self.consonne4=self.fond0.create_text(self.coordconsonne4,text='G', font='Arial 50')
		self.consonne5=self.fond0.create_text(self.coordconsonne5,text='L', font='Arial 50')
		self.consonne6=self.fond0.create_text(self.coordconsonne6,text='M', font='Arial 50')
		self.consonne7=self.fond0.create_text(self.coordconsonne7,text='P', font='Arial 50')
		self.consonne8=self.fond0.create_text(self.coordconsonne8,text='R', font='Arial 50')
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

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
		
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

		self.consonne1=self.fond0.create_text(self.coordconsonne1,text='B', font='Arial 50')
		self.consonne2=self.fond0.create_text(self.coordconsonne2,text='C', font='Arial 50')
		self.consonne3=self.fond0.create_text(self.coordconsonne3,text='F', font='Arial 50')
		self.consonne4=self.fond0.create_text(self.coordconsonne4,text='G', font='Arial 50')
		self.consonne5=self.fond0.create_text(self.coordconsonne5,text='L', font='Arial 50')
		self.consonne6=self.fond0.create_text(self.coordconsonne6,text='M', font='Arial 50')
		self.consonne7=self.fond0.create_text(self.coordconsonne7,text='P', font='Arial 50')
		self.consonne8=self.fond0.create_text(self.coordconsonne8,text='R', font='Arial 50')
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
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord1texte
			self.ellipse1=self.fond0.create_oval(self.coord1, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-45<=self.clicx<=(self.w/2)+45 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord2texte
			self.ellipse2=self.fond0.create_oval(self.coord2, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord3texte
			self.ellipse3=self.fond0.create_oval(self.coord3, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)-135<=self.clicy<=(self.h/2)-45:
			self.clicn= self.coord4texte
			self.ellipse4=self.fond0.create_oval(self.coord4, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord5texte
			self.ellipse5=self.fond0.create_oval(self.coord5, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)-45<=self.clicy<=(self.h/2)+45:
			self.clicn= self.coord6texte
			self.ellipse6=self.fond0.create_oval(self.coord6, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-135<=self.clicx<=(self.w/2)-45 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord7texte
			self.ellipse7=self.fond0.create_oval(self.coord7, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+45<=self.clicx<=(self.w/2)+135 and (self.h/2)+45 <=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord8texte
			self.ellipse8=self.fond0.create_oval(self.coord8, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-225<=self.clicx<=(self.w/2)-135 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord9texte
			self.ellipse9=self.fond0.create_oval(self.coord9, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+135<=self.clicx<=(self.w/2)+225 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord10texte
			self.ellipse10=self.fond0.create_oval(self.coord10, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-315<=self.clicx<=(self.w/2)-225 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord11texte
			self.ellipse11=self.fond0.create_oval(self.coord11, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+225<=self.clicx<=(self.w/2)+315 and (self.h/2)+45<=self.clicy<=(self.h/2)+135:
			self.clicn= self.coord12texte
			self.ellipse12=self.fond0.create_oval(self.coord12, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)-405<=self.clicx<=(self.w/2)-315 and (self.h/2)-135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord13texte
			self.ellipse13=self.fond0.create_oval(self.coord13, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		elif (self.w/2)+315<=self.clicx<=(self.w/2)+405 and (self.h/2)+135<=self.clicy<=(self.h/2)+225:
			self.clicn= self.coord14texte
			self.ellipse14=self.fond0.create_oval(self.coord14, fill='grey40', width='5')
			f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
			f.write('{}'.format(self.clicn))
			self.verifcercle()
		else:
			self.acote()    

	def reussite(self):
		self.combi.append(self.comb)
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
	
		self.NR=self.NR+1
		f.write('[Nouvelle combi[')
		print('NR={}'.format(self.NR))
							
		self.gain=self.gain+1.00

		self.tclic=time.perf_counter()
		self.RT=self.tclic-self.tapp
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
		self.after(100,self.initialize)

	def verifcercle(self):
		if self.clicn in self.comb:
			self.memecercle()
		elif self.nbblue1[0]<=self.clicx<=self.nbblue1[2] and self.nbblue1[1]<=self.clicy<=self.nbblue1[3]or self.nbblue2[0]<=self.clicx<=self.nbblue2[2] and self.nbblue2[1]<=self.clicy<=self.nbblue2[3] or self.nbblue3[0]<=self.clicx<=self.nbblue3[2] and self.nbblue3[1]<=self.clicy<=self.nbblue3[3]:
			self.erreurbleu()
		elif self.nbred1[0]<=self.clicx<=self.nbred1[2] and self.nbred1[1]<=self.clicy<=self.nbred1[3] or self.nbred2[0]<=self.clicx<=self.nbred2[2] and self.nbred2[1]<=self.clicy<=self.nbred2[3]:
			self.erreurrouge()
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
				self.pasvoyelle()
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.clicprecedent=2
				self.testcombi()
		elif self.clicprecedent==2:
			if self.clicn==self.coordconsonne1 or self.clicn==self.coordconsonne2 or self.clicn==self.coordconsonne3 or self.clicn==self.coordconsonne4 or self.clicn==self.coordconsonne5 or self.clicn==self.coordconsonne6 or self.clicn==self.coordconsonne7 or self.clicn==self.coordconsonne8 or self.clicn==self.coordconsonne9 or self.clicn==self.coordconsonne10:
				self.clicprecedent=1
				self.testcombi()
			elif self.clicn==self.coordvoyelle1 or self.clicn==self.coordvoyelle2 or self.clicn==self.coordvoyelle3 or self.clicn==self.coordvoyelle4 or self.clicn==self.coordvoyelle5:
				self.pasconsonne()

	def pasconsonne(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		self.after(100,self.initialize)

	def pasvoyelle(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		self.after(100,self.initialize)

	def testcombi(self):
		self.comb.append(self.clicn)
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		self.after(100,self.initialize)

	def erreurrouge(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
		self.ND=self.ND+1
		f.write('[Déjà faite\n')
		print('Déjà fait:{}\n'.format(self.ND))
		self.after(100,self.initialize)

	def acote(self):
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleDifficileForte.xls", "a")
		
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END', font='Arial 50')
		
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
		self.total=self.NR+self.NE+self.ND+self.MC+self.PC+self.PV+self.AC
		if self.total==0:
			self.taux=0
			self.RTmoy=0
		else:
			self.taux=self.NR/self.total*100
			self.RTmoy=self.SRT/self.total
		print('Taux de réussite= %.2f'%self.taux)
		f.write('Taux de réussite=[ %.2f\n'%self.taux)
		gain=self.fond0.create_text(self.w/4,self.h/4,text='Vous avez gagné BEAUCOUP.', font='Arial 20')
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
	app = VDF(None)
	app.title('my application')
	app.destroy()
	app.mainloop()
