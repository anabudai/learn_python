def slow_func():
    print("1")
    print("2")
    print("...")
    return 7

if( (result := slow_func()) > 3):
    print(result)
else:
    print("Not bigger than 3")