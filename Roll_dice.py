import random

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def roll_dice():
    return random.randint(1, 6)

num_rolls = int(input("Anzahl der Würfe: "))

rolls = np.zeros(num_rolls)
mean_rolls = np.zeros(num_rolls)

for i in range(num_rolls):
    rolls[i] = roll_dice()
    mean_rolls[i] = np.mean(rolls[:i+1])

fig, ax = plt.subplots()
ax.plot(range(1, num_rolls+1), rolls, label="Augenzahl")
ax.plot(range(1, num_rolls+1), mean_rolls, label="Mittelwert")
ax.axhline(y=3.5, linestyle='--', color='gray', label="μ=3.5")
ax.legend()
plt.show()

final_mean = np.mean(rolls)
print("Finaler Mittelwert: ", final_mean)