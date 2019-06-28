from apps import create_app

app = create_app()

APP_CONFIG={
    'host': '0.0.0.0',
    'port': 9001,
    'debug': True
}


if __name__ == '__main__':
    app.run(**APP_CONFIG)