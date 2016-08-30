from tkinter import *
class Kanvas:
    def __init__(self,raiz):

        self.canvas1=Canvas(raiz)
        self.canvas1['width']=150
        self.canvas1['height']=400
        self.canvas1['cursor']='X_cursor'
        self.canvas1['bd']=5
        self.canvas1['bg']='dodgerblue'
        self.canvas1.pack(side=LEFT)

        self.canvas2=Canvas(raiz)
        self.canvas2['width']=150
        self.canvas2['height']=400
        self.canvas2['cursor']='dot'
        self.canvas2['bd']=5
        self.canvas2['bg']='purple'
        self.canvas2.pack(side=LEFT)

        self.canvas3=Canvas(raiz)
        self.canvas3['width']=150
        self.canvas3['height']=400
        self.canvas3['cursor']='fleur'
        self.canvas3['bd']=5
        self.canvas3['bg']='red'
        self.canvas3.pack(side=LEFT)

        self.canvas4=Canvas(raiz)
        self.canvas4['width']=150
        self.canvas4['height']=400
        self.canvas4['cursor']='circle'
        self.canvas4['bd']=5
        self.canvas4['bg']='green'
        self.canvas4.pack(side=LEFT)

        self.canvas5=Canvas(raiz)
        self.canvas5['width']=150
        self.canvas5['height']=400
        self.canvas5['cursor']='dotbox'
        self.canvas5['bd']=5
        self.canvas5['bg']='gold'
        self.canvas5.pack(side=LEFT)

        self.canvas6=Canvas(raiz)
        self.canvas6['width']=150
        self.canvas6['height']=400
        self.canvas6['cursor']='target'
        self.canvas6['bd']=5
        self.canvas6['bg']='pink'
        self.canvas6.pack(side=LEFT)        

instancia=Tk()
Kanvas(instancia)
instancia.title('Exemplo de Kanvas')
instancia.mainloop()
