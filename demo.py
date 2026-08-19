import random

def birthday_problem(n):
    birthdays = []

    for i in range(n):
        birthday = random.randint(1, 365)

        if birthday in birthdays:
            return True

        birthdays.append(birthday)

    return False


# Number of people
n = int(input("Enter number of people: "))

# Run the experiment many times
trials = 1000
matches = 0

for i in range(trials):
    if birthday_problem(n):
        matches += 1

probability = matches / trials

print("Probability of at least two people having the same birthday:",
      probability)