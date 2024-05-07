from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return "contacto"

if __name__ == "__main__":
    app.run(debug=True, port=3500)
