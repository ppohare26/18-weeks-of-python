class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def increment(time, seconds):
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second + seconds

    new_hour = total_seconds // 3600
    remaining = total_seconds % 3600
    new_minute = remaining // 60
    new_second = remaining % 60

    return Time(new_hour, new_minute, new_second)

t1 = Time(2, 45, 10)
t2 = increment(t1, 125)

print('%.2d:%.2d:%.2d' % (t2.hour, t2.minute, t2.second))
