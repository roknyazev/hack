from complete_graph import *
import random
import time

import sys
from PyQt5.QtWidgets import QApplication
import mainwindow
import pandas as pd
import matplotlib.pyplot as plt


from hub import *
from package import *


def test():
    for i in range(10):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hub_list.append(Hub((x, y), i, random.randint(0, 2)))

    hub_identifiers = []
    for hub in hub_list:
        hub_identifiers.append([hub.identifier, hub.coordinates])
    graph = complete_graph(hub_identifiers)

    for i in range(1000):
        print(i)
        start = random.randint(0, 9)
        destination = random.randint(0, 9)
        package = Package(hub_identifiers[start], hub_identifiers[destination], graph)
        hub_list[start].append_storage(package)


if __name__ == '__main__':
    test()

    app = QApplication(sys.argv)
    form = mainwindow.MainWindow()
    form.show()
    form.start()
    sys.exit(app.exec_())
