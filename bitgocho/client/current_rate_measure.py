from bitgocho.clock import clock


class Measure:
    def __init__(self, max_rate_period, fudge=1):
        self.max_rate_period = max_rate_period
        self.ratesince = clock() - fudge
        self.last = self.ratesince
        self.rate = 0.0
        self.total = 0

    def update_rate(self, amount):
        self.total += amount
        t = clock()
        self.rate = (self.rate * (self.last - self.ratesince) + amount) / (
            t - self.ratesince + 0.0001
        )
        self.last = t
        if self.ratesince < t - self.max_rate_period:
            self.ratesince = t - self.max_rate_period

    def get_rate(self):
        self.update_rate(0)
        return self.rate

    def get_total(self):
        return self.total
