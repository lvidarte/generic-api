"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import os
from flask import Flask, request, jsonify
import flask_shelve as shelve

import lookup


app = Flask(__name__)
app.config['SHELVE_WRITEBACK'] = True
app.config['SHELVE_FILENAME'] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'db'
)
shelve.init_app(app)


@app.route("/", defaults={'path': ''})
@app.route("/<path:path>", methods=['GET', 'POST', 'DELETE'])
def endpoint(path):
    db = shelve.get_shelve('c')

    if request.method == 'GET':
        data, err = lookup.get(path, db)
        status_code = 200 if err is None else 404

    elif request.method == 'POST':
        value = request.get_json(force=True)
        data, err = lookup.post(path, db, value)
        status_code = 201 if err is None else 400

    elif request.method == 'DELETE':
        data, err = lookup.delete(path, db)
        status_code = 200 if err is None else 404

    else:
        err = {'error': 'method not allowed'}
        status_code = 405

    # Return
    if err:
        result = {'error': err}
    else:
        result = data

    return jsonify(result), status_code


# Error handlers

@app.errorhandler(404)
def error_404(err):
    return jsonify({'error': 'not found'}), 404

@app.errorhandler(400)
def error_400(err):
    return jsonify({'error': 'bad request'}), 400

@app.errorhandler(405)
def error_400(err):
    return jsonify({'error': 'method not allowed'}), 405

@app.errorhandler(500)
def error_400(err):
    return jsonify({'error': 'server error'}), 500


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)

