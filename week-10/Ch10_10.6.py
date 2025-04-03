def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 2])) 
print(is_sorted(['b', 'a']))