#1 Type this example into a script and test it.
print("#1")
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

#2 Modify do_twice so that it takes two arguments, a function object and a value, and calls the
#function twice, passing the value as an argument.
print("#2")
def do_twice(f, value):
    f(value)
    f(value)

def print_spam(s):
    print(s)

do_twice(print_spam, 'spam')


#3 Write a more general version of print_spam, called print_twice, that takes a string as a
#parameter and prints it twice.
print("#3")
def print_twice(s):
    print(s)
    print(s)


#4 Use the modified version of do_twice to call print_twice twice, passing'spam' as an argument.
print("#4")
do_twice(print_twice, 'spam')



#5 Define a new function called do_four that takes a function object and a value and calls the
#function four times, passing the value as a parameter. There should be only two statements in
#the body of this function, not four.
print("#5")
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'spam')
