import random
print("Fitness knowledge test")
print("Every question gives you one point.")
print("You should select from options 'A', 'B' or 'C'")
print("If you score eight points or more, you have a good knowledge foundation\n"
      "for potential fitness and health results!")
print("Good luck!")
print("")


questions_list = ["What's the amount of calories in 1 gram of protein?", "What is the amount of calories in 1 gram of fat?",
                  "What is the amount of calories in 1 gram of carbohydrates?", "Which body part is the main mover in the bench press?",
                  "What is the main macronutrient in a banana?", "What is the main macronutrient in a chicken fillet?",
                  "Which part of the body is the main mover in the pull-up.", "What is the main macronutrient in rice?",
                  "What is the main macronutrient in almonds?", "What is the main focus of a set if it's in the repetition range from 1 to 6?",
                  "What is the main focus of a set if it's in the repetition range from 6 to 15?"]


len_list = len(questions_list)
points = 0
question_number = 1
for question in range(len_list):
    current_question = random.choice(questions_list)
    if current_question == "What's the amount of calories in 1 gram of protein?":
        print(f"{question_number}.{current_question}")
        print("A: 4\nB: 2\nC: 7")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'.")
    elif current_question == "What is the amount of calories in 1 gram of fat?":
        print(f"{question_number}.{current_question}")
        print("A: 15\nB: 9\nC: 3")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "b":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'B'")
    elif current_question == "What is the amount of calories in 1 gram of carbohydrates?":
        print(f"{question_number}.{current_question}")
        print("A: 4\nB: 8\nC: 5")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'")
    elif current_question == "Which body part is the main mover in the bench press?":
        print(f"{question_number}.{current_question}")
        print("A: Legs\nB: Triceps\nC: Chest")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'C'")
    elif current_question == "What is the main macronutrient in a banana?":
        print(f"{question_number}.{current_question}")
        print("A: Protein\nB: Carbohydrate\nC: Fat")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "b":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'B'")
    elif current_question == "What is the main macronutrient in a chicken fillet?":
        print(f"{question_number}.{current_question}")
        print("A: Fat\nB: Carbohydrate\nC: Protein")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'c'")
    elif current_question == "Which part of the body is the main mover in the pull-up.":
        print(f"{question_number}.{current_question}")
        print("A: Shoulders\nB: Biceps\nC: Back")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'C'")
    elif current_question == "What is the main macronutrient in rice?":
        print(f"{question_number}.{current_question}")
        print("A: Carbohydrate\nB: Protein\nC: Fat")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'")
    elif current_question == "What is the main macronutrient in almonds?":
        print(f"{question_number}.{current_question}")
        print("A: Protein\nB: Carbohydrate\nC: Fat")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "c":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'C'")
    elif current_question == "What is the main focus of a set if it's in the repetition range from 1 to 6?":
        print(f"{question_number}.{current_question}")
        print("A: Strength\nB: Hypertrophy\nC: Repetition range is irrelevant")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "a":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'A'")
    elif current_question == "What is the main focus of a set if it's in the repetition range from 6 to 15?":
        print(f"{question_number}.{current_question}")
        print("A: Strength\nB: Hypertrophy\nC: Endurance")
        question_number += 1
        questions_list.remove(current_question)
        answer = input().lower()
        if answer == "b":
            points += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
            print("The right answer is 'B'")
if points >= 8:
    print("\033[93mYou can start your fitness journey!\033[0m")
    print(f"\033[93mYou have {points} correct answer, from 11!\033[0m")
elif points < 8:
    print("\033[93mYou need some more learning.\033[0m")
    print(f"\033[93mYou have {points} correct answer, from 11!\033[0m")
