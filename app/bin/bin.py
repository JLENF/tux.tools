from flask import Blueprint, render_template, jsonify

bin_bp = Blueprint('bin_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@bin_bp.route("/laden")
def main():
    return jsonify({"answer": "One of the worst human being that has ever existed."})