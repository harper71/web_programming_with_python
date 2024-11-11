from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return 'en'

if __name__ == "__main__":
    app.run()