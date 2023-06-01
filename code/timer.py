from time import time

class Timer:

    def __init__(self, duration):

        self.duration = duration
        self.t0 = time()

    def trigger(self):

        if self.t0 + self.duration <= time():
            self.t0 = time()
            return True

        else:
            return False
