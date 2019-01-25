#coding=utf-8
from PyQt5.QtGui import QTransform, QColor,QPainter, QFont
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import qsrand, Qt, QPoint
import os, random, socket, uuid

class MainWindow(QWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput | Qt.Tool | Qt.BypassWindowManagerHint)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog )

        self.setAttribute(Qt.WA_TranslucentBackground)


    def get_hostip(self):
        """
        for internet
        """
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('192.168.10.110', 80))
            ip = s.getsockname()[0]
        except:
            ip = '127.0.0.1'
        finally:
            s.close()

        return ip


    def get_hostmac(self):
        mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e+2] for e in range(0,11,2)])


    def get_replicate_text(self):
        i,space,str1,str2 = 0,20,"",""

        hostmac = self.get_hostmac()
        hostip  = self.get_hostip()
        text    = "MACADDRESS:"+ hostmac + " "*space +"IPADDRESS:" + hostip

        while (i <= 3):
            str1 = str1 + text + " "*space*2
            i = i + 1
        str2 = " "*space + str1 + "\n\n\n\n"
        str1 = str1 + "\n\n\n\n"
        str1 = "\n\n" + (str1 + str2) * 6
        return str1 


    def paintEvent(self,event):

        #Q_UNUSED(event)

        des = QApplication.desktop()
        #self.setTransformOriginPoint(des.size().width()/2 , des.size().height()/2)
        painter = QPainter(self)
        painter.save()
        #painter.setFont(QFont("Arial", 20))
        painter.setFont(QFont("Batang", 20))
        painter.setPen(QColor(112, 146, 190))
        transform = QTransform()
        #transform.translate(des.size().width()/2 , des.size().height()/2)
        transform.rotate(-25)
        painter.setTransform(transform);
        x, y = -64, 100
        row = 0
        qsrand(255)
        while(y < des.size().height()*2):
            x = 64 - 100 * row
            colorV = random.randint(1,255)
            #qDebug() << "colorV " << colorV
            #painter.setPen(QColor(128, 128, colorV, 24))
            while(x < des.size().width()):
                painter.drawText(x, y, "MAC:" + self.get_hostmac() + "  IP:" + self.get_hostip())
                x = x + 600
            y = y + 164
            row = row + 1

        #painter.drawText(x, y, self.get_replicate_text())

        painter.restore()
