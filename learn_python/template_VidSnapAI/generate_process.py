import os

def text_to_audio(folder_name):
    print(f"TA-{folder_name}")

def create_reel(folder_name):
    print(f"CR-{folder_name}")

if __name__ == "__main__":
    done_folders = []
    if os.path.exists("done.txt"):
        with open("done.txt", "r") as done_folders_list:
            done_folders = [file.strip() for file in done_folders_list.readlines()]

    all_reel_folders = os.listdir("user_uploads")
    for reel_folder in all_reel_folders:
        if not(reel_folder in done_folders):
            text_to_audio(reel_folder)
            create_reel(reel_folder)
            with open("done.txt", "a") as done_folders_list:
                done_folders_list.write(f"{reel_folder}\n")