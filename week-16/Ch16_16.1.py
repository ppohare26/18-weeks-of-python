class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

t = Time(9, 5, 3)
print_time(t)
