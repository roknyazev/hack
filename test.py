import sys
from PyQt5.QtWidgets import QApplication
import mainwindow



def start():
    app = QApplication(sys.argv)
    form = mainwindow.MainWindow()
    form.show()
    sys.exit(app.exec_())

start()