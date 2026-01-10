def sum(*argsval):
    total = 0
    for i in argsval:
        total += i
    return total

print(sum(1, 2, 3))

print()

def ages(**args):
    for key, value in args.items():
        print(f"key={key}, value={value}")

ages(ana=40, dan=20, mary=4)