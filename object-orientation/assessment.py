"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   The three main benefits of object oriented design are abstraction,
   encapsulation, and polymorphism.
   
   Abstration:
   Abstracti

2. What is a class?

3. What is an instance attribute?
An instance attribute is something that is assigned of an object's instance.

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Class Student that stores all the information in a dictionary."""
    student_info = {}
    def __init__(self, first_name, last_name, address):
        """Instantiates strings firstname, lastname, and address of student."""
        self.student_info["first_name"] = first_name
        self.student_info["last_name"] = last_name
        self.student_info["address"] = address

    def __repr__(self):
        return "Student - first_name: {}, last_name: {}, address: {}".format(
            self.student_info["first_name"], self.student_info["last_name"],
            self.student_info["address"])


class Question(object):
    """Class Question of just one question and answer. """
    def __init__(self, question, answer):
        """Instantiates with strings question and answer."""
        self.question_info = {}
        self.question_info["question"] = question
        self.question_info["correct_answer"] = answer

    def __repr__(self):
        return "(Question: {}, Answer: {})".format(
            self.question_info["question"], self.question_info["correct_answer"])

    def ask_and_evaluate(self):
        """Returns a boolean based on user's answer to the question. """
        user_input = raw_input(self.question_info["question"] + " > ")
        if user_input == self.question_info["correct_answer"]:
            return True
        else:
            return False


class Exam(object):
    """Class Exam contains list of questions."""
    # list of Questions in the exam
    questions = []

    def __init__(self, name):
        self.name = name
        # self.questions = []

    def __repr__(self):
        return "{} exam contains {} questions.".format(
            self.name, len(self.questions))

    def add_question(self, question, answer):
        """ Adds a new question fo the list of questions for exam."""
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def administer(self):
        """ Takes exam and returns score."""
        total_correct = 0
        total_num_questions = len(self.questions)

        if total_num_questions == 0:
            return 0
        else:
            for q in self.questions:
                if q.ask_and_evaluate():
                    total_correct += 1
            return (float(total_correct) / float(total_num_questions)) * 100


class StudentExam(object):
    """Object of student and test score. """
    score = 0

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def __repr__(self):
        return "Student {} for exam {}.".format(
            self.student, self.exam)

    def take_test(self):
        self.score = self.exam.administer()
        print self.score


class Quiz(Exam):
    """Quiz Class"""
    def __repr__(self):
        return "{} quiz contains {} questions.".format(
            self.name, len(self.questions))

    def administer(self):
        """ Returns pass/fail."""
        total_correct = 0
        total_num_questions = len(self.questions)

        if total_num_questions == 0:
            return None
        else:
            for q in self.questions:
                if q.ask_and_evaluate():
                    total_correct += 1
            if (float(total_correct) / float(total_num_questions)) * 100 > 0.5:
                return 1
            else:
                return 0


def example():
    """ Example of using classes to create exam, student and administers exam."""

    hackbrighter = Student("Ivy", "Chen", "San Francisco")
    week_2_assessment = Exam("Big Test")

    f = open("test.txt")

    for line in f:
        q, a = line.rstrip().split(" > ")
        week_2_assessment.add_question(q, a)
    print week_2_assessment
    s = StudentExam(hackbrighter, week_2_assessment)
    s.take_test()

example()
