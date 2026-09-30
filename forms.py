from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo 

class SignUP(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class CreateGroup(FlaskForm):
    groupname = StringField('Group Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create Group')


class JoinGroup(FlaskForm):
    groupname = StringField('Group Name', validators=[DataRequired()])
    groupcode = StringField('Group Code', validators=[DataRequired()])
    submit = SubmitField('Join Group')

class CreateTask(FlaskForm):
    taskname = StringField('Task Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
    assign_to = SelectField('Assign To',  coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Task')

class TaskStatusForm(FlaskForm):
    status = SelectField(
        'Status',
        choices=[
            ('To do', 'To do'),
            ('In progress', 'In progress'),
            ('Done', 'Done')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Update Status')