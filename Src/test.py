import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt

# Generate random fish lengths (replace this with your actual array)
a = np.random.rand(1000)

# Create a histogram with manually normalized frequencies
counts, bins, _ = plt.hist(a, bins=np.linspace(0, 1, 101), edgecolor='black', density=False)

# Normalize counts to get relative frequencies
relative_frequencies = counts / sum(counts)

# Create a new figure for the plot
plt.figure()

# Plot the normalized histogram
plt.bar(bins[:-1], relative_frequencies, width=0.01, edgecolor='black')

# Set labels and title
plt.title('Fish Length Distribution (Relative Frequencies)')
plt.xlabel('Fish Length')
plt.ylabel('Relative Frequency')

# Show the plot
plt.show()
