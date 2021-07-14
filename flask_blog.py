#   IMPORT Flask AND THE render_template FUNCTION
from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug = True)