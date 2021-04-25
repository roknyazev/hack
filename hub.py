import copy
import uav
import move

uav_list = []
hub_list = []


class Hub:
    def __init__(self, coordinates, identifier, hub_type):
        self.coordinates = coordinates
        self.type = hub_type
        self.storage = None
        if hub_type == 0:
            self.identifier = "Hub" + ":Small:" + str(identifier)
            self.min_load = 1
        elif hub_type == 1:
            self.identifier = "Hub" + ":Middle:" + str(identifier)
            self.min_load = 5
        elif hub_type == 2:
            self.identifier = "Hub" + ":Large:" + str(identifier)
            self.min_load = 10

    def append_storage(self, package):
        if package.get_next_hub() is None:
            return
        if self.storage is None:
            self.storage = [[package.get_next_hub(), [package]]]
            return
        for direction in self.storage:
            if direction[0] == package.get_next_hub():
                direction[1].append(package)
                return
        self.storage.append([package.get_next_hub(), [package]])

    def start_uav(self):
        if self.storage is None:
            return
        for direction in self.storage:
            print(direction[0])
            if (self.type == 0 and len(direction[1]) > 1) or \
                    (self.type == 1 and len(direction[1]) > 1 and direction[0][4] == "S"):

                direction[1].pop()
                uav_elem = uav.SmallUAV(len(uav_list) + 1)
                uav_list.append(uav_elem)

                hub_elem = None
                for hub in hub_list:
                    if direction[0] == hub.identifier:
                        hub_elem = hub

                uav_elem.set_move_method(move.Move(self.coordinates, hub_elem.coordinates))
                load = copy.copy(direction[1][-1])
                uav_elem.set_load([load])
                uav_elem.start()
            if (self.type == 1 and len(direction[1]) > 30 and direction[0][4] != "S") or \
                    (self.type == 2 and len(direction[1]) > 30 and direction[0][4] == "M"):


                uav_elem = uav.MiddleUAV(len(uav_list) + 1)
                uav_list.append(uav_elem)
                hub_elem = None
                for hub in hub_list:
                    if direction[0] == hub.identifier:
                        hub_elem = hub
                uav_elem.set_move_method(move.Move(self.coordinates, hub_elem.coordinates))
                load = copy.copy(direction[1][-1:1:-uav_elem.load_capacity])
                for i in range(uav_elem.load_capacity):
                    direction[1].pop()
                uav_elem.set_load(load)
                uav_elem.start()
            if self.type == 2 and len(direction[1]) > 300 and direction[0][4] == "L":

                uav_elem = uav.LargeUAV(len(uav_list) + 1)
                uav_list.append(uav_elem)
                hub_elem = None
                for hub in hub_list:
                    if direction[0] == hub.identifier:
                        hub_elem = hub
                uav_elem.set_move_method(move.Move(self.coordinates, hub_elem.coordinates))
                load = copy.copy(direction[1][-1:1:-uav_elem.load_capacity])
                for i in range(uav_elem.load_capacity):
                    direction[1].pop()
                uav_elem.set_load(load)
                uav_elem.start()
