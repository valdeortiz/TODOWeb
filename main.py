from flask import Flask, request,make_response, redirect, render_template

app = Flask(__name__)

todos = ['comprar cafe', 'comprar', 'enviar producto']

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
	return render_template('505.html', error=error)

@app.route("/")
def index():
	ip_user = request.remote_addr
	response = make_response(redirect("/hello"))
	response.set_cookie("ip_user", ip_user)
	return response

@app.route("/hello")
def hello():
	user_ip = request.cookies.get("ip_user")
	context = {
		"user_ip": user_ip,
		"todos": todos,
	}
	return render_template("hello.html", **context)
