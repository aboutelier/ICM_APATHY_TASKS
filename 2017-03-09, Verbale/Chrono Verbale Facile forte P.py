import tkinter
from tkinter import *
import winsound
from winsound import *
import random
from timeit import time
import math
class VFF(tkinter.Tk):
        def __init__(self,parent):
                self.racine0=tkinter.Tk()
                self.racine0.attributes('-fullscreen',True)
                self.w, self.h = self.racine0.winfo_screenwidth(),self.racine0.winfo_screenheight()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')

                self.pieces2 = PhotoImage(file = 'C:\\Users\johan.ferrandverdejo\Desktop\ECOCAPTURE\ICM_APATHY_TASKS\Image\pieces2.ppm')
                self.fond0.create_image(50, 10, image = self.pieces2, anchor = NW)

                f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleFacileFort.xls", "a")
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
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleFacileFort.xls", "a")
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
                self.consonne1=["R", "T", "M", "S", "F", "G", "L", "C", "B", "r", "t", "m", "s", "f", "g", "l", "c", "b"]
                self.consonne2=["M", "R", "T", "P", "S", "F", "G", "L", "C", "B", "m", "r", "t", "p", "s", "f", "g", "l", "c", "b"]
                self.motcible=random.choice(self.lettre1cible)+random.choice(self.voyelle)+random.choice(self.consonne2)+random.choice(self.voyelle)
                self.motdistracteur=random.choice(self.consonne1)+random.choice(self.voyelle)+random.choice(self.consonne2)+random.choice(self.voyelle)

                self.initialize()

        def initialize(self):
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleFacileFort.xls", "a")

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
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleFacileFort.xls", "a")

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
                f = open("C:\\Users\johan.ferrandverdejo\Desktop\Sujet_VerbaleFacileFort.xls", "a")

                self.fond0.destroy()
                self.fond0 = tkinter.Canvas(self.racine0, bg='white', width=self.w, height=self.h)
                self.fond0.pack(fill='both')
                end=self.fond0.create_text(self.w/2,self.h/2,text='THE END', font='Arial 50')
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
        app = VFF(None)
        app.title('my application')
        app.destroy()
        app.mainloop()
