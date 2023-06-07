# model
import connection, server
import util

def list_questions_dm():
    questions = connection.read_dict_from_file("data/question.csv")
    for question in questions:
        question["submission_time"]=util.convert_timestamp_to_date(int(question["submission_time"]))
    sorted_questions =sorted(questions, key= lambda x: x["submission_time"], reverse=True)
    return sorted_questions


# def get_question_by_id(question_id):
#     for question in connection.read_dict_from_file("data/question.csv"):
#         return question if question['id'] == question_id[0] else print("not found question")
