import matplotlib.pyplot as plt
import numpy as np

# Characteristics Names
characteristics = [
    "Functional Suitability",
    "Performance Efficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# Your Actual Ratings
APP1_RATINGS = [5,4,4,4,5,5,5,4]
APP2_RATINGS = [4,5,4,5,4,5,5,4]

# Radar chart ke liye values repeat karte hain
values1 = APP1_RATINGS + [APP1_RATINGS[0]]
values2 = APP2_RATINGS + [APP2_RATINGS[0]]

# Angles set karna
angles = np.linspace(0, 2 * np.pi, len(characteristics), endpoint=False).tolist()
angles += angles[:1]

# Figure banana
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)

# App 1 plot
ax.plot(angles, values1, linewidth=2, label="TikTok")
ax.fill(angles, values1, alpha=0.1)

# App 2 plot
ax.plot(angles, values2, linewidth=2, label="Instagram")
ax.fill(angles, values2, alpha=0.1)

# Labels set karna
ax.set_xticks(angles[:-1])
ax.set_xticklabels(characteristics)

# Title + Legend
plt.title("Software Quality Comparison Radar Chart")
plt.legend(loc="upper right")

# Save PNG file
plt.savefig("radar_chart.png")

# Show chart
plt.show()