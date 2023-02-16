from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QTextEdit
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon,QPixmap
from data.weather_inf import get_weather
class MainWeather(QMainWindow):
    def __init__(self,width=500,height=500,title="Weather app"):
        super().__init__()
        self.city_name = "фергана"
        self.setWindowTitle(title)
        self.setGeometry(250,250,width,height)
        self.photo_temp=QLabel()
        icon_title=QIcon("image//temp.png")
        far_icon=QIcon("image//f.png")
        tempe=QPixmap("image//hot.png").scaled(QtCore.QSize(150,150))
        self.setWindowIcon(icon_title)
        self.fbutton=QPushButton(far_icon,"Farg'ona",self)
        self.fbutton.setGeometry(80,50,100,50)
        self.fbutton.adjustSize()
        self.fbutton.setStyleSheet('background-color:#5CEA77;color:black;border-radius:10px;')
        an_icon=QIcon("image//letter-a.png")
        self.abutton=QPushButton(an_icon,"Andijon",self)
        self.abutton.setGeometry(180,50,100,50)
        self.abutton.adjustSize()
        self.abutton.setStyleSheet('background-color:#5CEA77;color:black;border-radius:10px;')
        nm_icon=QIcon("image//letter-n.png")
        self.nbutton=QPushButton(nm_icon,"Nukus",self)
        self.nbutton.setGeometry(270,50,100,50)
        self.nbutton.adjustSize()
        self.nbutton.setStyleSheet('background-color:#5CEA77;color:black;border-radius:10px;')
        t_icon=QIcon("image//letter-t.png")
        self.tbutton=QPushButton(t_icon,"Tashkent",self)
        self.tbutton.setGeometry(370,50,100,50)
        self.tbutton.adjustSize()
        self.tbutton.setStyleSheet('background-color:#5CEA77;color:black;border-radius:10px;')
        self.ubutton=QPushButton("Update",self)
        self.ubutton.setGeometry(30,350,100,50)
        self.ubutton.adjustSize()
        self.ubutton.setStyleSheet('background-color:yellow;color:black;border-radius:10px;')
        self.sbutton=QPushButton("send",self)
        self.sbutton.setGeometry(140,350,100,50)
        self.sbutton.adjustSize()
        self.sbutton.setStyleSheet('background-color:yellow;color:black;border-radius:10px;')
        self.qbutton=QPushButton("Quit",self)
        self.qbutton.setGeometry(280,350,100,50)
        self.qbutton.adjustSize()
        self.qbutton.setStyleSheet('background-color:yellow;color:black;border-radius:10px;')
        self.temp_img=QLabel(self)
        self.temp_img.setPixmap(tempe)
        self.temp_img.setGeometry(250,160,150,150)
        self.havo=QLabel("<b>Ob-Havo holati</b>",self)
        self.havo.setGeometry(150,150,250,50)
        self.temp=QLabel("<b>Harorat</b>",self)
        self.temp.setGeometry(150,200,250,50)
        self.tsh=QLabel("<b>Shamol</b>",self)
        self.tsh.setGeometry(150,250,250,50)
        self.fbutton.clicked.connect(self.far_temp)
        self.abutton.clicked.connect(self.and_temp)
        self.nbutton.clicked.connect(self.nam_temp)
        self.tbutton.clicked.connect(self.tash_temp)
        self.qbutton.clicked.connect(QApplication.quit)
        self.ubutton.clicked.connect(self.update)


    def far_temp(self):
        temp=get_weather(city="фергана")
        self.city_name = "фергана"
        self.temp.setText("<b>Harorat</b>: "+temp[1])
        self.tsh.setText("<b>Shamol</b>: "+temp[0])
        self.havo.setText("<b>Ob-Havo</b>: "+temp[2])
    def nam_temp(self):
        temp=get_weather(city="нукус")
        self.city_name = "нукус"
        self.temp.setText("<b>Harorat</b>: "+temp[1])
        self.tsh.setText("<b>Shamol</b>: "+temp[0])
        self.havo.setText("<b>Ob-Havo</b>: "+temp[2])

    def tash_temp(self):
        temp=get_weather(city="ташкент")
        self.city_name = "ташкент"
        self.temp.setText("<b>Harorat</b>: "+temp[1])
        self.tsh.setText("<b>Shamol</b>: "+temp[0])
        self.havo.setText("<b>Ob-Havo</b>: "+temp[2])
    def and_temp(self):
        temp=get_weather(city="андижан")
        self.city_name = "андижан"
        self.temp.setText("<b>Harorat</b>: "+temp[1])
        self.tsh.setText("<b>Shamol</b>: "+temp[0])
        self.havo.setText("<b>Ob-Havo</b>: "+temp[2])
    def update(self):
        temp=get_weather(city=self.city_name)
        self.temp.setText("<b>Harorat -</b>: "+temp[1])
        self.tsh.setText("<b>Shamol</b>: "+temp[0])
        self.havo.setText("<b>Ob-Havo</b>: "+temp[2])




    

