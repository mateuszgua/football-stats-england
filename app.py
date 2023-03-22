from views import app as application

if __name__ == '__main__':
    with application.app_context():
        application.config.from_object('config.DevelopmentConfig')
    application.run(host='0.0.0.0')
