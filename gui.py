#!/usr/bin/python34

from PyQt4 import QtCore, QtGui
import sys


class calcHandler:
    def __init__(self):
        self.method = 0
    def setMethod(self, method):
        self.method = method


class UI(QtGui.QWidget):

    def __init__(self, model):
        super(UI,self).__init__()
        self.initiation()
        self.m = model

    def initiation(self):
        
        
        #seperator
        line = QtGui.QFrame(self)
        line.setFrameShape(QtGui.QFrame.WinPanel)
        line.setLineWidth(3)
        line.setFrameShadow(QtGui.QFrame.Raised)
        line.resize(400,80)

        #Calculate button
        calc_btn = QtGui.QPushButton('Calculate', self)
        calc_btn.resize(180,40)
        calc_btn.move(200,20)

        #method selection
        method_lbl = QtGui.QLabel("Choose Analysis Method:", self)
        method_lbl.move(20,20)
        method_combo = QtGui.QComboBox(self)
        method_combo.addItem("1-Euclidean Distance")
        method_combo.addItem("2-Maha Distance")
        method_combo.addItem("3-Euclidean Voting")
        method_combo.addItem("4-Maha Voting")
        method_combo.addItem("5-Custom Aggregate")
        method_combo.move(20,40)

        

        #Hook up callbacks. 
        calc_btn.clicked.connect(self.clickCalc)
        method_combo.currentIndexChanged.connect(self.setMethod)

        #window
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Chemical Analysis')    
        self.show()

    def setMethod(self):
        sender = self.sender()
        self.m.setMethod(sender.currentIndex())
    def clickCalc(self):
        print(self.sender().text() + str(self.m.method))





def main():
    app = QtGui.QApplication(sys.argv)
    m = calcHandler()
    ui = UI(m)    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
