from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


#   CREATE A FORM BY CREATING A CLASS FOR THE REGISTRATION FORM
class RegistrationForm(FlaskForm):
    #   username FIELD WITH VALIDATION (DataRequired MEANS NOT EMPTY) (Length, self explanatory)
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign up")


#   CREATE A FORM BY CREATING A CLASS FOR THE LOGIN FORM
class LoginForm(FlaskForm):
    #   username FIELD WITH VALIDATION (DataRequired MEANS NOT EMPTY) (Length, self explanatory)
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")

    submit = SubmitField("Sign in")