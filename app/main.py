#!/usr/bin/env python3

from flask import Flask, render_template
import locale

from tools.tools import tools_bp
from bin.bin import bin_bp
from geo.geo import geo_bp

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

app = Flask(__name__)  # Create main application object
app.register_blueprint(tools_bp, url_prefix='/tools')
app.register_blueprint(bin_bp, url_prefix='/bin')
app.register_blueprint(geo_bp, url_prefix='/geo')


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
