import flask
from flask import Flask, request
import data_manager

app = Flask(__name__)

ID, SUBMISSION_TIME, VIEW_NUMBER = 0, 1, 2
VOTE_NUMBER, TITLE, MESSAGE = 3, 4, 5
IMAGE = 6


@app.route('/')
def main_page():
    return flask.render_template("main.html")


@app.route('/list')
def list_questions():
    order_by = flask.request.args.get('order_by')
    order_direction = flask.request.args.get('order_direction')
    questions = data_manager.get_sorted_questions(order_by, order_direction)
    return flask.render_template("list.html", questions=questions)


@app.route('/question/<question_id>')
def print_question(question_id):
    question = data_manager.get_question_data_by_id_dm(question_id)
    answers = data_manager.get_answers_by_question_id_dm(question_id)
    return flask.render_template('question.html', question=question[TITLE],
                                 message=question[MESSAGE], answers=answers, question_id=question_id)


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if flask.request.method == 'POST':
        title = flask.request.form['title']
        message = flask.request.form['message']
        new_question_id = data_manager.add_question_dm(title, message)
        return flask.redirect(f'/question/{new_question_id}')
    else:
        return flask.render_template('add_question.html', version="edit")


@app.route('/question/<question_id>/new_answer', methods=['GET', 'POST'])
def add_answer(question_id):
    if flask.request.method == 'POST':
        message = flask.request.form['message']
        data_manager.add_answer_dm(message, question_id)
        return flask.redirect(f'/question/{question_id}')
    elif flask.request.method == 'GET':
        return flask.render_template('add_answer.html', question_id=question_id)


@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    data_manager.delete_question(question_id)
    data_manager.delete_answer(question_id, "question")
    return flask.redirect('/list')


@app.route('/answer/<answer_id>/delete')
def delete_answer(answer_id):
    question_id = data_manager.get_question_id(answer_id)
    data_manager.delete_answer(answer_id, "answer")
    return flask.redirect(f'/question/{question_id}')


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    if flask.request.method == 'GET':
        question = data_manager.get_question_data_by_id_dm(question_id)
        return flask.render_template('edit_question.html', message=question[MESSAGE], question_id=question_id,
                                     title=question[TITLE])
    if flask.request.method == 'POST':
        title = flask.request.form['title']
        message = flask.request.form['message']
        data_manager.update_question(title, message, question_id)
        return flask.redirect(f'/question/{question_id}')


@app.route('/question/<question_id>/vote_up')
def vote_up(question_id):
    data_manager.vote_up_questions_dm(question_id)
    return flask.redirect('/list')


if __name__ == "__main__":
    app.run()
