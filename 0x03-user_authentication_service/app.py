#!/usr/bin/env python3
"""
Flask application
"""
from auth import Auth
from flask import Flask, jsonify, request, abort


app = Flask(__name__)
auth = Auth()


@app.route('/')
def root():
    """
    Root path
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], s)
def users():
    """
    Endpoint for users
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions
      Return:
        - message
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if auth.valid_login(email, password):
        session_id = auth.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
