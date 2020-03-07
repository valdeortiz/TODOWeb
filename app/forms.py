from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	"""formulario de login"""
	username = StringField('nombre de usuario', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
	description = StringField('descripcion', validators=[DataRequired] )
	submit = SubmitField('crear')