from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_url = StringField('Profile Image Url')
    password = PasswordField('password', validators=[Length(min=6)])
    #make sure to add a confirmation in users.new
    # confirm_password = PasswordField('password', validators=[Length(min=6)])

class EditUserForm(FlaskForm):
    name = StringField('Name')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_url = StringField('Profile Image Url')
    header_image_url = StringField('Header Image Url')
    location = StringField('Location')
    bio = StringField('Bio')
    password = PasswordField('Please reenter your password', validators=[Length(min=6)])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
