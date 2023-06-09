import connection
import util
import string

questions_csv = "data/question.csv"
answers_csv = "data/answer.csv"
#TODO lista question z csv


def get_question_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file(questions_csv)
    question = next((line["title"] for line in data_questions if line['id'] == question_id), "Not found")
    return question


def get_message_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file(questions_csv)
    message = next((line["message"] for line in data_questions if line['id'] == question_id), "Not found")
    return message


def get_answers_by_question_id_dm(question_id):
    data_answers = connection.read_dict_from_file(answers_csv)
    for answer in data_answers:
        answer["submission_time"] = util.convert_timestamp_to_date(int(answer["submission_time"]))
    sorted_answers = sorted(data_answers, key=lambda x: x["submission_time"], reverse=True)
    answers = [[line["submission_time"], line['message'], line['id']] for line in sorted_answers
               if line['question_id'] == question_id]
    return answers


def add_question_dm(title, message, question_id=0):
    questions = connection.read_dict_from_file(questions_csv)
    question_id = str(util.generated_id(questions_csv)) if question_id == 0 else question_id
    new_question = {
        'id': question_id,
        "submission_time": util.get_time(),
        "view_number": 0,
        "vote_number": 0,
        'title': title,
        'message': message,
        "image": 0

    }
    questions.append(new_question)
    connection.write_dict_to_file_str(questions_csv, questions)
    return question_id


def add_answer_dm(message, question_id):
    answers = connection.read_dict_from_file(answers_csv)
    new_answer_id = str(util.generated_id(answers_csv))
    new_answer = {
        'id': new_answer_id,
        "submission_time": util.get_time(),
        "vote_number": 0,
        "question_id": question_id,
        'message': message,
        "image": 0
    }
    answers.append(new_answer)
    connection.write_dict_to_file_str(answers_csv, answers)


def get_sorted_questions(order_by, order_direction):
    questions = connection.read_dict_from_file(questions_csv)
    for question in questions:
        question["submission_time"] = util.convert_timestamp_to_date(int(question["submission_time"]))
    if order_by == 'title':
        questions.sort(key=lambda q: q['title'].lower(), reverse=(order_direction == 'desc'))
    elif order_by == 'submission_time':
        questions.sort(key=lambda q: q['submission_time'], reverse=(order_direction == 'desc'))
    elif order_by == 'message':
        questions.sort(key=lambda q: q['message'].lower(), reverse=(order_direction == 'desc'))
    elif order_by == 'view_number':
        questions.sort(key=lambda q: int(q['view_number']), reverse=(order_direction == 'desc'))
    elif order_by == 'vote_number':
        questions.sort(key=lambda q: int(q['vote_number']), reverse=(order_direction == 'desc'))
    return questions


def delete_answer(id, type):
    answers = connection.read_dict_from_file(answers_csv)
    answers = [answer for answer in answers if answer.get('question_id' if type == "question" else 'id') != id]
    connection.write_dict_to_file_str(answers_csv, answers)


def delete_question(question_id):
    questions = connection.read_dict_from_file(questions_csv)
    questions = [question for question in questions if question.get('id') != question_id]
    connection.write_dict_to_file_str(questions_csv, questions)


def get_question_id(answer_id):
    answers = connection.read_dict_from_file(answers_csv)
    for answer in answers:
        if answer['id'] == answer_id:
            return answer['question_id']


def update_question(title, message, question_id):
    delete_question(question_id)
    add_question_dm(title, message, question_id)

