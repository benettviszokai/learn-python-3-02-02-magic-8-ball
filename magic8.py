import random

# Player's name
name = "James"

# Question
question = "Do you like this course?"

# Magic Ball's answer - empty for now.
answer = ""

# Random number generation - generating a random number between 1 and 11 (inclusive)
random_number = random.randint(1,11)

# Control Flow
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "I don't know, ask somebody else"
elif random_number == 11:
  answer = "Well, yeah... or not"
else:
  answer = "Error"

# Program in action

# Checking if there's a valid question or not
if question == "":
  print("That's not a valid question, sorry.")
else:
  # Checking if the player has a name or not
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks: " + question)

  # Printing out the ball's answer
  print("Magic 8-Ball's answer: " + answer)
