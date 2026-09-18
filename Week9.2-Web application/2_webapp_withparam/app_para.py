from flask import Flask,render_template 

app= Flask(__name__)

@app.route("/")
def hello_world():
    name = "Bhuvana"
    return render_template("index.html", guestname = name)


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)