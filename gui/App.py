#!/bin/python3
import mainwindow;
import os;
import sys;
import netifaces;
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox;


class App(QWidget, mainwindow.Ui_Dialog):
	
	def __init__(self, parent = None):
		super(App, self).__init__(parent)
		self.setupUi(self)
		self.setWindowTitle("Create AP UI");
		self.setFixedSize(self.size())
		self.setGeometry(240,240, self.size().width(), self.size().height());
		self.sourceComboBox.addItems(netifaces.interfaces())
		self.sharingComboBox.addItems(netifaces.interfaces())

	def accept(self):
		source = self.sourceComboBox.currentText()
		sharing = self.sharingComboBox.currentText()
		ssid = self.ssidEdit.displayText()
		password = self.passwordEdit.displayText()
		internetAvaible = self.shareInternetCheckBox.isChecked();

		print("Accepted")
		self.create_ap(source, sharing, ssid, password, internetAvaible)
		

	def reject(self):
		sys.exit()
	 
	def showErrorDialog(self, message):
		  print(message);
	#commands
	def create_ap(self, source, sharing, ssid, password, internetAvaible):
		flag = ""
		if not internetAvaible:
			flag = "-n"
		command = "create_ap {} {} {} {} {}".format(flag, sharing, source, ssid, password)
		print(command)
		os.system(command)
	
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = App()
	form.show()
	app.exec_()

