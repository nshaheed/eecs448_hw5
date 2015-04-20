from PyQt4 import QtCore, QtGui
import sys





class UI(QtGui.QWidget):

    def __init__(self):
        super(UI,self).__init__()
        self.initiation()


    def initiation(self):
        self.method = 0
        
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
        self.method = sender.currentIndex()
    def clickCalc(self):
        print(self.sender().text() + str(self.method))





def main():
    app = QtGui.QApplication(sys.argv)
    ui = UI()    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
