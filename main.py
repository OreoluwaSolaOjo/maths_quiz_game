import random

MIN_NB = 1
MAX_NB = 100
NB_QUESTIONS = 20
Question_Number = NB_QUESTIONS


def ask_question():
    a = random.randint(MIN_NB, MAX_NB)
    b = random.randint(MIN_NB, MAX_NB)

    o = random.randint(0, 1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    answer_str = input(f"What is {a} {operator_str} {b}?")
    compute = a+b
    if o == 1:
        compute = a*b
    answer_int = int(answer_str)
    if answer_int == compute:
        return True

    return False


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question no {i + 1} out of {NB_QUESTIONS}")
    if ask_question():
        print("You got it right yo")
        nb_points += 1
    else:
        print("You are so wrong")
    print()
print(f"You got {nb_points} out of {NB_QUESTIONS}")
average = int(NB_QUESTIONS)/2
if nb_points == NB_QUESTIONS:
    print("excellent")
elif nb_points == 0:
    print("You need to improve your maths")
elif nb_points <= average:
    print("Bad")
else:
    print("Good")
