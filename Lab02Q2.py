import numpy as np
import matplotlib.pyplot as plt

# Roll a fair die 6000 times
n = 6000

rolls = np.random.randint(1, 7, size=n)

# Count frequency of each outcome
outcomes = np.arange(1, 7)

frequencies = []

for i in outcomes:
    count = np.sum(rolls == i)
    frequencies.append(count)

# Calculate experimental probabilities
probabilities = np.array(frequencies) / n

# Display results
for i in range(6):
    print("Outcome:", outcomes[i],
          "Frequency:", frequencies[i],
          "Probability:", probabilities[i])

# Plot probabilities
plt.figure(figsize=(8, 5))

plt.bar(outcomes, probabilities, edgecolor='black')

plt.axhline(y=1/6, linestyle='--',
            label="Theoretical Probability = 1/6")

plt.xlabel("Die Outcome")
plt.ylabel("Experimental Probability")
plt.title("Experimental Probability of Rolling a Die")
plt.xticks(outcomes)
plt.legend()
plt.show()



import numpy as np

# Roll a die 10000 times
n = 10000

rolls = np.random.randint(1, 7, size=n)

# Define events
A = (rolls == 1)
B = (rolls == 6)

# Calculate probabilities
p_A = np.sum(A) / n
p_B = np.sum(B) / n

# Intersection probability
p_intersection = np.sum(A & B) / n

# Union probability
p_union = np.sum(A | B) / n

# Verify addition rule
rhs = p_A + p_B

print("P(A):", p_A)
print("P(B):", p_B)
print("P(A intersection B):", p_intersection)
print("P(A union B):", p_union)
print("P(A) + P(B):", rhs)

print("\nVerification:")
print("P(A union B) =", p_union)
print("P(A) + P(B) =", rhs)



import numpy as np

# Generate 10000 die rolls
n = 10000

rolls = np.random.randint(1, 7, size=n)

# Define events
A = (rolls % 2 == 0)
B = (rolls > 3)

# Calculate individual probabilities
p_A = np.sum(A) / n
p_B = np.sum(B) / n

# Calculate intersection
p_intersection = np.sum(A & B) / n

# Calculate union
p_union = np.sum(A | B) / n

# Apply addition rule
rhs = p_A + p_B - p_intersection

print("P(A):", p_A)
print("P(B):", p_B)
print("P(A intersection B):", p_intersection)
print("P(A union B):", p_union)

print("\nVerification:")
print("P(A union B):", p_union)
print("P(A) + P(B) - P(A intersection B):", rhs)



import numpy as np

# Number of trials
n = 10000

# Toss a coin
coin = np.random.choice(["Head", "Tail"], size=n)

# Roll a die
die = np.random.randint(1, 7, size=n)

# Define events
A = (coin == "Head")
B = (die % 2 == 0)

# Calculate individual probabilities
p_A = np.sum(A) / n
p_B = np.sum(B) / n

# Calculate intersection probability
p_intersection = np.sum(A & B) / n

# Apply multiplication rule
rhs = p_A * p_B

print("P(A) - Probability of Head:", p_A)
print("P(B) - Probability of Even Number:", p_B)

print("P(A intersection B):", p_intersection)
print("P(A) * P(B):", rhs)

print("\nVerification:")
print("Actual P(A intersection B):", p_intersection)
print("Calculated P(A) * P(B):", rhs)