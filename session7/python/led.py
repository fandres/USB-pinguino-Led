# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 21:13:10 2014

@author: fAnDrEs

Board pinguino: https://github.com/fandres/USB-pinguino-Led/tree/master/session7/pinguino

<< Iconos Flamini 0.3            License: GPL         [kotus.works@gmail.com] >>
<< Pinguino by Marin Purgar (marin.purgar@gmail.com)                          >>

"""

import sys
# Importa todos los elementos necesarios para PyQt
# Importar modulo Qt
from PyQt4 import QtCore,QtGui
# Importar el código del modulo compilado UI
from ledUi import Ui_Form
# Importamos Modulos para el manejo de USB
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
        # Centra el Frame
        self.centrar_frame()

        self.connect(self.ui.boton_iniciar, QtCore.SIGNAL("clicked()"), self.inicio)

    #--------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_boton_led1_clicked(self):
        if self.ui.kled_1.state() == 0 :
            self.ui.kled_1.on() # Enciende el led en la ui
            self.ui.boton_led1.setText("Off") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led1.setIcon(icon2)
            # Enviamos al pinguino la sen^al de estado alto en el pin 7
            # en la board pinguino se compara con respecto a este valor
            # '1' == Encender led 7 del pinguino  
            self.actualizar('1')  
            #print self.pinguino.pinguinoRead(2, 100)

        else:
            self.ui.kled_1.off() # Enciende el led en la ui
            self.ui.boton_led1.setText("On") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led1.setIcon(icon1)
            # Enviamos al pinguino la sen^al de estado bajo en el pin 7
            # en la board pinguino se compara con respecto a este valor
            # '2' == Apagar led 7 del pinguino  
            self.actualizar('2')  

    #--------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_boton_led2_clicked(self):
        if self.ui.kled_2.state() == 0 :
            self.ui.kled_2.on() # Enciende el led en la ui
            self.ui.boton_led2.setText("Off") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led2.setIcon(icon2)

            # Enviamos al pinguino la sen^al de estado alto en el pin 6
            # en la board pinguino se compara con respecto a este valor
            # '3' == Encender led 6 del pinguino  
            self.actualizar('3')  

        else:
            self.ui.kled_2.off() # Enciende el led en la ui
            self.ui.boton_led2.setText("On") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led2.setIcon(icon1)

            # Enviamos al pinguino la sen^al de estado bajo en el pin 6
            # en la board pinguino se compara con respecto a este valor
            # '4' == Apagar led 6 del pinguino  
            self.actualizar('4')  

    #--------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_boton_led3_clicked(self):
        if self.ui.kled_3.state() == 0 :
            self.ui.kled_3.on() # Enciende el led en la ui
            self.ui.boton_led3.setText("Off") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led3.setIcon(icon2)

            # Enviamos al pinguino la sen^al de estado alto en el pin 5
            # en la board pinguino se compara con respecto a este valor
            # '5' == Encender led 5 del pinguino  
            self.actualizar('5')  

        else:
            self.ui.kled_3.off() # Enciende el led en la ui
            self.ui.boton_led3.setText("On") # Cambia el titulo del boton_led1
            # Cambia el icono para el boton boton_led1
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.boton_led3.setIcon(icon1)

            # Enviamos al pinguino la sen^al de estado bajo en el pin 5
            # en la board pinguino se compara con respecto a este valor
            # '6' == Apagar led 5 del pinguino  
            self.actualizar('6')  


    ########-----------------------------------------------------------########
    def inicio(self):
        # Conexcion pinguino
        self.pinguino = Pinguino()
        
        self.ui.boton_iniciar.setEnabled(False)
        
        if self.pinguino.pinguinoOpen() == None:
            print >> sys.stderr, "Unable to open Pinguino device!"
            self.pinguino.pinguinoClose()
            # Cerrar aplicacion de manera correcta.
        else: 
            # Se habilita los botones "boton_ledx"
            self.ui.boton_led1.setEnabled(True)
            self.ui.boton_led2.setEnabled(True)
            self.ui.boton_led3.setEnabled(True)
            # Definir como salida los pines 5, 6 y 7
            # Pinguino  --- PC
            # Pin7 = Led 1 , Pin6 = Led 2, Pin5 = Led 3
        

    #--------------------------------------------------------------------------
    def actualizar(self, boton_onOff = None):
        self.boton_onOff = boton_onOff
        #print "parametro update",self.boton_onOff
        self.INTERVAL = 100 # intervalo (tiempo) de lectura
        #print self.INTERVAL
        #print self.boton_onOff
        try:
            if  self.boton_onOff != None :
                ##print "valor a ser enviado", self.boton_onOff
                self.pinguino.pinguinoWrite(self.boton_onOff, self.INTERVAL)

        except AttributeError as err:
            pass

    #--------------------------------------------------------------------------
    def pinguino_lectura(self):
        self.INTERVAL = 100 # intervalo (tiempo) de lectura
        deg = unichr(176).encode("utf-8")
        self.myString = ''

        # get data from Pinguino board
        try:
            for i in self.pinguino_read(2, self.INTERVAL):
                #print chr(i)
                #print type(myString)
                self.myString += chr(i) # es tipo str()

        except usb.USBError as err:
            pass

        """if self.myString == "0":
            print "es cero"
        else :
            print "cualquier valor, no es cero"
        """
        print "Valor recibido: ",self.myString
        

    def centrar_frame(self):
        vistaVentana = QtGui.QDesktopWidget().screenGeometry()
        escala =  self.geometry()
        self.move((vistaVentana.width()-escala.width())/2, (vistaVentana.height()-escala.height())/2)
        
#-------------------------------------------------------------------------------
# Pinguino Class by Marin Purgar (marin.purgar@gmail.com)
#-------------------------------------------------------------------------------

class Pinguino():

    VENDOR = 0x04D8
    PRODUCT = 0xFEAA
    #CONFIGURATION = 0x01 # if bootloader v4.x
    CONFIGURATION = 0x03 # if bootloader v2.x
    #print type(CONFIGURATION)
    INTERFACE = 0
       #ENDPOINT_IN = 0x81 # if bootloader v4.x
    ENDPOINT_IN = 0x82 # if bootloader v2.x
    ENDPOINT_OUT = 0x01

    device = None
    handle = None

    def __init__(self,):
        for bus in usb.busses():
            #print usb.busses()
            for dev in bus.devices:
                #print "vendor",dev.idVendor
                #print "idproduct",dev.idProduct
                if dev.idVendor == self.VENDOR and dev.idProduct == self.PRODUCT:
                    self.device = dev
        return None

    def pinguinoOpen(self):
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

    def pinguinoClose(self):
        try:
            self.handle.releaseInterface()
        except Exception, err:
            print >> sys.stderr, err
        self.handle, self.device = None, None

    def pinguinoRead(self, length, timeout = 0):
        return self.handle.bulkRead(self.ENDPOINT_IN, length, timeout)

    def pinguinoWrite(self, buffer, timeout = 0):
        return self.handle.bulkWrite(self.ENDPOINT_OUT, buffer, timeout)
        
        
#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

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
    # Cierra la conexcion con el pinguino Correctamente
    Principal.pinguino_close()

if __name__ == "__main__":
    main()