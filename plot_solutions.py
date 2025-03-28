import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"...\Project\EmptyVSCodeProject\build\src\solutions.txt")
eigenvals = np.loadtxt(r"...\Project\EmptyVSCodeProject\build\src\eigenvals.txt")
borders = np.loadtxt(r"...\Project\EmptyVSCodeProject\build\src\borders.txt")

# INFINITE WELL

y_positions = []
y_labels = []
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(2, min(8, data.shape[0])): 
   shift = 6*eigenvals[i]
   ax.plot(data[i] + shift, label=f'State {i-2}')
   y_positions.append(shift)
   y_labels.append(f"E{i-2} ({round(eigenvals[i],2)} eV)")

ticks = list(ax.get_yticks())
labels = [tick.get_text() for tick in ax.get_yticklabels()]

all_ticks = ticks + y_positions
all_labels = labels + y_labels

ax.set_xticks([0, data.shape[0] - 1], [f"{borders[0]}", f"{borders[1]}"])
ax.set_yticks(y_positions)
ax.set_yticklabels(y_labels)
ax.set_xlabel("Well dimensions (nm)")
ax.set_title("First 6 solutions of infinite well")
ax.legend()
ax.grid()
plt.show()



# INFINITE GAUSSIAN

# y_positions = []
# y_labels = []
# fig, ax = plt.subplots(figsize=(10, 6))
# for i in range(min(6, data.shape[0])): 
#     shift = 1.7*eigenvals[i]
#     ax.plot(data[i] + shift, label=f'State {i}')
#     y_positions.append(shift)
#     y_labels.append(f"E{i} ({round(eigenvals[i],2)} eV)")

# ticks = list(ax.get_yticks())
# labels = [tick.get_text() for tick in ax.get_yticklabels()]

# all_ticks = ticks + y_positions
# all_labels = labels + y_labels

# ax.set_xticks([0, data.shape[0] - 1], [f"{borders[0]}", f"{borders[1]}"])
# ax.set_yticks(y_positions)
# ax.set_yticklabels(y_labels)
# ax.set_xlabel("Well dimensions (nm)")
# ax.set_title("First 6 solutions of infinite Gaussian")
# ax.legend()
# ax.grid()
# plt.show()
