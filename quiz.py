from emoji import emojize

moj = emojize ("Packages are:thumbs_up:")
from components.quizQuestions import questions
from components import vars, quizTally
from colorama import init, Fore, Style
from PIL import Image

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("*****Prepare for next question******\n")


answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print(":sparkles:\n")

answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print(":sparkles:\n")

answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print(":sparkles:\n")

print("total so far: " + str(vars.quizTotal) + "\n")

#after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)
