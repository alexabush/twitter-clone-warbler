from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[Length(min=6)])
    #make sure to add a confirmation in users.new
    # confirm_password = PasswordField('password', validators=[Length(min=6)])

class EditUserForm(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    image_url = StringField('image_url')
    header_image_url = StringField('header_image_url')
    location = StringField('location')
    bio = StringField('bio')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[Length(min=6)])
