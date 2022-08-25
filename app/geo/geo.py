from flask import Blueprint, render_template, jsonify
import json

geo_bp = Blueprint('geo_bp', __name__,
                    template_folder='templates/geo',
                    static_folder='static/geo')

@geo_bp.route("/")
def main():
    return jsonify({"answer":"Congratulations, you reached 22° 33' 39.1716'' S and 17° 3' 56.718'' E"})