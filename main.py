print("Ramanujan")
print()

import random

operations = ["+","-","×","/"]

i = 1
correct = 0

while True:
    
    operation = operations[random.randint(0, 3)]
    a,b = random.randint(-100, 100), random.randint(-100, 100)
    if a == 0: a = a+1
    if b == 0: b = b+1
    
    result = 0
    match operation:
        case "+":
            if b < 0: b = b * -1
            result = a + b
            
        case "-":
            if b < 0: b = b * -1
            result = a - b
            
        case "×":
            result = a * b
            
        case "/":
            while True:
                if a % b == 0: break
                b = b-1
            result = int(a / b)
            
    player_input = input(f"{a} {operation} {b} = ")
    try:
        if int(player_input) == result:
            correct = correct+1
            print(f"Correct! ({correct}/{i})")
        else:
            print(f"Incorrect, its {result}.")
    except:
        print(f"That's not a number. Please enter an integer.")
    print()
    
    i = i+1
