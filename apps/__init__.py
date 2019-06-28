from flask import Flask
from apis import init_api
from flask_cors import *



def create_app():
    app = Flask(__name__)   # 创建程序实例
    # app.register_blueprint(user_blue)   # 注册蓝图对象
    init_api(app)
    CORS(app, supports_credentials=True)
    return app