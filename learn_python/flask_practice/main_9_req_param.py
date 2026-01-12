from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args['name']
    age = request.args['age']
    return render_template("index_9.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
