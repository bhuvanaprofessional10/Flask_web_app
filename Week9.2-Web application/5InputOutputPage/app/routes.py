from flask import Blueprint, render_template,request

main = Blueprint("main", __name__)

@main.route("/")
def home():

    return render_template("register.html")

@main.route("/result",methods =["POST"])
def result():
    message = ''

    if request.method == "POST":
        stdname= request.form.get("studentName")
        stdage= int(request.form.get("studentAge"))
        stdcoursefee= float(request.form.get("studentCourseFee"))

        gst_percentage = 0.18
        gst_amount = stdcoursefee * gst_percentage

        total_fee = stdcoursefee + gst_amount

    return render_template("result.html", 
                           studentName=stdname, 
                           studentAge=stdage, 
                           studentCourseFee=stdcoursefee, 
                           gstAmount=round(gst_amount, 2), 
                           totalFee=round(total_fee, 2))