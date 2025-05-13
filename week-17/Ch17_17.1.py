class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second
    
t = Time(2, 30, 15)
print(t.time_to_int())
