from flask import Flask,render_template,url_for


app=Flask(__name__)


@app.route("/")
def sample():
    return  render_template("nav.html")

@app.route("/Home")
def sample1():
    return  render_template("home.html")


@app.route("/Data Analytics")
def sample2():
    flipped = False
    return  render_template("Data.html", flipped=flipped)



if __name__=="__main__":
    app.run()
