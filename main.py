from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("NEWuserdash.html")

@app.route("/signup")
def signup():
    return render_template("Sign_up.html")

if __name__ == "__main__":
    app.run(debug=True)
