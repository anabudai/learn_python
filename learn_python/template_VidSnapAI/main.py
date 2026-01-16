from flask import Flask, render_template, request
import uuid, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "user_uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    upload_folder_name = uuid.uuid1()
    if request.method == "POST":
        print(f"file={request.files.keys()}")
        upload_folder_name = request.form.get("upload_folder_name")
        reel_description = request.form.get("textReel")
        input_files = []
        for file_name in request.files.keys():
             print(file_name)
             file = request.files[file_name]
             if file:
                upload_filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name)))):
                    os.mkdir(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name))
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name, upload_filename))
                input_files.append(file.filename)

             with open(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name, "descr.txt"), "w") as desc_file:
                desc_file.write(reel_description)

        with open(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name, "input.txt"), "a") as reel_spec_file:
            for input_file in input_files:
                reel_spec_file.write(f"file {input_file}\nduration 10\n")

    return render_template("create.html", upload_folder_name=upload_folder_name)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(f"============================={reels}")
    return render_template("gallery.html", reels=reels)

app.run(debug=True)