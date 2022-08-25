from flask import Flask, jsonify, request, render_template, redirect, make_response
import time
import locale
import datetime
import urllib.request, json
import random
import string
import os

locale.setlocale( locale.LC_ALL, 'pt_BR.UTF-8' )
app = Flask(__name__) # Create the server object

def get_random_password(var_lenght):
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(int(var_lenght)-4):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/time")
def get_time():
    return jsonify({"time": int(time.time())})

@app.route("/man")
def man():
    return render_template('man.html')

@app.route("/password")
@app.route("/password/<var_lenght>")
def password(var_lenght=12):
    return get_random_password(int(var_lenght))

@app.route("/check/<var_ip>")
@app.route("/check/<var_ip>/<var_port>")
@app.route("/check/<var_ip>/<var_port>/<var_protocol>")
def check(var_ip, var_port='null', var_protocol='tcp'):
    if var_ip == 'man':
        return render_template('man-check.html')

    if var_port == 'null':
        return 'ERROR: tux.tools/check/man\n'

    if var_protocol == 'udp':
        var_parameter='-vnzu'
    else:
        var_parameter='-vnz'

    ''' send to /dev/null 2>&1 to suppress terminal output '''
    res = os.system("/usr/bin/nc -w 1 "+var_parameter+" "+var_ip+" "+var_port+"  > /dev/null 2>&1")
    print(res)
    if res == 0:
        return "{}:{} - open\n".format(var_ip,var_port)
    else:
        return "{}:{} - closed\n".format(var_ip,var_port)

if __name__ == '__main__':
    #app.run(debug=True)
    app.debug = True
    app.run(host="0.0.0.0")
