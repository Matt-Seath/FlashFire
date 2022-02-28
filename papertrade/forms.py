from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email, Length


"""Forms users will interact with the obtain user input"""


class registerForm(FlaskForm):
    username = StringField("username:", validators=[DataRequired("Username field is empty"),
                Length(min=3, message="Username must be at least 3 characters long")])
    password = PasswordField("password:", validators=[DataRequired("Password field is empty"),
                Length(min=8, message="Password must be at least 8 characters long")])
    confirmPassword = PasswordField("confirm password:", validators=[InputRequired("Confirm password field is empty"),
                        EqualTo('password', message='Passwords must match')])
    email = EmailField("email:") 
    submit = SubmitField("register")

class loginForm(FlaskForm):
    username = StringField("username:", validators=[DataRequired("Username field is empty")])
    password = PasswordField("password:", validators=[DataRequired("Password field is empty")])
    submit = SubmitField("login")
    
class changePasswordForm(FlaskForm):
    oldPassword = PasswordField("old password:", validators=[DataRequired()])
    newPassword = PasswordField('New Password', validators=[InputRequired(),
                    EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Confirm Password')
    submit = SubmitField("change")

class searchBar(FlaskForm):
    userInput = StringField("Search: ", validators=[DataRequired()])

