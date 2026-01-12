from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    print(f"request.method={request.method}")
    print(f"request.form={request.form}")
    return render_template("index_4_form.html")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
