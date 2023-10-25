from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

@application.route("/blog/")
def blog():
    return render_template('blog.html')

@application.route("/blog-details/")
def blog_details():
    return render_template('blog-details.html')

@application.route("/services-details/")
def services_details():
    return render_template('services-details.html')

if __name__ == "__main__":
    application.run()