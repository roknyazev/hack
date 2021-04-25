import time
import hub


class AbstractUAV:
    def __init__(self, identifier):
        self.mean_v = None
        self.load_capacity = None
        self.max_trajectory_length = None
        self.uav_weight = None
        self.identifier = identifier
        self.load = None
        self.move = None
        self.is_arrived = False
        self.uav_type = None

    def get_cost(self, fuel_price, trajectory_length, load):
        if trajectory_length > self.max_trajectory_length:
            print("Trajectory is too long")
            return
        if load > self.load_capacity:
            print("Not enough load capacity")
            return
        k = 1
        fuel_consumption = k * (load + self.uav_weight)
        return fuel_consumption * trajectory_length * fuel_price

    def set_move_method(self, move_method):
        if move_method is None:
            print("Move method is none")
            return
        move_method.set_mean_v(self.mean_v)
        self.move = move_method

    def set_load(self, load):
        self.load = load

    def start(self):
        self.move.set_start(time.time())

    def get_current_position(self, cur_time):
        if self.move.get_current_position(cur_time) is None:

            hub_id = (self.load[0]).get_next_hub()
            for dst in hub.hub_list:
                if dst.identifier == hub_id:
                    for package in self.load:
                        dst.append_storage(package)
            self.is_arrived = True
        return self.move.get_current_position(cur_time)


class SmallUAV(AbstractUAV):
    def __init__(self, identifier):
        super().__init__(identifier)
        self.mean_v = 5
        self.load_capacity = 1
        self.max_trajectory_length = 150
        self.uav_weight = 35
        self.uav_type = 0


class MiddleUAV(AbstractUAV):
    def __init__(self, identifier):
        super().__init__(identifier)
        self.mean_v = 12
        self.load_capacity = 5
        self.max_trajectory_length = 250
        self.uav_weight = 160
        self.uav_type = 1


class LargeUAV(AbstractUAV):
    def __init__(self, identifier):
        super().__init__(identifier)
        self.mean_v = 25
        self.load_capacity = 10
        self.max_trajectory_length = 500
        self.uav_weight = 1500
        self.uav_type = 2
