from flask import Flask, render_template, request
from codes import sum

app = Flask(__name__, template_folder='/home/jayshil/Documents/Codes/Python/flsk/Basic')
app.config["DEBUG"] = True

# Route tells the def home() will be activated when one goes to said path on web ("/" in the case below)
@app.route("/", methods=["GET", "POST"])
def home():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = sum(number1, number2)
            return render_template('home1.html').format(result=result)

    return render_template('home.html').format(errors=errors)


if __name__ == '__main__':
    app.run(debug=True)