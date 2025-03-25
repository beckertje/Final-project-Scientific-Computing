# Tom Becker
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"C:\Users\tombe\Documents\Master\Scientific Computing\Project\EmptyVSCodeProject\build\src\solutions.txt")

plt.figure(figsize=(10, 6))
for i in range(2, min(7, data.shape[0])): 
    plt.plot(data[i], label=f'State {i-2}')

plt.xlabel("x (index number)")
plt.ylabel("y")
plt.title("First 5 solutions")
plt.legend()
plt.grid()
plt.show()
