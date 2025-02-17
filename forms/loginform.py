from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired(),
                                       Length(min=4, max=15)])
    password = PasswordField(
        'password', validators=[InputRequired(),
                                Length(max=80)])
    remember = BooleanField('remember me')