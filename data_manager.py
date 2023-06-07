# model
import connection, server
import util


def list_questions_dm():
    questions = connection.read_dict_from_file("data/question.csv")
    for question in questions:
        question["submission_time"]=util.convert_timestamp_to_date(int(question["submission_time"]))
    sorted_questions =sorted(questions, key= lambda x: x["submission_time"], reverse=True)
    return sorted_questions


def get_question_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file("data/question.csv")
    question = next((line["title"] for line in data_questions if line['id'] == question_id),"Not found")
    return question


def get_message_by_id_dm(question_id):
    data_questions = connection.read_dict_from_file("data/question.csv")
    message = next((line["message"] for line in data_questions if line['id'] == question_id),"Not found")
    return message

def get_answers_by_question_id_dm(question_id):
    data_answers = connection.read_dict_from_file('data/answer.csv')
    answers = [line['message'] for line in data_answers if line['question_id'] == question_id]
    return answers

