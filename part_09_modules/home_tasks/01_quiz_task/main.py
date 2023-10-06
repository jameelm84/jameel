from quiz_manager import *

print("----Welcome to the Game ---- \n note : to exit the game write 'quite'")

wrong_answers_counter = 0
while wrong_answers_counter < 3:
    question, answer = get_random_question()
    print("\nQuestion", question)

    user_answer = input("Your answer: ")
    if user_answer.lower() == "quite":
        break

    if check_answer(question, user_answer):
        print("your answer is correct")
        user_score +=1

    else:
        print("not correc the correct answer is -- >", answer)
        wrong_answers_counter +=1

print("Thanks for playing!")
print("your score is: ", user_score)
