from flask import Blueprint, render_template,request

main = Blueprint("main", __name__)

@main.route("/",methods =["GET","POST"])
def home():
    message = ''

    if request.method == "POST":
        username= request.form.get("UserName")
        message = f"hello {username} , welcome to flask"

    return render_template("index.html", inputtext=message)