from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/curiosidades")
def curiosidades():
    return render_template("curiosidades.html")

@app.route("/infoflask")
def infoflask():
    return render_template("infoflask.html")

if __name__ == "__main__":
    app.run(debug=True, port=3500)
