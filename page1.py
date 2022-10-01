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
                    if units in ["euros","yuan","usd","hkd"]:
                        ans = str(round((amount*float(coefficient)), 2))
                        final_ans = tempamount +" "+ units +" is "+ans+ " pounds. "
                    elif units == "fahrenheit":
                        ans = str(round((amount-32)*(5/9), 2 ))
                        final_ans = tempamount+" fahrenheit(°F) is "+ans+" celsius(°C)" 
                    else:
                        smallans = str(int(round(amount*float(coefficient), sigfigs = 3)) )
                        bigans = str(round(amount*float(coefficient)/1000, sigfigs = 3) )
                        final_ans = tempamount +" "+ units + " is "+ smallans + " "+metric_units_1 + " or "+ bigans + " " + metric_units_2
        return render_template("index.html", answer = final_ans)
    elif request.method == "GET":   
        return render_template("index.html", answer="")
