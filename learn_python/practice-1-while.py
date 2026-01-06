number = int(input("Enter a number: "))

temp = number
result_as_string = ""
while temp != 0:
    digit = temp % 10
    result_as_string = result_as_string + str(digit)
    temp = temp // 10

if result_as_string != "":
    result = int(result_as_string)
    print(f"Reversed number is: {result}")
