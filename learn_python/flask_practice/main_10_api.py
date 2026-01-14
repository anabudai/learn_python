from flask import Flask, jsonify

app = Flask(__name__)

marks = {"ana":10, "maria":7, "dana":8}

@app.route("/")
def json():
    return jsonify(marks)

if __name__ == "__main__":
    app.run(debug=True)
