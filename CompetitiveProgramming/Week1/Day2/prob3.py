class TempTracker(object):
    def __init__(self):
        self.present = [0] * 111
        self.max_present = 0
        self.mode = None
        self.n = 0
        self.sum = 0.0
        self.mean = None
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, t):
        self.present[t] += 1
        if self.present[t] > self.max_present:
            self.mode = t
            self.max_present = self.present[t]

        self.n += 1
        self.sum += t
        self.mean = self.sum / self.n

        if t > self.max_temp:
            self.max_temp = t
        if t < self.min_temp:
            self.min_temp = t

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode