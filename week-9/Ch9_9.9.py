def pad_number(i, n):
    return str(i).zfill(n)

def is_reversed(i, j):
    return pad_number(i, 2) == pad_number(j, 2)[::-1]

def count_palindromic_ages(diff, flag=False):
    daughter_age = 0
    count = 0
    while True:
        mother_age = daughter_age + diff
        if is_reversed(daughter_age, mother_age) or is_reversed(daughter_age, mother_age + 1):
            count += 1
            if flag:
                print(daughter_age, mother_age)
        if mother_age > 120:
            break
        daughter_age += 1
    return count

def find_age_differences():
    diff = 10
    while diff < 70:
        n = count_palindromic_ages(diff)
        if n > 0:
            print(diff, n)
        diff += 1

print('diff  #instances')
find_age_differences()

print()
print('daughter  mother')
count_palindromic_ages(18, True)