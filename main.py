from flask import Flask, render_template

app = Flask(__name__)

## To connect HTML pages to the "app" instance website use this @app...
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    #f = pandas.read_csv("")
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}



app.run(debug=True)