from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from .validators import my_lenght_check

class Form1(DynamicForm):
    field1 = StringField('field1',
            description=('Your field number one!'), 
            validators=[DataRequired(), my_lenght_check],
            widget=BS3TextFieldWidget())
    field2 = StringField('field2',
            description=('Your field number two!'),
            validators=[Email()],
            widget=BS3TextFieldWidget())