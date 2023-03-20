from wtforms.validators import ValidationError

def my_lenght_check(form, field):
    if len(field.data) > 66:
        raise ValidationError('The length of your password must be less than 66 characters.')