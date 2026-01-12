from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    marks = {"ana": 10, "dan": 8, "john":5, "ema": 10}
    return render_template("index_5_jinja.html", marks=marks)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
