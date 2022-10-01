from flask import Blueprint, render_template, request
from sigfig import round


page1 = Blueprint(__name__, "page1")


@page1.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        tempamount = request.form["tempamount"]
        units = request.form["units"]
        amount = float(tempamount)
        with page1.open_resource("static/conversiontable.txt", "r") as f:
            for line in f:
                if units in line:
                    units, coefficient, metric_units_1, metric_units_2 = line.split(",")
                    smallans = str(int(round(amount*float(coefficient), sigfigs = 3)) )
                    bigans = str(round(amount*float(coefficient)/1000, sigfigs = 3) )
        return render_template("index.html", answer=tempamount +" "+ units + " is "+ smallans + " "+metric_units_1 + " or "+ bigans + " " + metric_units_2)
    elif request.method == "GET":   
        return render_template("index.html", answer="")
