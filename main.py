from complete_graph import *
import random
import time

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

    for hub in hub_list:
        hub.start_uav()

    for i in range(100):

        for elem in uav_list:
            print(elem.get_current_position(time.time()))

    for hub in hub_list:
        hub.start_uav()

    for i in range(100):

        for elem in uav_list:
            print(elem.get_current_position(time.time()))


if __name__ == '__main__':
    test()

    for hub in hub_list:
        if hub.type == 0:
            color = 'blue'
            size = 50
        if hub.type == 1:
            color = 'green'
            size = 150
        if hub.type == 2:
            color = 'red'
            size = 250
        plt.scatter(hub.coordinates[0], hub.coordinates[1], facecolor=color, s=size)
    plt.show()
    
    print("\nend")
