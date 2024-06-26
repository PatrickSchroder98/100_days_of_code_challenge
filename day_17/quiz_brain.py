class QuizBrain:
    """Class to maintain the quiz logic."""
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Returns True or False depending if there are more questions left on the list."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Takes answer from user, calls method to check it, increments the question number."""
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False):")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        """Checks the answer given by user, displays the correct answer and current score."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
