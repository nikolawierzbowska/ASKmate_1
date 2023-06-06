import flask
from flask import Flask
import connection

app = Flask(__name__)


@app.route('/')
def main_page():
    return flask.render_template("main.html")


@app.route('/list')
def list_questions(file="question.csv"):
    user_questions = connection.read_dict_from_file(file)
    return flask.render_template("list.html", questions=user_questions)


if __name__ == "__main__":
    app.run()
