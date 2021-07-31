from flask import render_template, redirect, request, current_app, Blueprint, url_for, flash, session
from utils import *
from models import User
from detector import *
from xssscanner import *

main = Blueprint('main', __name__)


@main.route("/", methods=["GET"])
@no_login_required
def home():

    return render_template("index.html")


# endpoint for login system
@main.route("/login")
@no_login_required
def login():

    return render_template("login.html")


# endpoint for register system
@main.route("/register")
@no_login_required
def register():

    return render_template("register.html")


# endpoint for post login
@main.route('/login', methods=["POST"])
@no_login_required
def signin():

    form = request.form

    User().signin(form)

    return redirect(url_for('main.dashboard'))


# endpoint for post registeration
@main.route('/register', methods=["POST"])
@no_login_required
def signup():

    form = request.form
    fname = form['fname']
    lname = form['lname']
    email = form['email']
    password = form['password']

    User.signup(fname, lname, email, password)

    return redirect(url_for('main.login'))


# endpoint for user dashboard
@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard(user):

    user = User.get(user['_id'])

    return render_template('dashboard.html', user=user)


# endpoint for user logout
@main.route('/logout')
@login_required
def logout(user):
    User.signout()
    return redirect(url_for('main.home'))


@main.route('/report', methods=['GET'])
def report():

    url = request.args.get('url')

    inject = scan_sql_injection(url)
    xss_scanner(url)

    if inject:
        flash(inject, 'danger')
        return redirect(url_for('main.dashboard'))

    clear_list = [xss_detected, scan_logs, risk_level, payloads_tried]
    clear_list2 = [db, sqli_detected, risk_state, logs]

    def clear(list):
        for x in list:
            x.clear()

    def clear2(list):
        for x in list:
            x.clear()

    return render_template("report.html", test_logs=logs, db=db, sqli_detected=sqli_detected, risk_state=risk_state, sqli_type=sqli_type, scan_logs=scan_logs, xss_type=xss_type, risk_level=risk_level, xss_detected=xss_detected, payloads_tried=payloads_tried), clear(clear_list), clear2(clear_list2)


# scan report endpoint for logged in user
@main.route('/u_report', methods=['GET'])
@login_required
def u_report(user):

    url = request.args.get('url')

    inject = scan_sql_injection(url)
    xss_scanner(url)

    if inject:
        flash(inject, 'danger')
        return redirect(url_for('main.dashboard'))

    # compiling the scan data
    data = {
        'url': url,
        'sql': {
            "databaseType": db,
            "riskLevel": risk_state,
            "isVul": sqli_detected,
            "slqiType": sqli_type,
            "scanLogs": logs
        },
        'xss': {
            "xssType": xss_type,
            "isVul": xss_detected,
            "payloadsTried": payloads_tried,
            "riskLevel": risk_level,
            "scanLogs": scan_logs
        }
    }
    # saving the scan data
    user = user['_id']
    save = User.save(user, data)

    clear_list = [xss_detected, scan_logs, risk_level, payloads_tried]
    clear_list2 = [db, sqli_detected, risk_state, logs]

    def clear(list):
        for x in list:
            x.clear()

    def clear2(list):
        for x in list:
            x.clear()

    return render_template("u_report.html", test_logs=logs, db=db, sqli_detected=sqli_detected, risk_state=risk_state, sqli_type=sqli_type, scan_logs=scan_logs, xss_type=xss_type, risk_level=risk_level, xss_detected=xss_detected, payloads_tried=payloads_tried), clear(clear_list), clear2(clear_list2)

# previous scans


@main.route('/previous')
@login_required
def previous(user):
    scans = User.query(user['_id'])
    return render_template('previous.html', scans=scans)


# previous scan details
@main.route('/previous/<string:id>')
@login_required
def details(user, id):
    details = User.fetch(id, user['_id'])
    return render_template('details.html', details=details)
