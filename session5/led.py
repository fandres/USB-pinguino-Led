# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 21:13:10 2014

@author: fAnDrEs
"""

import sys    
# Importa todos los elementos necesarios para PyQt
# Importar modulo Qt
from PyQt4 import QtCore,QtGui
# Importar el código del modulo compilado UI
from ledUi import Ui_Form
import usb

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------
# Crear una clase para nuestra ventana principal
# Se hereda de la clase QtGui.QFrame
class Principal(QtGui.QFrame):
     # Se define el constructor de la clase __init__ 
    def __init__(self):
        # Se llama al constructor de la clase padre
        QtGui.QFrame.__init__(self)
        
        # Esto es siempre igual.
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
        self.connect(self.ui.boton_iniciar, QtCore.SIGNAL("clicked()"), self.inicio)

        
    @QtCore.pyqtSlot()    
    def on_boton_led1_clicked(self):
        if self.ui.kled_1.state() == 0 :
            self.ui.kled_1.on() # Enciende el led en la ui
            self.ui.boton_led1.setText("Off") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1 
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led1.setIcon(icon2)
            
        else:
            self.ui.kled_1.off() # Enciende el led en la ui
            self.ui.boton_led1.setText("On") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1 
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led1.setIcon(icon1)
            
    @QtCore.pyqtSlot()    
    def on_boton_led2_clicked(self):
        if self.ui.kled_2.state() == 0 :
            self.ui.kled_2.on() # Enciende el led en la ui
            self.ui.boton_led2.setText("Off") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1 
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led2.setIcon(icon2)
            
        else:
            self.ui.kled_2.off() # Enciende el led en la ui
            self.ui.boton_led2.setText("On") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1 
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led2.setIcon(icon1)

    @QtCore.pyqtSlot()    
    def on_boton_led3_clicked(self):
        if self.ui.kled_3.state() == 0 :
            self.ui.kled_3.on() # Enciende el led en la ui
            self.ui.boton_led3.setText("Off") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1 
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led3.setIcon(icon2)
            
        else:
            self.ui.kled_3.off() # Enciende el led en la ui
            self.ui.boton_led3.setText("On") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1 
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led3.setIcon(icon1)
        
        
    
    def inicio(self):
        # Se habilita los botones "boton_ledx"        
        self.ui.boton_led1.setEnabled(True)
        self.ui.boton_led2.setEnabled(True)
        self.ui.boton_led3.setEnabled(True)
        # Conexcion pinguino
        self.Pinguino()
        if self.pinguino_open() == None:
            print >> sys.stderr, "Unable to open Pinguino device!"
        self.pinguino_update()
        
        
    def Pinguino(self):
        self.VENDOR = 0x04D8
        self.PRODUCT = 0xFEAA
        #self.CONFIGURATION = 0x01 # if bootloader v4.x
        self.CONFIGURATION = 0x03 # if bootloader v2.x
        self.INTERFACE = 0
        #self.ENDPOINT_IN = 0x81 # if bootloader v4.x
        self.ENDPOINT_IN = 0x82 # if bootloader v2.x
        self.ENDPOINT_OUT = 0x01
        
        self.device = None
        self.handle = None

        for bus in usb.busses():
            for dev in bus.devices:
                # Cuando encuentra el pinguino con botlace 2.x  
                if dev.idVendor == self.VENDOR and dev.idProduct == self.PRODUCT:
                    self.device = dev # crea un dispositivo usb
                    #print self.device
                #else: print "error"  
    
    def pinguino_open(self):
        if not self.device:
            print >> sys.stderr, "Unable to find device!"
            return None
        try:
            self.handle = self.device.open()
            self.handle.setConfiguration(self.CONFIGURATION)
            self.handle.claimInterface(self.INTERFACE)
        except usb.USBError, err:
            print >> sys.stderr, err
            self.handle = None
        return self.handle
            
    def pinguino_read(self, length, timeout = 0):
        print 
        return self.handle.bulkRead(self.ENDPOINT_IN, length, timeout)            
            
        
    def pinguino_update(self):
        self.INTERVAL = 10000 # intervalo (tiempo) de lectura 
        self.deg = unichr(176).encode("utf-8")
        self.myString = ''
        
        # get data from Pinguino board
        try:
            for i in self.pinguino_read(2, self.INTERVAL):
                #print chr(i)
                #print type(myString)
                self.myString += chr(i) # es tipo str()
            
        except usb.USBError as err:
            pass
        
        if self.myString == "0":
            print "es cero"
        else :
            print "cualquier valor, no es cero"

        
"""    
#-------------------------------------------------------------------------------
# Pinguino Class by Marin Purgar (marin.purgar@gmail.com)
#-------------------------------------------------------------------------------
class Pinguino():


    def close(self):
        try:
            self.handle.releaseInterface()
        except Exception, err:
            print >> sys.stderr, err
        self.handle, self.device = None, None

    def read(self, length, timeout = 0):
        return self.handle.bulkRead(self.ENDPOINT_IN, length, timeout)

    def write(self, buffer, timeout = 0):
        return self.handle.bulkWrite(self.ENDPOINT_OUT, buffer, timeout)


"""
"""
#-------------------------------------------------------------------------------
# update
#-------------------------------------------------------------------------------
def update():
    INTERVAL = 10000 # intervalo (tiempo) de lectura 
    deg = unichr(176).encode("utf-8")
    myString = ''

	# get data from Pinguino board
    try:
        for i in pinguino.read(15, INTERVAL):
            #print chr(i)
            #print type(myString)
            myString += chr(i)
        
    except usb.USBError as err:
        pass
    #print "myString",myString 
    if len(myString) > 0:
        #print 't =',t    # debug
        #print "myString if:",myString 
        return True
    else:
        return False                
    # recall every 500ms
    #HelloWorld.canvas.after(INTERVAL, update)
"""    
            
def main():
    # Nuevamente, esto es estándar, será igual en cada 
    # aplicación que escribas
    app = QtGui.QApplication(sys.argv)
    # Se crea una instancia de la clase
    ventana=Principal()
    # Se muestra el elemento en pantalla
    ventana.show()
    # Se ejecuta y expera a que termine la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()