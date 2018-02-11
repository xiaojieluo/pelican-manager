from flask_restplus import fields

class DictFields(fields.Raw):
    def format(self, value):
        if isinstance(value, dict):
            return value
        else:
            return False

article_fields = {
    'meta': DictFields,
    'text': fields.String,
    'path': fields.String,
}

article_list_fields = {
    # 'results': fields.List(fields.Nested(article_fields))
    'results':fields.List(fields.Nested(article_fields)),
}
