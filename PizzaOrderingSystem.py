from flask import *

application = Flask(__name__)


@application.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    application.run(debug=True)
