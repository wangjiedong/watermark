# coding=utf-8

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
import sys, os, sip

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':

    app = QApplication([])

    dwidth = app.desktop().width()
    dheight= app.desktop().height()
    
    translator = QTranslator()
    translator.load("qm/qt_zh_CN.qm")
    app.installTranslator(translator)

    print "mainwindow"
    mainwindow = MainWindow()
    mainwindow.setFixedSize(dwidth, dheight)
    mainwindow.setObjectName("MainWindow")
    mainwindow.show()

    app.exec_()

