
from data import  question_data
from question_model import  Question
from quiz_brain import  QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

"""
    for q in question_bank:
    print(f"Quest: {q.text}, Ans: {q.answer}")

    print("q1: ", question_bank[0].text, "ans1: ", question_bank[0].answer)
"""

quiz = QuizBrain(question_bank)
quiz.next_question()
