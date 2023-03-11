from flask import Flask
from flask import render_template
from flask import redirect

from database_reader import DatabaseReader

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('flask_settings.Config')


@app.route('/')
def main():
    return "Hello world!"


if __name__ == '__main__':
    app.run()
