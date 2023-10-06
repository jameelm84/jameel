import random
import quiz_questions

quiz_questions = {
    # השאלות והתשובות מיובאות מקובץ quiz_questions.py
}

user_score = 0

def get_random_question():
    # בחירת שאלה רנדומלית
    question = random.choice(list(quiz_questions.keys()))
    return question, quiz_questions[question]

def check_answer(question, user_answer):
    # בדיקה האם התשובה נכונה
    correct_answer = quiz_questions[question]
    return user_answer.lower() == correct_answer.lower()
