class Question:
    def __init__(self, question_text, options, correct_answer, user_answer=None):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = user_answer

    def display_question(self):
        print(self.question_text)
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")
    
    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def is_correct(self):
        return self.user_answer == self.correct_answer


def main():
    # Define more questions
    question1 = Question(
        "Which planet is known as the Red Planet?",
        ["Mars", "Jupiter", "Venus", "Mercury"],
        "1"
    )

    question2 = Question(
        "What is the chemical symbol for water?",
        ["H2O", "CO2", "NaCl", "O2"],
        "1"
    )

    question3 = Question(
        "Who wrote 'Romeo and Juliet'?",
        ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
        "1"
    )

    question4 = Question(
        "What is the tallest mammal?",
        ["Giraffe", "Elephant", "Horse", "Kangaroo"],
        "1"
    )

    # List of questions
    questions = [question1, question2, question3, question4]

    # Quiz loop
    for question in questions:
        print("\n")
        question.display_question()
        user_input = input("Enter your choice (1, 2, 3, 4): ")
        question.set_user_answer(user_input)

    # Display results
    print("\nResults:")
    for index, question in enumerate(questions, 1):
        print(f"Question {index}: {question.question_text}")
        if question.is_correct():
            print("    Your answer is correct!")
        else:
            print("    Your answer is incorrect.")

if __name__ == "__main__":
    main()
