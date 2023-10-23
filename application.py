from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

@application.route("/blog")
def blog():
    return render_template('blog.html')

@application.route("/blog-details")
def blog_details():
    return render_template('blog-details.html')

if __name__ == "__main__":
    application.run()