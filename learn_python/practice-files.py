import os
import shutil

file_out = open("notes.txt", "w")
file_out.write("Learning Python is fun!")
file_out.close()
             
file_in = open("notes.txt", "r")
content = file_in.read()
print(content)

print("================================================")

file_out = open("notes.txt", "w")
file_out.write('''first line
               Learning Python is fun!
               third line ''')
file_out.close()

file_out = open("notes.txt", "a")
file_out.write("Task completed!")
file_out.close()

file_in = open("notes.txt", "r")
content = file_in.readlines()
print(len(content))
for line in content: print(line)

print("=======================================")
print(f"Current directory: {os.getcwd()}")
print(f"All files and folders:\n {os.listdir()}")
print()

if os.path.isdir("my_folder") is False:
    os.mkdir("my_folder")
os.removedirs("my_folder")
