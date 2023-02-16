import requests
from bs4 import BeautifulSoup
from PyQt6.QtGui import QIcon,QPixmap
def get_weather(city):
   weather=requests.get(f"https://sinoptik.ua/погода-{city}")
   soup=BeautifulSoup(weather.content)
   s=soup.find("div",class_="Tooltip wind wind-E").text
   h=soup.find("td",class_="p2 bR").text
   temp=soup.find("p",class_="today-temp").text
   return (s,temp,h)
