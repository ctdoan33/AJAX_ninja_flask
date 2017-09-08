from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)
@app.route("/")
def choose():
    return render_template("index.html")
@app.route("/request", methods=["POST"])
def ninja():
    color = request.form["color"].lower()
    if color == "red":
        src="../static/raphael.jpg"
        name="You chose Raphael!"
    elif color == "blue":
        src="../static/leonardo.jpg"
        name="You chose Leonardo!"
    elif color == "orange":
        src="../static/michelangelo.jpg"
        name="You chose Michelangelo!"
    elif color == "purple":
        src="../static/donatello.jpg"
        name="You chose Donatello!"
    else:
        src="../static/notapril.jpg"
        name="There's no ninja in that color!"
    return jsonify(name=name,source=src)
app.run(debug=True)