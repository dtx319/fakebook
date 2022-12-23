from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm): 
    name=StringField('first_name', validators=[DataRequired()])