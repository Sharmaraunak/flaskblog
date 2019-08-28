from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
	username = StringField("Username",
		validators = [DataRequired(),Length(min = 2,max = 10)])
	email = StringField("Email",
		validators = [DataRequired(),Email()])
	password = PasswordField("Password",validators = [DataRequired(),Length(min  = 8)])

	confirmPassword = PasswordField("Confirm Password",
		validators = [DataRequired(),EqualTo('password')])
	submit = SubmitField("Sign Up")


	def validate_username(self,username):
		user = User.query.filter_by(username = username.data).first()

		if user:
			raise ValidationError('That username is taken .Please choose a different one.')
	def validate_email(self,email):
		user = User.query.filter_by(email = email.data).first()

		if user:
			raise ValidationError('That email is taken .Please choose a different one.')


class LoginForm(FlaskForm):
	email = StringField("Email",
		validators = [DataRequired(),Email()])
	password = PasswordField("Password",validators = [DataRequired()])

	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
	username = StringField("Username",
		validators = [DataRequired(),Length(min = 2,max = 10)])
	email = StringField("Email",
		validators = [DataRequired(),Email()])

	picture = FileField('update profile picture',validators = [FileAllowed(['jpg','png'])])

	
	update = SubmitField("Update")


	def validate_username(self,username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()

			if user:
				raise ValidationError('That username is taken .Please choose a different one.')


	def validate_email(self,email):
		if email.data != current_user.email:
			user = User.query.filter_by(email = email.data).first()

			if user:
				raise ValidationError('That email is taken .Please choose a different one.')


class PostForm(FlaskForm):
	title = StringField('title',validators = [DataRequired()])
	content = TextAreaField('content',validators = [DataRequired()])
	submit = SubmitField('Post')

