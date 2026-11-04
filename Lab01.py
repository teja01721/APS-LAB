# 1.Problem1: A fair coin is tossed 100 times.Calculate:
# Number of heads 
# Number of tails 
# Experimental probability of Head 
# Experimental probability of Tail


import numpy as np
import matplotlib.pyplot as plt

import numpy as np

# Toss a fair coin 100 times
n = 100

coin = np.random.choice(["Head", "Tail"], size=n)

# Count heads and tails
heads = np.sum(coin == "Head")
tails = np.sum(coin == "Tail")

# Calculate experimental probabilities
p_head = heads / n
p_tail = tails / n

print("Total Tosses:", n)
print("Number of Heads:", heads)
print("Number of Tails:", tails)
print("Experimental Probability of Head:", p_head)
print("Experimental Probability of Tail:", p_tail)



import numpy as np
import matplotlib.pyplot as plt

# Different numbers of trials
trials = [10, 100, 1000, 10000]

head_probabilities = []

for n in trials:

    # Toss coin n times
    coin = np.random.choice(["Head", "Tail"], size=n)

    # Count heads
    heads = np.sum(coin == "Head")

    # Calculate experimental probability
    p_head = heads / n

    head_probabilities.append(p_head)

    print("Number of Trials:", n)
    print("Heads:", heads)
    print("Experimental Probability of Head:", p_head)
    print()

# Plot the results
plt.figure(figsize=(8, 5))

plt.plot(trials, head_probabilities, marker='o',
         label="Experimental Probability")

plt.axhline(y=0.5, linestyle='--',
            label="Theoretical Probability = 0.5")

plt.xscale("log")
plt.xlabel("Number of Trials")
plt.ylabel("Probability of Head")
plt.title("Effect of Number of Trials on Experimental Probability")
plt.legend()
plt.grid()
plt.show()