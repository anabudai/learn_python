import os, time, subprocess
from text_to_speech import text_to_speech_file

def text_to_audio(folder_name):
    with  open(os.path.join("user_uploads", folder_name, "descr.txt"), "r") as file:
        text_to_speech_file(file.read(), f"user_uploads/{folder_name}")


def create_reel(folder_name):
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder_name}/input.txt -i user_uploads/{folder_name}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder_name}.mp4'''
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":

    while True:
        print("Processing queued...")
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
        time.sleep(4)