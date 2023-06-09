# model
import connection
import util

questions_csv = "data/question.csv"
answers_csv = "data/answer.csv"

HEADERS_Q = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
HEADERS_A = ["id", "submission_time", "vote_number", "question_id", "message", "image"]


def get_question_data_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file(questions_csv)
    for data in data_questions:
        if data['id'] == question_id:
            question_data = list(data.values())
            return question_data


def get_answers_by_question_id_dm(question_id):
    data_answers = connection.read_dict_from_file(answers_csv)
    for answer in data_answers:
        answer["submission_time"] = util.convert_timestamp_to_date(int(answer["submission_time"]))
    sorted_answers = sorted(data_answers, key=lambda x: x["submission_time"], reverse=True)
    answers = [[line["submission_time"], line['message'], line["id"],line["vote_number"], line["image"]] for line in sorted_answers if
               line['question_id'] == question_id]
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
    connection.write_dict_to_file_str(questions_csv, questions, HEADERS_Q)
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
    connection.write_dict_to_file_str(answers_csv, answers, HEADERS_A)


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


def delete_answer_dm(id, type):
    header = "question_id" if type == "question" else "id"
    answers = connection.read_dict_from_file(answers_csv)
    answers = [answer for answer in answers if answer.get(header) != id]
    connection.write_dict_to_file_str(answers_csv, answers, HEADERS_A)


def delete_question_dm(question_id):
    questions = connection.read_dict_from_file(questions_csv)
    questions = [question for question in questions if question.get('id') != question_id]
    connection.write_dict_to_file_str(questions_csv, questions, HEADERS_Q)


def get_question_id(answer_id):
    answers = connection.read_dict_from_file(answers_csv)
    for answer in answers:
        if answer['id'] == answer_id:
            return answer['question_id']


def update_question_dm(title, message, question_id):
    delete_question_dm(question_id)
    add_question_dm(title, message, question_id)


def vote_on_questions_dm(question_id, vote):
    questions = connection.read_dict_from_file(questions_csv)
    for question in questions:
        if question["id"] == question_id:
            number_of_vote = int(question["vote_number"])
            if vote == "up":
                number_of_vote += 1
            elif vote == "down":
                number_of_vote -= 1
            question["vote_number"] = number_of_vote
    connection.write_dict_to_file_str(questions_csv, questions, HEADERS_Q)

def vote_on_answers_dm(answer_id, vote):
    answers = connection.read_dict_from_file(answers_csv)
    for answer in answers:
        if answer["id"] == answer_id:
            number_of_vote = int(answer["vote_number"])
            if vote == "up":
                number_of_vote += 1
            elif vote == "down":
                number_of_vote -= 1
            answer["vote_number"] = number_of_vote
    connection.write_dict_to_file_str(answers_csv, answers, HEADERS_A)