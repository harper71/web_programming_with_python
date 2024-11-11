from flask import (
    Flask,
    render_template,
    session,
    request,
    redirect, 
    url_for,
)
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session['user'] = user
        return redirect(url_for("user"))
    else:
        return render_template("form.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return redirect(url_for("form.html"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
