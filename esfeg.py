import sys
from PyQt5.QtWidgets import *
import folium
import untitled_1
import io
from PyQt5 import QtWidgets, QtWebEngineWidgets


app = QtWidgets.QApplication(sys.argv)
m = folium.Map(
    location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13
)

data = io.BytesIO()
m.save(data, close_file=False)
w = QtWebEngineWidgets.QWebEngineView()
w.setHtml(data.getvalue().decode())
w.resize(640, 480)
w.show()
sys.exit(app.exec_())