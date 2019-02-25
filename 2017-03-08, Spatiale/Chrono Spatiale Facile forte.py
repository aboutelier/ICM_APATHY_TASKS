import tkinter
from tkinter import *
import winsound
from winsound import *
import random
from timeit import time
import math
class SFF(tkinter.Tk):
	def __init__(self,parent):
		self.racine0=tkinter.Tk()
		self.racine0.attributes('-fullscreen',True)
		self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')

		self.pieces = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
		self.fond0.create_image(50, 10, image = self.pieces, anchor = NW)

		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeFacileFort.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeFacileFort.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeFacileFort.xls", "a")
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
		f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_SpatialeFacileFort.xls", "a")
		self.fond0.destroy()
		self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
		self.fond0.pack(fill='both')
		end=self.fond0.create_text(self.w/2,self.h/2,text='THE END\nCliquez 3 fois pour continuer...', font='Arial 50')
		
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
	app = SFF(None)
	app.title('my application')
	app.destroy()
	app.mainloop()

