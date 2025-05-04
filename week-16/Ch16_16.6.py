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

def mul_time(time, number):
    total_seconds = time_to_int(time) * number
    return int_to_time(int(total_seconds))

def average_pace(finishing_time, distance):
    return mul_time(finishing_time, 1/distance)

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

race_time = Time(1, 30, 0)  
distance = 10 
pace = average_pace(race_time, distance)
print_time(pace)  
