from flask import Flask, render_template, request, url_for, redirect, jsonify
import requests
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from detector import *
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "hb7489fjbfygb"


class Website(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])


@app.route("/", methods=["GET", "POST"])
def home():

    form = Website()

    if form.validate_on_submit():

        url = form.url.data

        scan_sql_injection(url)
        return redirect('/report')

    return render_template("index.html", form=form)


@app.route('/report', methods=['GET', 'POST'])
def report():

    return render_template("report.html", test_logs=logs)


if __name__ == "__main__":
    app.run(debug=True)
