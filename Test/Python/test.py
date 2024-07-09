import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
        'Age': [24, 27, 22, 32, 29]}
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(df)

# Create a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
