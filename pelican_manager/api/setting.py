from flask import current_app, Blueprint
from flask_restplus import Resource, Api
from pelican_manager.config import Config

app = current_app
setting_api = Blueprint('setting_api', __name__, url_prefix='/api/settings')
api = Api(setting_api)


class SettingListApi(Resource):
    def get(self):
        print("settingsLstApi")
        config  = Config
        print(config.__dict__)

class SettingApi(Resource):
    def get(self, name):
        print(name)
        pass

api.add_resource(SettingApi, '/<string:name>')
api.add_resource(SettingListApi, '/')
