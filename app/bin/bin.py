from flask import Blueprint, jsonify


bin_bp = Blueprint('bin_bp', __name__,
                   template_folder='templates/bin',
                   static_folder='static/bin')


@bin_bp.route("/laden")
def main():
    return jsonify({"answer": "One of the worst human being that has ever existed."})
