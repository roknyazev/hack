import sys
from PyQt5.QtWidgets import *

import untitled_1
import io
from PyQt5 import *
import pyqtgraph as pg
import sqlite3
import random
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import thread
import hub


class MainWindow(QMainWindow, untitled_1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.output_GUI_Hubs()
        self.output_GUI_Track()

        self.pushButton_9.clicked.connect(self.mini_hub)
        self.pushButton_8.clicked.connect(self.midl_hub)
        self.pushButton_7.clicked.connect(self.xl_hub)
        self.pushButton_5.clicked.connect(self.db_hub)
        self.pushButton_6.clicked.connect(self.remove_db_hub)
        self.pushButton.clicked.connect(self.db_tracks)
        self.pushButton_2.clicked.connect(self.remove_db_tracks)
        self.fig = None
        self.ax = None
        self.canvas = None
        self.widget = None
        self.map()
        self.thread_instance1 = thread.thread()
        thread.sender1.data.connect(self.update_map)

        for hub_elem in hub.hub_list:
            if hub_elem.type == 0:
                color = 'blue'
                size = 50
            if hub_elem.type == 1:
                color = 'green'
                size = 150
            if hub_elem.type == 2:
                color = 'red'
                size = 250
            plt.scatter(hub_elem.coordinates[0], hub_elem.coordinates[1], facecolor=color, s=size)

        self.points = []


    def db_tracks(self): #база данных заказов
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        index = random.randint(0,100000)
        sql.execute(f"INSERT INTO 'TRACKS' VALUES (?,?,?,?,?)", (index, self.lineEdit_3.text(),self.lineEdit.text(), self.lineEdit_2.text(), datetime.now()))
        db.commit()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.output_GUI_Track()

    def db_hub(self):
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        index = random.randint(0,10000)
        name = str(self.lineEdit_9.text()) + "_Cargo_" + str(self.lineEdit_11.text()) + '_' + str(self.lineEdit_10.text())
        sql.execute(f"INSERT INTO 'HUBS' VALUES (?,?,?,?,?)", (index, name, float(self.lineEdit_9.text()),float(self.lineEdit_11.text()), float(self.lineEdit_10.text())))
        db.commit()
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.output_GUI_Hubs()

    def output_GUI_Hubs(self):
        z = 0
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        z = sql.execute(f'SELECT * FROM "HUBS"')
        c = 0
        for i in z:
            #print(i[0])
            table = self.tableWidget_2
            table.setColumnCount(5)
            table.setRowCount(c+1)
            table.setHorizontalHeaderLabels(["id", "name", "type","lat","long"])
            table.setItem(c, 0, QTableWidgetItem(str(i[0])))
            table.setItem(c, 1, QTableWidgetItem(str(i[1])))
            table.setItem(c, 2, QTableWidgetItem(str(i[2])))
            table.setItem(c, 3, QTableWidgetItem(str(i[3])))
            table.setItem(c, 4, QTableWidgetItem(str(i[4])))
            table.resizeColumnsToContents()
            db.commit()
            c = c + 1
        #self.grid_layout.addWidget(table, 0, 0)

    def output_GUI_Track(self):
        z = 0
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        z = sql.execute(f'SELECT * FROM "TRACKS"')
        c = 0
        for i in z:
            # print(i[0])
            table_1 = self.tableWidget
            table_1.setColumnCount(5)
            table_1.setRowCount(c + 1)
            table_1.setHorizontalHeaderLabels(["id", "cargo", "hub start", "hub point", "time"])
            table_1.setItem(c, 0, QTableWidgetItem(str(i[0])))
            table_1.setItem(c, 1, QTableWidgetItem(str(i[1])))
            table_1.setItem(c, 2, QTableWidgetItem(str(i[2])))
            table_1.setItem(c, 3, QTableWidgetItem(str(i[3])))
            table_1.setItem(c, 4, QTableWidgetItem(str(i[4])))
            table_1.resizeColumnsToContents()
            db.commit()
            c = c + 1
        # self.grid_layout.addWidget(table, 0, 0)

    def remove_db_hub(self):
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        m = int(self.lineEdit_12.text())
        #print (m)
        sql.execute(f'DELETE FROM HUBS WHERE id = "{m}"')

        self.lineEdit_12.setText("")
        db.commit()
        self.output_GUI_Hubs()

    def remove_db_tracks(self):
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        m = int(self.lineEdit_4.text())
        # (m)
        sql.execute(f'DELETE FROM TRACkS WHERE id = "{m}"')
        db.commit()
        self.lineEdit_4.setText("")
        self.output_GUI_Track()

    def mini_hub(self):

        self.lineEdit_9.setText("1")

    def midl_hub(self):
        self.lineEdit_9.setText("2")


    def xl_hub(self):
        self.lineEdit_9.setText("3")
        

    def map(self):
        db = sqlite3.connect('logistic.db')
        sql = db.cursor()
        z = sql.execute(f'SELECT * FROM "HUBS"')
        c = 0
        self.widget = self.label_7
        self.widget.setLayout(QGridLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)
        self.fig, self.ax = plt.subplots()
        self.ax.set_facecolor('white')
        self.fig.patch.set_facecolor('lightgrey')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.widget.layout().addWidget(self.canvas, 0, 0)

    def update_map(self, data):
        for point in self.points:
            point.remove()
        self.points = []
        for elem in data:
            if elem is None:
                continue
            x = elem[0]
            y = elem[1]
            self.points.append(self.ax.scatter(x, y, facecolor='orange', s=10))
        self.canvas.draw()

    def start(self):
        self.thread_instance1.start()


