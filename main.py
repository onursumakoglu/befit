from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


# kullanıcı kayıt formu

class register_form(Form):
    name = StringField("İsim Soyisim", validators=[validators.Length(min = 4, max = 25), validators.DataRequired()])
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min = 5, max = 30), validators.DataRequired()])
    email = StringField("Email Adresi", validators=[validators.DataRequired(), validators.Email(message="Lütfen geçerli bir email adresi girin.")])
    password = PasswordField("Parola:", validators=[
        validators.DataRequired(message="Lütfen bir parola belirleyin."),
        validators.EqualTo(fieldname = "confirm", message="Parolanız uyuşmuyor.")
    ])

    confirm = PasswordField("Parola Doğrula")


app = Flask(__name__, static_url_path='/static')

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "befit"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register", methods = ["GET","POST"])
def register_page():

    form = register_form(request.form)

    if request.method == "POST":
        return redirect(url_for("main_page"))

    else:
        return render_template("register.html", form = form)

@app.route("/anasayfa")
def main_page():
    return render_template("main.html")

@app.route("/profil")
def profil_page():
    return render_template("profil.html")

@app.route("/program")
def program_page():
    return render_template("program.html")


if __name__ == "__main__":
    app.run()

