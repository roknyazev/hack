
class Move:
    def __init__(self, start, destination):
        self.start = start
        self.destination = destination

        self.dt = 0.1
        self.trajectory = None
        self.current_position = None
        self.mean_v = 1
        self.start_time = 0

    def set_mean_v(self, mean_v):
        self.mean_v = mean_v

    def set_start(self, start_time):
        self.start_time=start_time

    def get_current_position(self, time):
        S = self.mean_v * (time - self.start_time)
        distance = ((self.destination[0] - self.start[0]) ** 2 + (self.destination[1] - self.start[1]) ** 2) ** 0.5
        X = [0, 0]
        if S < distance:
            X[0] = self.start[0] + (self.destination[0] - self.start[0]) / distance * S
            X[1] = self.start[1] + (self.destination[1] - self.start[1]) / distance * S
        else:
            X = None
        return X
