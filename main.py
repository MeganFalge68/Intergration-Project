"""My Quiz Game Integration Project"""
__author__ = "Megan Falge"

# Megan Falge
# Quiz Game to study the textbook
print('-' * (2**5))


def main():
    """This is my main"""
    print("Hello User!", sep="\n")
    print("This will help you study the Introduction of Computer Science")
    print("There will be", "20 questions total. ", end=" ")
    name = input("To begin, print name: ")
    print("Well,", name, "lets start!", end=" ")

    # ---------------------------------------------

    questions = [
        {
            "Question": "A sequence of instructions that specifies how to perform a computation. ",
            "Answer": "B"
        },
        {
            "Question": "A program that reads and executes Python Code. ",
            "Answer": "C"
        },
        {
            "Question": "What is the process of finding and correcting bugs? ",
            "Answer": "B"
        },
        {
            "Question": "What is an example of a keyword? ",
            "Answer": "A"
        },
        {
            "Question": "What is not an example of a keyword in the Python Language? ",
            "Answer": "B"
        },
        {
            "Question": "A combination of values, variables, and operators. ",
            "Answer": "C"
        },
        {
            "Question": "What symbol starts a comment? ",
            "Answer": "B"
        },
        {
            "Question": "Which of these is not a debug error? ",
            "Answer": "A"
        },
        {
            "Question": "An error in the structure of a program and rules about that structure. ",
            "Answer": "C"
        },
        {
            "Question": "Runs without generating error messages, but will not do the right thing. ",
            "Answer": "A"
        },
        {
            "Question": "The error does not appear until after the program has started running. ",
            "Answer": "B"
        },
        {
            "Question": "What is a part of a program that can run repeatedly? ",
            "Answer": "C"
        },
        {
            "Question": "A type of expression that is either true or false? ",
            "Answer": "A"
        },
        {
            "Question": "A statement that controls the flow of execution depending on condition. ",
            "Answer": "A"
        },
        {
            "Question": "What is it called when part of a program can never run? ",
            "Answer": "C"
        },
        {
            "Question": "A type of loop in which the terminating condition is never satisfied. ",
            "Answer": "B"
        },
        {
            "Question": "What is something a variable can refer to? ",
            "Answer": "A"
        },
        {
            "Question": "An ordered collection of other values. ",
            "Answer": "C"
        },
        {
            "Question": "What is an expression called in brackets? ",
            "Answer": "B"
        },
        {
            "Question": "What is a sequence of values? ",
            "Answer": "A"
        }
    ]

    # ---------------------------------------------

    options = [
        ["A) Input ", "B) Program ", "C) Conditional Execution "],
        ["A) Integer ", "B) Prompt ", "C) Interpreter "],
        ["A) Bug ", "B) Debugging ", "C) Syntax "],
        ["A) Class ", "B) Stop ", "C) it "],
        ["A) while ", "B) when ", "C) continue "],
        ["A) Statement ", "B) Executes ", "C) Expression "],
        ["A) / ", "B) # ", "C) % "],
        ["A) Multiple ", "B) Syntax ", "C) Runtime "],
        ["A) Semantic ", "B) Runtime ", "C) Syntax "],
        ["A) Semantic ", "B) Runtime ", "C) Syntax "],
        ["A) Semantic ", "B) Runtime ", "C) Syntax "],
        ["A) Interface ", "B) Method ", "C) Loop "],
        ["A) Boolean Expression ", "B) Expression ", "C) Rational Expression "],
        ["A) Conditional Statement ", "B) Compound Statement ", "C) Print Statement "],
        ["A) Ending Code ", "B) Pause Code ", "C) Dead Code "],
        ["A) Nested Loop ", "B) Infinite Loop ", "C) For Loop "],
        ["A) Object ", "B) Sequence ", "C) Item "],
        ["A) Slice ", "B) Traversal ", "C) Sequence "],
        ["A) String ", "B) Index ", "C) Expression "],
        ["A) List ", "B) Map ", "C) Nested List "]
    ]

    # ---------------------------------------------

    correct = 0
    question_num = 0
    total_questions = len(questions)

    for x in questions:
        print('\n')
        print(x["Question"])
        for i in options[question_num]:
            print(i)
        guess = input("Answer is A, B, or C: ")
        valid_guess = is_valid(guess)
        while valid_guess is not True:
            guess = input("Answer is A, B, or C: ")
            guess = guess.upper()
            valid_guess = is_valid(guess)

        # user_guess.append(guess)
        correct += checking_answers(x["Answer"], guess)
        print("correct = " + str(correct))
        question_num += 1

    score = (correct / total_questions)
    print("total correct = " + str(score * 100))
    if score >= 90:
        print("Amazing!")
    elif score < 90 and (score >= 80):
        print("Great Job!")
    elif score < 80 and (score >= 70):
        print("Nice Job")
    elif score < 70 and (score >= 60):
        print("You did okay.")
    else:
        print("Study and try again!")

    # ---------------------------------------------


def is_valid(guess):
    """Checks if input is Valid"""
    guess = guess.upper()
    return guess == "A" or guess == "B" or guess == "C"


def checking_answers(answer, guess):
    """This is checking if answers are correct."""
    print("answer={}, guess={}".format(answer, guess))
    if answer == guess:
        print("Correct Answer!")
        return 1
    else:
        print("Wrong")
        return 0


main()
