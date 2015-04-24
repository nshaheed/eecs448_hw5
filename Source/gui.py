#!/usr/bin/python3.4

#Author: Robert Winslow
#Date: 2015-04-24
#Purpose: EECS 448 HW 5
#This program creates and updates a gui which allows the user to select which classification methods to use on a database of chemical compounds, and then displays the accuracy of these classification methods.

from PyQt4 import QtCore, QtGui
import sys

import classifier
import readfile
import vector_handler
import ratio


class calcHandler:
    def __init__(self):
        self.method = 0
        self.data = [None,None,None,None,None]
        self.values = [None,None,None,None,None]
        self.maximum = None
        self.names = [' Eucl Dist', ' Maha Dist', ' Eucl Vote', ' Maha Vote', '  Custom']

        file1 = open("hw5db1.txt","r")
        file2 = open("hw5db2.txt","r")
        dataIn = readfile.readFile(file1)
        stats = readfile.readStats(file2)

        self.vectors = vector_handler.vector_holder(dataIn,stats)
        self.classifier = classifier.classifier()
        
    def setMethod(self, method):
        self.method = method
        
    def calc(self):
        #Calculate the array of results if we need to, and then calculate the ratio.
        if self.method in range(0,4):
            if not self.data[self.method]:
                self.calcData(self.method)
            self.values[self.method] = ratio.ratio(self.data[self.method])
        #For custom measure, calculate all uncalculated methods and then use them to calculate the final
        elif 4 == self.method:
            if not self.data[4]:
                for i,x in enumerate(self.data):
                    if (x == None) and i < 4:
                        #print(i)
                        self.calcData(i)
                self.data[4] = []
                for i in range(0, len(self.data[0])):
                    self.data[4].append(self.classifier.customClassify(self.data[0][i], self.data[1][i], self.data[2][i], self.data[3][i]))
            self.values[4] = ratio.ratio(self.data[4])
            
        self.maximum = max([x for x in self.values if x])

    def calcData(self, x):
        if x == 0:
            print('Calculating Euclidean Distance')
            self.data[0] = self.classifier.directClassify(self.vectors.vectorArr,self.vectors.statArr,self.classifier.method_1)
        elif x == 1:
            print('Calculating Maha Distance')
            self.data[1] = self.classifier.directClassify(self.vectors.vectorArr,self.vectors.statArr,self.classifier.method_2)
        elif x == 2:
            print('Calculating Euclidean Voting')
            self.data[2] = self.classifier.votingClassify(self.vectors.vectorArr,self.vectors.statArr,self.classifier.method_3)
        elif x == 3:
            print('Calculating Maha Voting')
            self.data[3] = self.classifier.votingClassify(self.vectors.vectorArr,self.vectors.statArr,self.classifier.method_4)
        print('Calculations Complete')
            



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
        #This triggers uppon window resize
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
            qp.drawRect(45, 350, 10, 0)
            #Label text
            qp.drawText(100,120, 'Ratio of True Positives to False Postives')
            qp.drawText(15,155,'%.3f' % self.m.maximum)
            qp.drawText(35,355,'0')
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





def main():
    app = QtGui.QApplication(sys.argv)
    m = calcHandler()
    ui = UI(m)    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
