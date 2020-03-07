from flask import Flask, flash, url_for,request,make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap
import unittest

from app import create_app
from app.forms import LoginForm
from app.firestone_service import get_users, get_todos

app = create_app()

@app.cli.command()
def test():
	tests = unittest.TestLoader().discover('test')
	unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
	return render_template('505.html', error=error)

@app.route("/")
def index():
	user_ip = request.remote_addr
	response = make_response(redirect("/hello"))
	session['user_ip'] = user_ip
	return response

@app.route("/hello", methods=['GET'])
def hello():
	user_ip = session.get("user_ip")
	username = session.get('username')
	context = {
		"user_ip": user_ip,
		"todos": get_todos(user_id=username),
		'username': username
	}
	
	users = get_users()
	for user in users:
		print(user.id)
		print(user.to_dict()['password'])

	return render_template("hello.html", **context)

