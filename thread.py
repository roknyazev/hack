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
        while True:
            result = []
            time.sleep(0.5)
            for hub_elem in hub.hub_list:
                hub_elem.start_uav()
            for uav_elem in hub.uav_list:
                result.append(uav_elem.get_current_position(time.time()))
            self.slot(result)

    @pyqtSlot(name='call_function')
    def slot(self, results):
        sender1.data.emit(results)


class Sender1(QObject):
    data = pyqtSignal(list)


sender1 = Sender1()