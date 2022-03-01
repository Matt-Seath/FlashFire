from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email, Length


"""Forms users will interact with the obtain user input"""


class registerForm(FlaskForm):
    username = StringField("username:", validators=[DataRequired("Username field is empty"),
                Length(min=3, max=30, message="Username must be between 3 and 30 characters long")])
    password = PasswordField("password:", validators=[DataRequired("Password field is empty"),
                Length(min=8, max=30, message="Password must be between 8 and 30 characters long")])
    confirmPassword = PasswordField("confirm password:", validators=[InputRequired("Confirm password field is empty"),
                        EqualTo('password', message='Passwords must match')])
    email = EmailField("email:", validators= [InputRequired("Email field is empty"), Email(message="Invalid email"),
                        Length(max=40, message="Email must be less than 40 characters long")])
    submit = SubmitField("register")


class changePasswordForm(FlaskForm):
    oldPassword = PasswordField("old password:", validators=[DataRequired("Old password field is empty")])
    newPassword = PasswordField("new password:", validators=[DataRequired("New password field is empty"),
                Length(min=8, max=30, message="New password must be between 8 and 30 characters long")])
    confirmPassword = PasswordField("confirm new:", validators=[InputRequired("Confirm password field is empty"),
                        EqualTo('newPassword', message='Passwords must match')])
    submit = SubmitField("change")


class loginForm(FlaskForm):
    username = StringField("username:", validators=[DataRequired("Username field is empty")])
    password = PasswordField("password:", validators=[DataRequired("Password field is empty")])
    submit = SubmitField("login")


class searchBar(FlaskForm):
    userInput = StringField("Search: ", validators=[DataRequired()])

