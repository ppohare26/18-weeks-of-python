import math 

def eval_loop():
    last_result = None
    while True:
        user_input = input("Enter an expression (or 'done' to quit): ")
        if user_input.lower() == 'done':
            break
        last_result = eval(user_input)
        print(last_result)
    return last_result


eval_loop()