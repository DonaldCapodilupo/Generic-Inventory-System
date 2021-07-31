from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login_Screen():
    return render_template("login.html")


if __name__ == '__main__':
    from backend import programSetup
    programSetup()
    app.run()
