from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():

    return render_template("index.html")

@app.route("/about", methods=['GET'])
def about():

    return render_template("about.html")

@app.route("/portfolio", methods=['GET'])
def portfolio():

    return render_template("portfolio.html")

@app.route("/login", methods=['GET'])
def login():

    return render_template("login.html")

@app.route("/blog", methods=['GET'])
def blog():

    return render_template("blog.html")

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()
