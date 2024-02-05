from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "dev"
app.permanent_session_lifetime = timedelta(days=7)


# route for home
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["usrname"]
        session.permanent = True
        session["user"] = user
        flash("Logged in successfully", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in.", "info")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Logged out successfully, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", username=user)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
