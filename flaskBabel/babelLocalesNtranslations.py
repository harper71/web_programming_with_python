from flask_babel import Babel, format_datetime, gettext
from flask import Flask, render_template, request
from datetime import datetime


class Config:
    LANGUAGES = ['en', 'es', 'de']
    BABEL_DEFAULT_LOCALE = 'de'
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index():
    
    anthony = gettext("Anthony")
    dt = datetime.now()
    
    auto_date = format_datetime(dt)
    locale = {
        'auto_date': auto_date
    }
    return render_template('usingLocale.html', locale=locale, anthony=anthony)



if __name__ == '__main__':
    app.run(debug=True)
