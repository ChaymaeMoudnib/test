from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health_check():
    return "OK", 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
