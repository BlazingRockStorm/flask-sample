from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@application.route("/hi")
def hi_world():
    return "<p>Hi, World!</p>"
    
if __name__ == "__main__":
    application.run()