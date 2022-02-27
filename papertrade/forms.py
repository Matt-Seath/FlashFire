from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired

# Create a Form class

class registerForm(FlaskForm):
    username = StringField("username:", validators=[DataRequired()])
    password = PasswordField("password:", validators=[DataRequired()])
    submit = SubmitField("login")

class loginForm(FlaskForm):
        username = StringField("username:", validators=[DataRequired()])
        password = PasswordField("password:", validators=[DataRequired()])
        submit = SubmitField("login")
    

