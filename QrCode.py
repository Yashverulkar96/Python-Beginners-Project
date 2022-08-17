import pyqrcode
from pyqrcode import QRCode
s="https://www.w3schools.com/python"
url=pyqrcode.create(s)
url.svg("w3school1.svg",scale=8)