from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world <h1>HELLO EVERYBODY</h>"

@app.route("/<name>")
def user(name):
    return f"<h2> Hello {name.replace('-', ' ')}!</h2>"

@app.route("/admin")
def admin():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)