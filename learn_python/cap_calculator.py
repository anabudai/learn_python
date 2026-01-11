try:
    first = int(input("First number=\n"))
    second = int(input("Second number=\n"))

    print("Please provide operation to apply on the numbers.\nType:\n + for addition\n - for substraction\n * for multiplication\n \ for division \n")

    operation = input("Operation=\n")

    result = None
    match operation:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "*":
            result = first * second
        case "/":
            result = first / second
        case _:
            print("Please provide a valid operator!")

    if result != None:
        print(f"Result={result}")
    
except ValueError as e:
    print(f"Please provide valid numbers. Error={e}")
except Exception as e:
    print(f"Error during calculator processing. Error={e}")