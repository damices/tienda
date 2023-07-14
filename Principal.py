from tkinter import *
from Clientes import Clientes

class Principal:
    def __init__(self):
        self.ventanaPrincipal = Tk()
        self.ventanaPrincipal.title("Sistema de Fcaturación")
        m = self.ventanaPrincipal.maxsize()
        self.ventanaPrincipal.geometry('{}x{}+0+0'.format(*m))

        self.barraMenu = Menu(self.ventanaPrincipal)
        self.ventanaPrincipal.config(menu=self.barraMenu)

        self.menuArchivo = Menu(self.barraMenu,tearoff=0)
        self.menuArchivo.add_command(label='Información')
        self.menuArchivo.add_command(label='Salir', command=lambda:self.ventanaPrincipal.destroy())

        self.menuAdminitracion = Menu (self.barraMenu, tearoff=0)
        self.menuAdminitracion.add_command(label='Clientes', command=lambda:Clientes.__init__(self,self.ventanaPrincipal))

        self.barraMenu.add_cascade(label="Archivo", menu=self.menuArchivo)
        self.barraMenu.add_cascade(label='Administración', menu=self.menuAdminitracion)

        self.ventanaPrincipal.mainloop()