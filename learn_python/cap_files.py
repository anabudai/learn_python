file = open("input_ana.txt", "rt")

content = file.read()
file.close()

print(content)

file_out = open("output_ana.txt", "w")
file_out.write('''
Ana likes Python
but she will also like to learn Go next week
What do you say?
''')

file_out.close()

file_out = open("output_ana.txt", "a")
file_out.write('''
Text appended
''')

file_out.close()

file_read_line_by_line = open("output_ana.txt", "r")


for line in file_read_line_by_line:
    print(line)

file_read_line_by_line.close()

with open("output_ana.txt", "a") as f:
    f.write("text text text")


