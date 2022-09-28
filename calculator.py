"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_input = input("Enter your equation. ") # + 1 2
    tokens = user_input.split(' ')              #['+', '1', '2']

    if tokens[0] == 'q' or tokens[0] == 'quit': #exit conditions
        print("Exiting calculator.")
        break

    elif tokens[0] == '+':
        try:
            print(add(float(tokens[1]), float(tokens[2])))
        except:
            print("invalid operation")

    elif tokens[0] == '-':
        try:
            print(subtract(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")

    elif tokens[0] == '*':
        try:
            print(multiply(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")
    
    elif tokens[0] == '/':
        try:
            print(divide(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")

    elif tokens[0] == 'square':
        try:
            print(square(float(tokens[1])))
        except:
            print("invalid operation")

    elif tokens[0] == 'cube':
        try:
            print(cube(float(tokens[1])))
        except:
            print("invalid operation")

    elif tokens[0] == 'power':
        try:
            print(power(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")
    
    elif tokens[0] == 'mod':
        try:
            print(mod(float(tokens[1]),float (tokens[2])))
        except:
            print("invalid operation")
            
    else: print("invalid operation")
