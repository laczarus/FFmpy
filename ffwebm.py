#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QPushButton, 
	QFileDialog, QApplication, QInputDialog, QLabel, QComboBox)
from PyQt5.QtGui import QIcon 
import subprocess

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

		self.btnscale = QPushButton("Scale", self)
		self.btnscale.move(220, 75)
		self.btnscale.clicked.connect(self.showInputScale)

		self.btnsave = QPushButton("Save as", self)
		self.btnsave.setShortcut("Ctrl+S")
		self.btnsave.move(20, 250)
		self.btnsave.clicked.connect(self.showSaveDialog)

		self.btnconv = QPushButton("Convert", self)
		self.btnconv.setShortcut("Ctrl+C")
		self.btnconv.move(500, 250)
		self.btnconv.clicked.connect(self.startConv)

		#combobox
		self.rotation = QComboBox(self)
		self.rotation.addItem("No Rotation")
		self.rotation.addItem("90° Clockwise + Vertical Flip")
		self.rotation.addItem("90° Clockwise")
		self.rotation.addItem("90° CounterClockwise")
		self.rotation.addItem("90° CounterClockwise + Vertical Flip")
		self.rotation.move(220, 105)
		self.rotation.activated[str].connect(self.onActivated)

		#labels
		self.qlpath = QLabel("", self)
		self.qlpath.setFixedWidth(400)
		self.qlpath.move(130, 10)

		self.qlfrom = QLabel("", self)
		self.qlfrom.move(130,75)

		self.qlto = QLabel("", self)
		self.qlto.move(130, 105)

		self.qlsave = QLabel("", self)
		self.qlsave.setFixedWidth(400)
		self.qlsave.move(130, 250)

		self.qlscale = QLabel("", self)
		self.qlscale.move(330, 75)

		self.qlrotation = QLabel("No Rotation", self)
		self.qlrotation.move(330, 110)

		# main window
		self.setGeometry(300, 300, 650, 300)
		self.setFixedSize(650, 300)
		self.setWindowTitle("FFWebM")
		self.show()

	def startConv(self):

		inputFile = str(self.qlpath.text())
		outputFile = str(self.qlsave.text())
		scale = "scale="+str(self.qlscale.text())+":-1"

		subprocess.call(["ffmpeg", "-i", ""+ inputFile +"", "-c:v", "libvpx", "-quality", "best", "-an", "-qmin", "10", "-qmax", "35", 
				"-vf", ""+scale+"", ""+ outputFile])

	def showFileDialog(self):

		fpath = QFileDialog.getOpenFileName(self, "Select file", " ")[0]

		self.qlpath.setText(str(fpath))

	def showSaveDialog(self):

		spath = QFileDialog.getSaveFileName(self, "Save as", ".webm")[0]

		self.qlsave.setText(str(spath))

	def showInputScale(self):
		scale = QInputDialog.getText(self, "Input Width",
			"Enter width (i.e. 1052 for 1052px)")[0]

		self.qlscale.setText(str(scale))

	def onActivated(self, text):

		self.qlrotation.setText(text)
		self.qlrotation.adjustSize()

	def showInputTime(self):

		text, ok = QInputDialog.getText(self, "Input Time",
			"Enter time hh:mm:ss (i.e. 1min22s = 00:01:22)")

		if ok:
			self.qlfrom.setText(str(text))

	def showInputTime2(self):

		text, ok = QInputDialog.getText(self, "Input Time",
			"Enter time hh:mm:ss (i.e. 1min22s = 00:01:22)")

		if ok:
			self.qlto.setText(str(text))

if __name__ == "__main__":

	app = QApplication(sys.argv)
	ff = FFwebm()
	sys.exit(app.exec_())