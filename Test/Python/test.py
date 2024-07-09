import requests
import matplotlib.pyplot as plt
import numpy as np

# Fetch a random joke from an API
response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()

print(f"Joke: {joke['setup']} - {joke['punchline']}")

# Create a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()