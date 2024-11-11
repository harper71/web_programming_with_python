from  flask import Flask, render_template
from flask_babel import Babel, numbers

app = Flask(__name__)

@app.route('/')
def index():
    """
    Purpose: 
    """
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale='de_DE')
    
    results = {
        'us_num': us_num,
        'se_num': se_num,
        'de_num': de_num
    }
    return render_template('index.html', results=results)

# end def

if __name__ == "__main__":
    app.run()