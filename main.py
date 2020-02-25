from flask import Flask, flash, url_for,request,make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'super SECRETO'

todos = ['comprar cafe', 'comprar', 'enviar producto']

class LoginFrom(FlaskForm):
	"""formulario de login"""
	username = StringField('nombre de usuario', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	submit = SubmitField('Enviar')

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

@app.route("/hello", methods=['GET', 'POST'])
def hello():
	user_ip = session.get("user_ip")
	login_form = LoginFrom()
	username = session.get('username')
	context = {
		"user_ip": user_ip,
		"todos": todos,
		"login_form": login_form
	}
	if login_form.validate_on_submit():
		username = login_form.username.data
		session['username'] = username

		flash('nombre de usuario registrado con exito')

		return redirect(url_for('index'))

	return render_template("hello.html", **context)
