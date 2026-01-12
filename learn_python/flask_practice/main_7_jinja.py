from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index_7.jinja")

@app.route("/contact")
def contact():
    return render_template("contact.jinja")

@app.route("/about")
def about():
    return render_template("about.jinja")

if __name__ == "__main__":
    app.run(debug=True)
