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
    question_info = {}

    def __init__(self, question, answer):
        """Instantiates with strings question and answer."""
        self.question_info["question"] = question
        self.question_info["correct_answer"] = answer

    def __repr__(self):
        return "Question: {}, Answer: {}".format(
            self.question_info["question"], self.question_info["correct_answer"])

    def ask_and_evaluate(self):
        """Returns a boolean based on user's answer to the question. """
        user_input = raw_input(self.question_info["question"] + " > ")
        if user_input == self.question_info["correct_answer"]:
            print True
        else:
            print False


class Exam(object):
    """Class Exam contains list of questions.
    """
    questions = []
    total_num_questions = 0
    score = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass

    def add_question(self, question, answer):
        new_question = Question(question, answer)
        self.questions.append(new_question)
        self.total_num_questions += 1

    def administer(self):

    

class StudentExam(object, Exam):
    pass
