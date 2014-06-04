import os
import site
site.addsitedir(os.path.dirname(__file__),'packages')

from flask import Flask
application = Flask(__name__)
application.DEBUG=True
application.run()
@app.route("/")
def hello():
    return "Hello yuc!"

