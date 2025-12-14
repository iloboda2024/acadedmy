import random

name = input("Enter your name")
question = "Yes or No"
answer = ""
random_number = random.randint(1,9)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
else:
  answer = "Error"

print(name + " asks:" + "Will war end this year?")
print("Magic 8-Ball's answer: " + answer)
