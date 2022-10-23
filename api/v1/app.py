#!/usr/bin/python3
"""Flask app module"""
from flask import Flask, request
from models import storage
from api.v1.views import app_views
from flask import make_response, jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    """Release Resources"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Not found"""
    if (request.path.startswith('/api/v1/states/') and
       request.method == 'POST'):
        return ('Not a JSON')
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    HOSTS = getenv('HBNB_API_HOST', '0.0.0.0')
    PORTS = getenv('HBNB_API_PORT', '5000')
    app.run(host=HOSTS, port=int(PORTS), threaded=True)
