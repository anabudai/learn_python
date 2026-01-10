import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fileName")

args = parser.parse_args()

if args.fileName != None:
    try:
        file = open(args.fileName, "r")
        content = file.readlines()
        print(f"Number of lines = {len(content)}")
    except Exception as e:
        print(f"Exception = {e}")
