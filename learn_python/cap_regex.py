import re

text = "I am Ana and I don't like the name Ana that much but it is ok"

result = re.search("Ana", text)
if result:
    print(f"result={result}")
    print(f"start={result.start()}")
    print(f"end={result.end()}")

print("====")

result = re.findall("Ana", text, re.IGNORECASE)
if result:
    print(f"result={result}")
    print(f"result count={len(result)}")

print("====")

result = re.sub("Ana", "Maria", text)
print(f"New text={result}")
