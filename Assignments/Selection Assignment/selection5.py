"""
selection5.py
Kevin Xu

This is a simple trivia program about United States history. It asks the user 10 questions and will indicate whether or not the user
got it correct. The program will display the total score of the user at the end.
"""


score = 0    # This is the counter for the score.

# Questions - Each of the questions asks the user for an input and checks if it matches the correct answer
# If the answer that the user gave is correct, the score counter's value increases by one. If the
# answer is incorrect, the counter doesn't change and the correct answer will be printed.

answer1 = input("Who was the third president of the United States? > ")
if answer1.upper() == "THOMAS JEFFERSON" or answer1.upper() == "JEFFERSON":   #The .upper is just here for the
    score += 1                                                                # capitalization. even if the user
    print("Correct!")                                                         # enters somethings like "tHomas JefFeRson"
else:                                                                         # it will still be correct.
    print("Incorrect. It was Thomas Jefferson.")

answer2 = input("Which General led the Confederate army during the Civil War? > ")
if answer2.upper() == "ROBERT E LEE" or answer2.upper() == "ROBERT E. LEE":
    score += 1
    print("Correct!")
else:
    print("Incorrect. It was actually Robert E. Lee")

answer3 = input("Who was the first U.S. president to ever be impeached? > ")
if answer3.upper() == "ANDREW JOHNSON":
    score += 1
    print("Correct!")
else:
    print("Incorrect. Andrew Johnson, the 17th president of the United States was the first president to ever be impeached.")

answer4 = input("Who was the individual that passed the Emancipation Proclamation?> ")
if answer4.upper() == "ABRAHAM LINCOLN" or answer4.upper() == "LINCOLN":
    score += 1
    print("Correct!")
else:
    print("Incorrect. Abraham Lincoln passed the Emancipation Proclamation.")

answer5 = input("In what year was the Emancipation Proclamation issued? > ")
if answer5 == 1863:
    score += 1
    print("Correct!")
else:
    print("Incorrect. Lincoln passed the Emancipation Proclamation in 1863.")

answer6 = input("In what year was the Declaration of Independence signed? > ")
if answer6 == 1776:
    score += 1
    print("Correct!")
else:
    print("Incorrect. It was signed August 2, 1776.")

answer7 = input("Who was the first U.S. president to win a Noble Peace Prize? > ")
if answer7.upper() == "THEODORE ROOSEVELT" or answer7.upper() == "TEDDY ROOSEVELT":
    score += 1
    print("Correct!")
else:
    print("Incorrect. It was actually Theodore Roosevelt.")

answer8 = input("Which Amendment to the Constitution ended slavery in the United States?> ")
if answer8 == "13" or answer8 == "13th":
    score += 1
    print("Correct!")
else:
    print("Incorrect. It was the 13th Amendment.")

answer9 = input("Who was the only U.S. president to ever serve more than two terms in office?> ")
if answer9.upper() == "FRANKLIN D. ROOSEVELT" or answer9.upper() == "FRANKLIN ROOSEVELT":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The only president that served more than two terms is Franklin D. Roosevelt.")

answer10 = input("In which year was George H.W. Bush elected president?> ")
if answer10.upper() == "1988":
    score += 1
    print("Correct!")
else:
    print("Incorrect. He was elected president in 1988.")


# Scoring - To make it more fun, I've decided that the program will give different messages for different scores.
# There are multiple scoring ranges and the lines below will check which category the user's score belongs to and
# will print a special message and the user's percentage.

if score == 10:
    print("""
Great job! You got a perfect score!""")
    print("Score:",score)
elif score < 10 and score >= 5:
    print("""
Good Job! You got """,score," points! That is ",int(round(((score / 10) * 100), 0 )),"% of the questions right!", sep = "")
elif score < 5 and score > 0:
    print("""
You got """, score, " points. That is only ", int(round(((score / 10) * 100), 0 )),"% of them right. :(", sep = "")
elif score == 0:
    print("How did you manage to not get any of these questions correctly???? You got 0%. >:(")

# .title()     -   capitalizes the first letter in each word.