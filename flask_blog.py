#   IMPORT Flask AND THE render_template FUNCTION
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
#   SECRET KEY PROTECTS APP FROM MODIFYING COOKIES AND SECURITY TYPE STUFF
app.config["SECRET_KEY"] = "b3d9315ea350f6023ab5b8582c044883"

posts = [
    {
        "author": "Luyanda Dingindlela",
        "title": "Blog title 1",
        "content": "This is some content",
        "date_posted": "April 20, 2021"
    },
    {
        "author": "Bruce wayne",
        "title": "Blog title 2",
        "content": "This is some content",
        "date_posted": "April 20, 2021"
    },
]

# ADD A ROUTE DECORATOR TO TELL FLASK WHICH URL TO TRIGGER
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug = True)