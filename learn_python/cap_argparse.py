import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operator", choices=["add", "minus", "div", "mul"], help="Operation to perform")

args = parser.parse_args()

print(args)

result = None
if args.operator == "add":
    result = args.num1 + args.num2
elif args.operatpr == "minus":
    result = args.num1 - args.num2
elif args.operator == "mul":
    result = args.num1 * args.num2
elif args.operator == "div":
    result = args.num1 / args.num2

print(f"Result = {result}")