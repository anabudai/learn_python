import os
import shutil

result = os.listdir()
print(result)

print()

current_dir = os.getcwd()
print(f"Current dir={current_dir}")

# os.remove("file_to_be_removed.txt")
# os.remove("dir")
# shutil.rmtree("dir")

shutil.copy("input_ana.txt", "input_ana_copy.txt")
shutil.move("input_ana_copy.txt", "new_dir")