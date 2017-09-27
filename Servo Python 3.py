import sys
from PyQt5 import QtWidgets,uic
import serial, time

qtCreatorFile = "Servo PyQt 5.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
                QtWidgets.QMainWindow.__init__(self)
                Ui_MainWindow.__init__(self)
                self.setupUi(self)
                self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
                self.pushButton_KirimData.clicked.connect(self.send)

                self.textEdit_LogMessage.append("Tugas Mikrokontroler")
                self.pushButton_KirimData.setEnabled(False)

        def OpenSerial(self):
                if self.pushButton_OpenSerial.text()=='Open Serial':
                        self.ser = serial.Serial("COM3", "9600", timeout=0.1)
                        if self.ser.isOpen():
                                self.pushButton_OpenSerial.setText('Close Serial')
                                self.textEdit_LogMessage.append("Port Opening")
                                self.pushButton_KirimData.setEnabled(True)
                        else:
                                self.textEdit_LogMessage.append("can not open serial port")
                else:
                        if self.ser.isOpen():
                                self.ser.close()
                        self.pushButton_OpenSerial.setText('Open Serial')
                        self.textEdit_LogMessage.append("Closing serial port... OK")
                        self.pushButton_KirimData.setEnabled(False)

        def send(self):
                self.PWM  = self.horizontalSlider_PWM.value()
                self.TXdata = bytearray(2)
                self.TXdata[0]=self.PWM
                self.textEdit_LogMessage.append("Sending PWM = " + (bytes(self.TXdata)).decode())
                self.ser.write(self.TXdata)
                time.sleep(2)


                line = ''
                line = (self.ser.readline()).decode()
                self.textEdit_LogMessage.append(line)

                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
