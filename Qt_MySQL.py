import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLineEdit
import MySQL_Op

class Example(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#窗口设置
		self.setGeometry(300,300,300,320)
		self.setWindowTitle('聊天室')
		self.setWindowIcon(QIcon('timg.jpg')) #设置窗口图标
		#按钮设置
		btn = QPushButton('Button', self)
		btn.move(200, 200)
		btn.resize(100,120)
		btn.clicked.connect(self.Onchanged)
		#消息框
		self.textbox = QLineEdit(self)
		self.textbox.move(0, 200)
		self.textbox.resize(200, 120)
		#label设置
		self.lb1 = QLabel(self)
		self.show()
	
	def Onchanged(self, text):
		txt = self.textbox.text()
		MySQL_Op.InsertTB(txt)
		self.lb1.setText(txt)
		self.lb1.adjustSize()
	





if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_()) 