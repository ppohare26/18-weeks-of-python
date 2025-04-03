#2
from __future__ import print_function, division
import random

def contains_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def generate_random_birthdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def simulate_birthday_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = generate_random_birthdays(num_students)
        if contains_duplicates(t):
            count += 1
    return count

def main():
    num_students = 23
    num_simulations = 1000
    count = simulate_birthday_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)

if __name__ == '__main__':
    main()



#1
print("*******1********")
def has_duplicates(lst):
    return len(lst) != len(set(lst))


print(has_duplicates([1, 2, 3, 4, 5])) 
print(has_duplicates([1, 2, 3, 4, 5, 1])) 