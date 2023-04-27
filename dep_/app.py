from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route("/")
def halamanCV():
    return render_template("index.html")


if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()