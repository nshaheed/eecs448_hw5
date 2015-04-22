#!/usr/bin/python34

from PyQt4 import QtCore, QtGui
import sys
import random


class calcHandler:
    def __init__(self):
        self.method = 0
        self.values = [None,None,None,None,None]
        self.maximum = None
        self.names = [' Eucl Dist', ' Maha Dist', ' Eucl Vote', ' Maha Vote', '  Custom']
    def setMethod(self, method):
        self.method = method
    def calc(self):
        if 0 == self.method:
            self.values[0] = 2*random.random()
        elif 1 == self.method:
            self.values[1] = random.random()
        elif 2 == self.method:
            self.values[2] = random.random()
        elif 3 == self.method:
            self.values[3] = random.random()
        elif 4 == self.method:
            self.values[4] = random.random()
        self.maximum = max([x for x in self.values if x]+[1])

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

    def paintEvent(self,e):
        
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawGraph(qp)
        qp.end()
        
    def drawGraph(self, qp):
        if self.m.maximum:
            color = QtGui.QColor(100, 100, 100)
            #color.setNamedColor('#d4d4d4')
            qp.setPen(color)
            #axis lines
            qp.setBrush(QtGui.QColor(0, 0, 0))
            qp.drawRect(50, 350, 300, 0)
            qp.drawRect(50, 150, 0, 200)
            qp.drawRect(45, 150, 10, 0)
            #Label text
            qp.drawText(25,155,'%.1f' % self.m.maximum)
            #data bars
            qp.setBrush(QtGui.QColor(150, 0, 0))
            for i,x in enumerate(self.m.values):
                if x:
                   qp.drawRect(60+i*55, 350-200*(x/self.m.maximum), 50, 200*(x/self.m.maximum))
                   qp.drawText(60+i*55, 365 ,self.m.names[i])

        


    def setMethod(self):
        sender = self.sender()
        self.m.setMethod(sender.currentIndex())
        
    def clickCalc(self):
        self.m.calc()
        self.update()
        #self.paintEvent()
        #self.disp_lbl.setText(viewGraph(self.m.values, self.m.max))
        #self.disp_lbl.setText('hh\nlklk')





def main():
    app = QtGui.QApplication(sys.argv)
    m = calcHandler()
    ui = UI(m)    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
