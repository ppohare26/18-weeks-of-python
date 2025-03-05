#1 Write a function that draws a grid like the following:
print("#1")
def print_row():
    print('+ - - - - + - - - - +')

def print_column():
    print('|         |         |')

def draw_grid_2x2():
    print_row()
    for _ in range(4):
        print_column()
    print_row()
    for _ in range(4):
        print_column()
    print_row()

draw_grid_2x2()


#2 Write a function that draws a similar grid with four rows and four columns.

print("#2")
def print_row():
    print('+ - - - - + - - - - + - - - - + - - - - +')

def print_column():
    print('|         |         |         |         |')

def draw_grid_4x4():
    for _ in range(4):
        print_row()
        for _ in range(4):
            print_column()
    print_row()

draw_grid_4x4()