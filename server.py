from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)
@app.route("/")
def choose():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def ninja():
    color = request.form["color"]
    if color == "red":
        src="../static/raphael.jpg"
    elif color == "blue":
        src="../static/leonardo.jpg"
    elif color == "orange":
        src="../static/michelangelo.jpg"
    elif color == "purple":
        src="../static/donatello.jpg"
    return src
app.run(debug=True)