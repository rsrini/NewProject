from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return " Helo this is the main page <h1> Hi Srini <h1>"

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

@app.route("/<name>")
def user(name):
    return render_template("index.html", content=name, r="Srini")


# @app.route("/admin")
# def admin():
# #    return redirect(url_for("home"))
#     return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run()

