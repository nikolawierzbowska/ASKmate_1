# model
import connection, server
import util

questions_csv = "data/question.csv"
answers_csv ="data/answer.csv"

def list_questions_dm():
    questions = connection.read_dict_from_file(questions_csv)
    for question in questions:
        question["submission_time"]=util.convert_timestamp_to_date(int(question["submission_time"]))
    sorted_questions =sorted(questions, key= lambda x: x["submission_time"], reverse=True)
    return sorted_questions


def get_question_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file(questions_csv)
    question = next((line["title"] for line in data_questions if line['id'] == question_id),"Not found")
    return question


def get_message_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file(questions_csv)
    message = next((line["message"] for line in data_questions if line['id'] == question_id),"Not found")
    return message

def get_answers_by_question_id_dm(question_id):
    data_answers = connection.read_dict_from_file(answers_csv)
    for answer in data_answers:
        answer["submission_time"] = util.convert_timestamp_to_date(int(answer["submission_time"]))
    sorted_answers = sorted(data_answers, key=lambda x: x["submission_time"], reverse=True)
    answers = [[line["submission_time"],line['message']] for line in sorted_answers if line['question_id'] == question_id]
    return answers


def add_question_dm(title, message):
    questions = connection.read_dict_from_file(questions_csv)
    new_question_id = str(util.generated_id(questions_csv))
    new_question = {
        'id':new_question_id,
        "submission_time":util.get_time(),
        "view_number":0,
        "vote_number":0,
        'title': title,
        'message': message,
        "image":0
    }
    questions.append(new_question)
    connection.write_dict_to_file_str(questions_csv, questions)
    return new_question_id


def add_answer_dm(message,question_id):
    answers = connection.read_dict_from_file(answers_csv)
    new_answer_id = str(util.generated_id(answers_csv))
    new_answer = {
        'id':new_answer_id,
        "submission_time":util.get_time(),
        "vote_number":0,
        "question_id":question_id,
        'message': message,
        "image":0
    }
    answers.append(new_answer)
    connection.write_dict_to_file_str(answers_csv, answers)

