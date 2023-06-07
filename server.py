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
def print_question(question_id):
    question = data_manager.get_question_by_id_dm(question_id)
    message = data_manager.get_message_by_id_dm(question_id)
    answers = data_manager.get_answers_by_question_id_dm(question_id)
    return flask.render_template('question.html', question=question,message =message, answers=answers)


if __name__ == "__main__":
    app.run()
