from flask import render_template

from testapp import app


@app.route("/")
def index():
    my_dict = {
        "data1": "Hello",
        "data2": "goodbye",
        "test_titles": ["Title1", "Title2", "Title3"],
    }
    return render_template("testapp/index.html", my_dict=my_dict)
