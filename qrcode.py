import pyqrcode 
from pyqrcode import QRCode
link = "https://www.python.org/"
url = pyqrcode.create(link)
url.svg("D:\Casual\pythonprog/welcometopython.svg", scale = 10) 