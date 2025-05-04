class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def time_to_int(time):
    return time.hour * 3600 + time.minute * 60 + time.second

def int_to_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)

def increment(time, seconds):
    total_seconds = time_to_int(time) + seconds
    return int_to_time(total_seconds)

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

t1 = Time(1, 59, 30)
t2 = increment(t1, 90)
print_time(t2)  # Output: 02:01:00
