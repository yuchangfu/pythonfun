import os
import site
site.addsitedir(os.path.dirname(__file__),'packages')

from flask import Flask
app = Flask(__name__)
app.DEBUG=True
@app.route("/")
def hello():
    return "Hello yuc!"

if __name__ == "__main__":
    app.run()
