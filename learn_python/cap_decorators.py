def decorator_example(func):
    def wrapper_example():
        print("Before decorated")
        func()
        print("After decorated")
    return wrapper_example

@decorator_example
def say_hello():
    print("Hi")

# decorator_example(say_hello)()

say_hello()

print()

def repeat(n):
    def decorator_repeat(func):
        def wrapper_repeat():
            for i in range(1, n + 1):
                func()
            
        return wrapper_repeat
    return decorator_repeat

@repeat(4)
def sample_text():
    print("It is fine")

sample_text()


