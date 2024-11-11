from flask import (
    Flask,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash
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
        flash("login Sucessful")
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            flash('you are already logged in')
            return redirect(url_for('user'))
        return render_template("form.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        if "user" in session:
            return redirect(url_for("login"))
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if 'user' in session:
        user = session["user"]
        flash(f"You have been logged out, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
