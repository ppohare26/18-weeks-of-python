class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def cmp(self, other):
        return (self.time_to_int() > other.time_to_int()) - (self.time_to_int() < other.time_to_int())

t1 = Time(10, 30, 0)
t2 = Time(9, 45, 0)

print(t1.cmp(t2)) 
print(t2.cmp(t1)) 
print(t1.cmp(t1))
