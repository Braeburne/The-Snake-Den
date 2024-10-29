# Python Essentials Tour

# 1. Basic Syntax and Data Types
print("## Basic Syntax and Data Types ##")
a = 10          # Integer
b = 3.14        # Float
c = "Hello"     # String
d = True        # Boolean
e = [1, 2, 3]   # List
f = (4, 5, 6)   # Tuple
g = {7, 8, 9}   # Set
h = {'key': 'value'}  # Dictionary

print("Variables:", a, b, c, d, e, f, g, h)
print("Data Types:", type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

# 2. Control Structures
print("\n## Control Structures ##")
for i in range(1, 6):
    print(f"Loop iteration {i}")

condition = True
if condition:
    print("Condition is True")
else:
    print("Condition is False")

# 3. Functions and Modules
print("\n## Functions and Modules ##")
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))

# Importing the math module
import math
print("Square root of 16:", math.sqrt(16))

# 4. File Handling
print("\n## File Handling ##")
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nLine 2.\nLine 3.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# 5. Data Structures
print("\n## Data Structures ##")
# List operations
lst = [5, 3, 8, 6]
lst.sort()
print("Sorted List:", lst)

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print("Squares Dictionary:", squares)

# Set operations
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print("Set Union:", set_a | set_b)
print("Set Intersection:", set_a & set_b)

# 6. Object-Oriented Programming (OOP)
print("\n## Object-Oriented Programming ##")
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

dog = Dog("Buddy")
print(dog.speak())

# 7. Error Handling
print("\n## Error Handling ##")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught an error:", e)
finally:
    print("This runs regardless of an exception.")

# 8. Data Analysis (using Pandas)
print("\n## Data Analysis with Pandas ##")
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'Salary': [50000, 60000, 45000, 70000]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Basic statistics
print("Mean Salary:", df['Salary'].mean())

# 9. Web Requests
print("\n## Web Requests ##")
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Response JSON:", response.json())

# 10. Web Scraping
print("\n## Web Scraping ##")
from bs4 import BeautifulSoup

html_content = "<html><body><h1>Welcome to Web Scraping!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')
print("Scraped Text:", soup.h1.text)

# 11. Simple Visualization (using Matplotlib)
print("\n## Simple Visualization ##")
import matplotlib.pyplot as plt

# Line chart of a sample data
x = [0, 1, 2, 3, 4]
y = [i ** 2 for i in x]
plt.plot(x, y, marker='o')
plt.title("Sample Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.savefig("plot.png")  # Save the plot as an image file
print("Plot saved as 'plot.png'")

# 12. Machine Learning (using scikit-learn)
print("\n## Machine Learning with scikit-learn ##")
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Linear Regression Model
model = LinearRegression()
model.fit(X, y)
predicted = model.predict([[6]])
print("Predicted value for input 6:", predicted[0])

print("\nTour of Python completed!")