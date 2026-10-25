from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html.j2")

@app.route("/info")
def info():
		return "Це інформаційний маршрут Flask.", 200, {
    "Content-Type": "text/plain; charset=utf-8"
    }

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html.j2", name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)