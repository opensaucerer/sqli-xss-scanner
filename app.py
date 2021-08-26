from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'THIS IS THE HOME PAGE'


if __name__ == '__main__':
    app.run(debug=True, port=443)
