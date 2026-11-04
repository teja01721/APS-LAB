import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define population parameters
population_mean = 50
population_sd = 10
population_size = 10000

# Step 2: Generate population from normal distribution
population = np.random.normal(
    population_mean,
    population_sd,
    population_size
)

# Calculate population mean and standard deviation
pop_mean = np.mean(population)
pop_sd = np.std(population, ddof=0)

print("Population Mean:", pop_mean)
print("Population Standard Deviation:", pop_sd)

# Step 3: Generate 1000 random samples
number_of_samples = 1000
sample_size = 30

samples = []

for i in range(number_of_samples):
    sample = np.random.choice(population, sample_size, replace=False)
    samples.append(sample)

# Step 4: Calculate standard deviation of each sample
sample_sds = []

for sample in samples:
    sample_sd = np.std(sample, ddof=1)
    sample_sds.append(sample_sd)

# Step 5: Plot distribution of sample standard deviations
plt.figure(figsize=(10, 5))

plt.hist(sample_sds, bins=30, edgecolor='black')

plt.axvline(pop_sd, linestyle='--',
            label='Population SD')

plt.xlabel("Sample Standard Deviation")
plt.ylabel("Frequency")
plt.title("Distribution of Standard Deviations from 1000 Samples")
plt.legend()
plt.show()

# Step 6: Draw one random sample of 30 observations
random_sample = np.random.choice(population, 30, replace=False)

# Step 7: Calculate sample statistics
sample_mean = np.mean(random_sample)
sample_sd = np.std(random_sample, ddof=1)

# Sample Standard Error
sample_se = sample_sd / np.sqrt(30)

# Step 8: Display results
print("\nOne Random Sample of 30 Observations:")
print(random_sample)

print("\nSample Statistics:")
print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_sd)
print("Sample Standard Error:", sample_se)