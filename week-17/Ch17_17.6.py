class Time:
    def __init__(self, hour=0, minute=0, second=0):
     
        self.seconds = hour * 3600 + minute * 60 + second

    def __str__(self):
        return int_to_time(self.seconds)

    def time_to_int(self):
        return self.seconds

    def __add__(self, other):
  
        return Time.from_seconds(self.seconds + other.seconds)

    @staticmethod
    def from_seconds(seconds):
    
        return Time(0, 0, seconds)

def int_to_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return f'{hour:02}:{minute:02}:{second:02}'

def time_to_int(time):
    return time.seconds

def increment(time, seconds):
    
    return Time.from_seconds(time.time_to_int() + seconds)

def main():
    start = Time(9, 45, 30) 
    print("Start time:", start)
    
    incremented_time = increment(start, 1500)  
    print("Incremented time:", incremented_time)
    
    time1 = Time(1, 30, 15)
    time2 = Time(2, 15, 0)
    
   
    print("Time1 in seconds:", time1.time_to_int())
    print("Time2 in seconds:", time2.time_to_int())

    added_time = time1 + time2
    print("Added time:", added_time)

if __name__ == "__main__":
    main()
