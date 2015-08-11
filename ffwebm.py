#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QPushButton, 
	QFileDialog, QApplication, QInputDialog, QLabel)
from PyQt5.QtGui import QIcon 

class FFwebm(QMainWindow):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		#buttons
		self.openbtn = QPushButton("Select File", self)
		self.openbtn.setShortcut("Ctrl+O")
		self.openbtn.move(20, 10)
		self.openbtn.clicked.connect(self.showFileDialog)

		self.btnfrom = QPushButton("Time [From]", self)
		self.btnfrom.move(20, 75)
		self.btnfrom.clicked.connect(self.showInputTime)

		self.btnto = QPushButton("Time [To]", self)
		self.btnto.move(20, 105)
		self.btnto.clicked.connect(self.showInputTime2)

		self.btnsave = QPushButton("Save as", self)
		self.btnsave.setShortcut("Ctrl+S")
		self.btnsave.move(20, 250)
		self.btnsave.clicked.connect(self.showSaveDialog)

		#labels
		self.qlpath = QLabel("", self)
		self.qlpath.setFixedWidth(500)
		self.qlpath.move(130, 35)

		self.qlfrom = QLabel("", self)
		self.qlfrom.move(130,75)

		self.qlto = QLabel("", self)
		self.qlto.move(130, 105)

		self.qlsave = QLabel("", self)
		self.qlsave.setFixedWidth(500)
		self.qlsave.move(130, 250)

		# main window
		self.setGeometry(300, 300, 650, 300)
		self.setFixedSize(650, 300)
		self.setWindowTitle("FFWebM")
		self.show()

	def showFileDialog(self):

		fpath = QFileDialog.getOpenFileName(self, "Select file", " ")[0]

		self.qlpath.setText(str(fpath))

	def showSaveDialog(self):

		spath = QFileDialog.getSaveFileName(self, "Save as", ".webm")[0]

		self.qlsave.setText(str(spath))

	def showInputTime(self):

		text, ok = QInputDialog.getText(self, "Input Time",
			"Enter time hh:mm:ss (i.e. 1min22s = 00:01:22):")

		if ok:
			self.qlfrom.setText(str(text))

	def showInputTime2(self):

		text, ok = QInputDialog.getText(self, "Input Time",
			"Enter time hh:mm:ss (i.e. 1min22s = 00:01:22):")

		if ok:
			self.qlto.setText(str(text))

	def collectParams(self):

		mainString = "ffmpeg -i {} -c:v libvpx -quality good -cpu-used 0 -an -vf scale={}:-1 -ss {} -to {} {}"


if __name__ == "__main__":

	app = QApplication(sys.argv)
	ff = FFwebm()
	sys.exit(app.exec_())