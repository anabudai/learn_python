import os

def arrange_files(files, file_extension):
    files_with_extension = [file for file in files if file.endswith(file_extension)]

    if not(os.path.exists("images")):
        os.mkdir("images")

    for i, file in enumerate(files_with_extension):
        os.rename(file, f"images/photo-{i + 1}.jpg")

folder_files = os.listdir()
file_extension = ".jpg"

arrange_files(folder_files, file_extension)
