def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

t1 = Time(12, 30, 15)
t2 = Time(11, 45, 50)

print(is_after(t1, t2))