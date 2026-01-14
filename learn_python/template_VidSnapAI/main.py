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
        for file_name in request.files.keys():
             print(file_name)
             file = request.files[file_name]
             if file:
                upload_filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name)))):
                    os.mkdir(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name))
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name, upload_filename))

             with open(os.path.join(app.config["UPLOAD_FOLDER"], upload_folder_name, "descr.txt"), "w") as desc_file:
                desc_file.write(reel_description)

    return render_template("create.html", upload_folder_name=upload_folder_name)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)