from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
