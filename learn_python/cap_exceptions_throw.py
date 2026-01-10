age_as_string = input("Please insert age=\n")

try:
    age = int(age_as_string)

    if age <= 0:
        raise ValueError("Age must be a value bigger than 0")
    
    print(f"Age= {age}")
except ValueError as e:
    print(f"Error during processing. Error = {e}")
else:
    print(f"No error. Age=\"{age_as_string}\" is correct")
finally:
    print("Thank you for choosing us")


