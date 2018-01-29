from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    authors = StringField('Authors')
    tags = StringField('Tags')
    status = StringField('Status')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')
