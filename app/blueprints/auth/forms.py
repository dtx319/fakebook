from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm): 
    email = StringField('Email', validators=[DataRequired(), Email()])
    username=StringField('Username', validators=[DataRequired()])
    first_name=StringField('First Name', validators=[DataRequired()])
    last_name=StringField('Last Name', validators=[DataRequired()])     
    password=PasswordField('Password', validators=[DataRequired()])
    password_confirm=PasswordField('Please confirm your Password', validators=[DataRequired()])
    submit_button = SubmitField('Create my Account')
   