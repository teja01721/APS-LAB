import random
import matplotlib.pyplot as plt


def birthday_problem(n):
    birthdays = []

    for i in range(n):
        birthday = random.randint(1, 365)

        if birthday in birthdays:
            return True

        birthdays.append(birthday)

    return False


# Store results for the graph
people = []
probabilities = []

trials = 1000

# Test groups from 1 to 60 people
for n in range(1, 61):

    matches = 0

    for i in range(trials):
        if birthday_problem(n):
            matches += 1

    probability = matches / trials

    people.append(n)
    probabilities.append(probability)


# Print probability for 23 people
print("Probability for 23 people:", probabilities[22])


# Plot graph
plt.plot(people, probabilities, marker='o')

plt.xlabel("Number of People")
plt.ylabel("Probability of Shared Birthday")
plt.title("Birthday Problem")

plt.grid(True)
plt.show()