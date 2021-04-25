from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import hub
import time


class thread(QThread, QObject):
    def __init__(self):
        super().__init__()
        self.step = None
        self.precision = None
        self.t0 = None
        self.ft = None

    def run(self):
        for hub_elem in hub.hub_list:
            hub_elem.start_uav()

        print(len(hub.uav_list))
        while True:
            result = []
            time.sleep(0.7)
            #if int(time.time()) % 10 == 0:
            #    print(12345)
            #
            i = 0
            for uav_elem in hub.uav_list:
                result.append([uav_elem.get_current_position(time.time()), uav_elem.uav_type])
                if uav_elem.is_arrived is True:
                    print(i)
                    i += 1
            if i == len(hub.uav_list):
                print("New epoch")
                hub.uav_list = []
                for hub_elem in hub.hub_list:
                    hub_elem.start_uav()
            self.slot(result)

    @pyqtSlot(name='call_function')
    def slot(self, results):
        sender1.data.emit(results)


class Sender1(QObject):
    data = pyqtSignal(list)


sender1 = Sender1()