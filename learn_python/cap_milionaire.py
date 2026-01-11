questions = [
    ["What is the tallest mountain?", "Everest", "K9", "Omu", "Bucegi", 1],
    ["What is the largest country?", "China", "France", "Russia", "Brasil", 3]
]

for question in questions:
    print(f"Question={question[0]}")
    print(f"1 {question[1]}")
    print(f"2 {question[2]}")
    print(f"3 {question[3]}")
    print(f"4 {question[4]}")

    print("Please choose which answer you think is best by typing 1 or 2 or 3 or 4:\n")
    try:
        answer = int(input("Answer=\n"))

        if question[5] == answer:
            print("Great work!!!")
        else:
            print("Wrong answer. Game over!")
            break
    except ValueError as e:
        print("Please insert a valid answer number")




    