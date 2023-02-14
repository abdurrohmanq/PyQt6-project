from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QTextEdit
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon,QPixmap
from data.weather_inf import get_weather
class MainWeather(QMainWindow):
    def __init__(self,width=500,height=500,title="Weather app"):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(250,250,width,height)
        self.photo_temp=QLabel()
        icon_title=QIcon("image//temp.png")
        far_icon=QIcon("image//f.png")
        tempe=QPixmap("image//hot.png").scaled(QtCore.QSize(70,70))
        self.setWindowIcon(icon_title)
        self.fbutton=QPushButton(far_icon,"Farg'ona",self)
        self.fbutton.setGeometry(10,10,100,50)
        self.fbutton.adjustSize()
       # self.setStyleSheet("QPushButton {background}")
        self.abutton=QPushButton("Andijon",self)
        self.abutton.setGeometry(120,10,100,50)
        self.abutton.adjustSize()
        self.nbutton=QPushButton("Namangan",self)
        self.nbutton.setGeometry(240,10,100,50)
        self.nbutton.adjustSize()
        self.tbutton=QPushButton("Tashkent",self)
        self.tbutton.setGeometry(360,10,100,50)
        self.tbutton.adjustSize()
        self.temp_img=QLabel(self)
        self.temp_img.setPixmap(tempe)
        self.temp_img.setGeometry(300,160,150,150)
        self.temp=QLabel("Harorat",self)
        self.temp.setGeometry(20,200,150,50)
        self.fbutton.clicked.connect(self.far_temp)
        self.abutton.clicked.connect(self.and_temp)
        self.nbutton.clicked.connect(self.nam_temp)
        self.tbutton.clicked.connect(self.tash_temp)
    def far_temp(self):
        temp=get_weather(city="фергана")
        self.temp.setText("Harorat: "+temp)
    def and_temp(self):
        temp=get_weather(city="андижан")
        self.temp.setText("Harorat: "+temp)
    def nam_temp(self):
        temp=get_weather(city="наманган")
        self.temp.setText("Harorat: "+temp)
    def tash_temp(self):
        temp=get_weather(city="ташкент")
        self.temp.setText("Harorat: "+temp)



    

