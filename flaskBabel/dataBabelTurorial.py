from flask import Flask, render_template
from flask_babel import Babel, dates
from datetime import time, datetime


app = Flask(__name__)

@app.route('/')
def index():
    d = datetime.now()
    dt = datetime.today()
    us_date = dates.format_date(d, locale='en_US')
    de_date = dates.format_date(d, locale="de_DE")
    de_dateTime = dates.format_datetime(dt, locale='de_DE')
    en_dateTime = dates.format_datetime(dt, locale='en_US')

    results = {
        'us_date': us_date,
        'de_date': de_date,
        'de_datetime': de_dateTime,
        'en_datetime': en_dateTime
    }
    return render_template('dates.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
