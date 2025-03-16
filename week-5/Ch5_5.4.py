def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        print("No")
    else:
        print("Yes")

def prompt_triangle():
    a = int(input("Enter length of first stick: "))
    b = int(input("Enter length of second stick: "))
    c = int(input("Enter length of third stick: "))
    is_triangle(a, b, c)

prompt_triangle()