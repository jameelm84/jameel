from quiz_manager import get_random_question, check_answer, user_score


def main():
    print("Welcome to the Python Quiz Game!")
    while True:
        # בחירת שאלה רנדומלית
        question, correct_answer = get_random_question()
        print("Question:", question)

        user_answer = input("Your answer (or 'quit' to exit): ")
        if user_answer.lower() == 'quit':
            break

        # בדיקת התשובה
        if check_answer(question, user_answer):
            print("Correct!")
            global user_score
            user_score += 1
        else:
            print("Wrong answer. The correct answer is:", correct_answer)

        print("Your score:", user_score)
        print("\nNext question!\n")


if __name__ == "__main__":
    main()
