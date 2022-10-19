# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from fpdf import FPDF
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("index.html")


@app.route('/reg8')
# ‘/’ URL is bound with hello_world() function.
def reg8():

    return render_template("regforn-8.html")

@app.route('/regsucess', methods=["GET", "POST"])
def regsucess():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", "", 20)
    pdf.set_text_color(0, 0, 120)
    pdf.text(63, 20, str("Adarsh Lakshya Academy"))
    pdf.set_font("Arial", "", 12)
    pdf.text(78, 28, str("Fazilnagar Kushinagar (U.P)"))

    pdf.set_text_color(120, 0, 0)
    pdf.set_font("Arial", "UB", 12)
    pdf.text(20, 50, str("Student Registration Form"))
    if request.method == "POST":
        StdName = request.form["studentname"]
        mothername = request.form["mname"]
        fathername = request.form["fname"]
        modileno = request.form["mno"]
        altmobileno = request.form["Amno"]
        adharno = request.form["ano"]
        email = request.form["email"]
        clas = request.form["class"]
        dob = request.form["dob"]
        gender = request.form["gdr"]
        addresh = request.form["addr"]
        # img= request.files["files"]
        # img.save(secure_filename(img.filename))
        # img.stream
        # pdf.image(img, x=0, y=0)
        # data = request.form
        # print(StdName)

        pdf.set_text_color(0, 0, 0)

        # Student name l
        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 70, str("Student Name -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 70, str(StdName))

        # Student Class r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 70, str("Class -"))
        pdf.set_font("Arial", "", 9)
        pdf.text(140, 70, str(clas))

        # Father Name l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 80, str("Father Name - "))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 80, str(fathername))

        # Mother Name r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 80, str("Mother Name -"))
        pdf.set_font("Arial", "", 9)
        pdf.text(150, 80, str(mothername))

        # Gender l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 90, str("Gender - "))
        pdf.set_font("Arial", "", 9)
        pdf.text(50, 90, str(gender))

        # Section r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 90, str("D.O.B -"))
        pdf.set_font("Arial", "", 9)
        pdf.text(150, 90, str(dob))

        # Mobile No l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 100, str("Mobile No-"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 100, str(modileno))

        # Alt Mobile No r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 100, str("Alt. Mobile No - "))
        pdf.set_font("Arial", "", 9)
        pdf.text(150, 100, str(altmobileno))

        # Aadhar l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 110, str("Aadhar No -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 110, str(adharno))

        # Email r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 110, str("Email -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(150, 110, str(email))

        # Addresh l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 120, str("Address -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 120, str(addresh))

        pdf.output('regclass1to8.pdf')

        return render_template("success-x.html")
    # return render_template("regforn-8.html")

# @app.route("")

@app.route('/reg612')
# ‘/’ URL is bound with hello_world() function.
def reg612():
    return render_template("regn6-12.html")

@app.route('/regsucess1', methods=["GET", "POST"])
def regsucess1():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", "", 20)
    pdf.set_text_color(0, 0, 120)
    pdf.text(63, 20, str("Adarsh Lakshya Academy"))
    pdf.set_font("Arial", "", 12)
    pdf.text(78, 28, str("Fazilnagar Kushinagar (U.P)"))

    pdf.set_text_color(120, 0, 0)
    pdf.set_font("Arial", "UB", 12)
    pdf.text(20, 50, str("Student Registration Form Non-Schooling"))
    if request.method == "POST":
        StdName = request.form["studentname"]
        mothername = request.form["mname"]
        fathername = request.form["fname"]
        modileno = request.form["mno"]
        altmobileno = request.form["Amno"]
        adharno = request.form["ano"]
        email = request.form["email"]
        clas = request.form["class"]
        dob = request.form["dob"]
        gender = request.form["gdr"]
        addresh = request.form["addr"]
        # img= request.files["files"]
        # img.save(secure_filename(img.filename))
        # img.stream
        # pdf.image(img, x=0, y=0)
        # data = request.form
        # print(StdName)

        pdf.set_text_color(0, 0, 0)

        # Student name l
        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 70, str("Student Name -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 70, str(StdName))

        # Student Class r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 70, str("Class -"))
        pdf.set_font("Arial", "", 9)
        pdf.text(140, 70, str(clas))

        # Father Name l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 80, str("Father Name - "))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 80, str(fathername))

        # Mother Name r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 80, str("Mother Name -"))
        pdf.set_font("Arial", "", 9)
        pdf.text(150, 80, str(mothername))

        # Gender l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 90, str("Gender - "))
        pdf.set_font("Arial", "", 9)
        pdf.text(50, 90, str(gender))

        # Section r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 90, str("D.O.B -"))
        pdf.set_font("Arial", "", 9)
        pdf.text(150, 90, str(dob))

        # Mobile No l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 100, str("Mobile No-"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 100, str(modileno))

        # Alt Mobile No r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 100, str("Alt. Mobile No - "))
        pdf.set_font("Arial", "", 9)
        pdf.text(150, 100, str(altmobileno))

        # Aadhar l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 110, str("Aadhar No -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 110, str(adharno))

        # Email r

        pdf.set_font("Arial", "B", 10)
        pdf.text(120, 110, str("Email -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(150, 110, str(email))

        # Addresh l

        pdf.set_font("Arial", "B", 10)
        pdf.text(20, 120, str("Address -"))
        pdf.set_font("Arial", "", 10)
        pdf.text(50, 120, str(addresh))

        pdf.output('regclass6-12.pdf')

        return render_template("success-x.html")

@app.route('/regcoach')
# ‘/’ URL is bound with hello_world() function.
def regcoach():
    return render_template("blog.html")


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
