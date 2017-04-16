"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   
   The three main benefits of object oriented design are abstraction,
   encapsulation, and polymorphism.
   
   Abstration:
   Abstraction is a way for programmers to use code without actually knowing
   what is going on inside. It is related to objection oriented programming in 
   that a programmer and utlize a class and use its methods/functions and attributes
   without knowing how the code was written.

   Encapution:
   Encapution means that functions for certain attributes are grouped together 
   and used together. With object oriented programming, the instance of the 
   object can call its methods (the object's own functions), and use variables
   that are within its own instance without passing it as arguments.

   Polymorphism
   Objection oriented programming allows for polymorphism, or the flexibility
   to change and add things as needed between a parent class and a child class.
   Child classes can inherit what it wants from the parent class and redefine 
   or customize parent functions/methods to behave differently for its own class.

2. What is a class?
    Classes are "smart dictionaries" in that a class has a bunch of attributes
    grouped together in a similar way. The difference is that a class has its
    attributes living close to its functions, which are called methods.

    A class does not need to pass all the contents of its "dictionary" into a
    method and can access those attributes internally. To do something to a 
    dictionary, the data needs to be passed into a function's arguments.

3. What is an instance attribute?
    When an object is instantiated, a copy of the class is created. The 
    attributes associated to that copy, or instance, are instance
    attributes. Those attributes can be changed for that instance. And other attributes can
    be added during that instance.

4. What is a method?
    A method is a function within a class with "self" as the first argument.
    "Self" refers to the instance that called the method. It is passed into
    the method so the method is able to use its attributes within the method.

5. What is an instance in object orientation?
    An instance is an individual occurence of a class. It is a copy of that
    class with specific attributes. A copy is made during the instantiation
    of that class. A user can then define that copy with specific traits and
    attributes. That instance lives for as long as the copy is being used.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   An instance attribute is an attribute from the copy or instantiation of that
   object. 

   A class attribute is normally an attribute that is defined for that
   class and doesn't change much. If there are two instances of the same class,
   and that class has a class attribute. When one instance changes the class
   attribute, then the other instance will have the same change. 

   For example, if there was a Car Class with a class attribute of number
   of wheels and a list of all the features, and then a "Sedan" object of Car
   and a "SUV" object of car were instantiated, each instance should have the
   same number of wheels, which is 4. 

   However, if the Sedan has a "sport feature" and it was added to the feature
   list, then the SUV would have the same feature list even if it did not have
   that feature. The class Car's feature list should then be created as an 
   instance variable, so then Sedan and SUV can have its own copy of that list
   and use it as needed without affecting the each other's lists.

"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Class Student that stores all the information in a dictionary."""
    def __init__(self, first_name, last_name, address):
        """Instantiates strings firstname, lastname, and address of student."""
        # student_info as instance variable as it changes from student to student
        self.student_info = {}
        self.student_info["first_name"] = first_name
        self.student_info["last_name"] = last_name
        self.student_info["address"] = address

    def __repr__(self):
        return "Student first_name: {}, last_name: {}, address: {}".format(
            self.student_info["first_name"], self.student_info["last_name"],
            self.student_info["address"])


class Question(object):
    """Class Question of just one question and answer. """
    def __init__(self, question, answer):
        """Instantiates with strings question and answer."""
        # dictionary of question_info
        self.question_info = {}
        self.question_info["question"] = question
        self.question_info["correct_answer"] = answer

    def __repr__(self):
        return "(Question: {}, Answer: {})".format(
            self.question_info["question"], self.question_info["correct_answer"])

    def ask_and_evaluate(self):
        """Returns a boolean based on user's answer to the question. """
        # Checking to see if user has correct answer to the question
        user_input = raw_input(self.question_info["question"] + " > ")
        if user_input == self.question_info["correct_answer"]:
            return True
        else:
            return False


class Exam(object):
    """Class Exam contains list of questions."""
    def __init__(self, name):
        """Contains name of the exam and a list of Questions object."""
        self.name = name
        self.questions = []

    def __repr__(self):
        return "{} exam contains {} questions.".format(
            self.name, len(self.questions))

    def add_question(self, question, answer):
        """ Adds a new question fo the list of questions for exam."""
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def administer(self):
        """ Takes exam and returns score."""
        # Correct counter
        total_correct = 0
        total_num_questions = len(self.questions)

        if total_num_questions == 0:
            return 0
        else:
            for q in self.questions:
                if q.ask_and_evaluate():
                    total_correct += 1
            # Return score as a percentage
            return (float(total_correct) / float(total_num_questions)) * 100


class StudentExam(object):
    """Object of student and exam that student takes. """
    # Keeping track of the score of when student takes a test
    score = 0

    def __init__(self, student, exam):
        """Takes in Student and Exam objects."""
        self.student = student
        self.exam = exam

    def __repr__(self):
        return "Student {} for exam {} has score {}.".format(
            self.student, self.exam, self.score)

    def take_test(self):
        self.score = self.exam.administer()
        print self.score


class Quiz(Exam):
    """Quiz Class"""
    def __repr__(self):
        return "{} quiz contains {} questions.".format(
            self.name, len(self.questions))

    def add_question(self, question, answer):
        """ Adds a new question to the quiz with max of 10 questions."""
        if len(self.questions) < 10:
            super(Quiz, self).add_question(question, answer)
        else:
            print "Only 10 questions can be added."

    def administer(self):
        """ Returns pass 1/fail 0."""
        if super(Quiz, self).administer() > 0.5:
            return 1
        else:
            return 0


class StudentQuiz(StudentExam):
    """Object of student and quiz that student should take."""
    # Keeping track of the score Pass or Fail for the exam
    score = None

    def __init__(self, student, quiz):
        """Contains the quiz that a student should take."""
        super(StudentQuiz, self).__init__(student, quiz)

    def __repr__(self):
        return "Student {} for quiz {} has score {}.".format(
            self.student, self.exam. self.score)

    def take_test(self):
        """Sets score of test as Pass or Fail."""
        if self.exam.administer() == 1:
            self.score = "Pass"
            print self.score
        else:
            self.score = "Fail"
            print self.score


def example():
    """ Example of using classes to create exam, student and administers exam."""
    hackbrighter = Student("Ivy", "Chen", "San Francisco")
    big_test = Exam("Big Test")
    small_test = Quiz("Small Quiz")

    f = open("test.txt")

    for line in f:
        q, a = line.rstrip().split(" > ")
        big_test.add_question(q, a)
        small_test.add_question(q, a)

    s1 = StudentExam(hackbrighter, big_test)
    s1.take_test()

    s2 = StudentQuiz(hackbrighter, small_test)
    s2.take_test()

example()
