from datetime import datetime, timedelta

# Task 1
def current_day_of_week():
    today = datetime.today()
    print("Today is:", today.strftime('%A'))

# Task 2
def birthday_info(birth_str):
    birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    time_until = next_birthday - today

    print(f"Age: {age}")
    print(f"Time until next birthday: {time_until.days} days, {time_until.seconds // 3600} hours, {(time_until.seconds % 3600) // 60} minutes, {time_until.seconds % 60} seconds")

# Task 3
def double_day(birth1_str, birth2_str):
    b1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    b2 = datetime.strptime(birth2_str, "%Y-%m-%d")

    if b1 > b2:
        older, younger = b2, b1
    else:
        older, younger = b1, b2

    diff = younger - older
    double_day = younger + diff
    print("Double Day is:", double_day.strftime("%Y-%m-%d"))

# Task 4
def n_times_day(birth1_str, birth2_str, n):
    b1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    b2 = datetime.strptime(birth2_str, "%Y-%m-%d")

    if b1 > b2:
        older, younger = b2, b1
    else:
        older, younger = b1, b2

    diff = younger - older
    target = younger + diff / (n - 1)
    print(f"{n}-times Day is:", target.strftime("%Y-%m-%d"))


current_day_of_week()
print()

birthday_info("2000-06-15")
print()

double_day("2000-06-15", "2003-08-10")
print()

n_times_day("2000-06-15", "2003-08-10", 3)
