from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    authors = StringField('Authors')
    tags = StringField('Tags')
    status = StringField('Status')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')

class SettingForm(FlaskForm):
    debug = IntegerField("Debug")
    port = IntegerField('Port')
    path = StringField("Path")
