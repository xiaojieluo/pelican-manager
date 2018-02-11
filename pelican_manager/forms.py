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
    server_debug = IntegerField("Debug")
    server_port = IntegerField('Port')
    path = StringField("Path")

class ServerSettingForm(FlaskForm):
    server_debug = IntegerField("Debug")
    server_port = IntegerField('Port')
    page_size = IntegerField('Page Size')
    page_hide_column = StringField('hide columns')
    title_color_with_status = IntegerField('Title color with status')
