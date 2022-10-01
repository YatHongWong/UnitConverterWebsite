from re import L
from flask import Flask
from page1 import page1 

app = Flask(__name__)
app.register_blueprint(page1, url_prefix="/")

if __name__ == "__main__":
    app.run(debug = True)