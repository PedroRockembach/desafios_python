import sys
from PySide import QtCore, QtGui

app = QtGui.QApplication(sys.argv)

win = QtGui.QWidget()

win.resize(320, 240)  
win.setWindowTitle("Olá, Mundo!") 
win.show()  

sys.exit(app.exec_())