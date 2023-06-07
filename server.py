import flask
from flask import Flask, request
import connection
import data_manager

app = Flask(__name__)

@app.route('/')
def main_page():
    return flask.render_template("main.html")


@app.route('/list')
def list_questions():
    return flask.render_template("list.html", questions = data_manager.list_questions_dm())


@app.route('/question/<question_id>')
def print_question():
        return flask.render_template("question.html", question=list_questions(file="data/question.csv"))


if __name__ == "__main__":
    app.run()
