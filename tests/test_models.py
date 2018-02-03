from pelican_manager.forms import ArticleForm, SettingForm
from wtforms import StringField, IntegerField, Field

def test_article_model():
    article_fields = [
        ('title', StringField),
        ('authors',StringField),
        ('tags',StringField),
        ( 'status', StringField),
        ('created_at', StringField),
        ('updated_at', StringField),
    ]

    for fields in article_fields:
        key, value = fields
        assert key in ArticleForm.__dict__

def test_setting_model():
    setting_fields = [
        ('server_debug', StringField),
        ('server_port', IntegerField),
        ('path', StringField),
    ]

    for fields in setting_fields:
        key, value = fields
        assert key in SettingForm.__dict__
