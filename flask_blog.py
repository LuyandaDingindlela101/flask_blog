#   IMPORT Flask AND THE render_template FUNCTION
from flask import Flask, render_template

app = Flask(__name__)


# ADD A ROUTE DECORATOR TO TELL FLASK WHICH URL TO TRIGGER
@app.route("/")
@app.route("/home")
def home():
    return "This is home."


@app.route("/about")
def about():
    return "This is about."


if __name__ == "__main__":
    app.run(debug = True)