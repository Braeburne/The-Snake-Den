# Python Essentials Tour

def module_1():
    # 1. Basic Syntax and Data Types
    print("## Section 1 | Basic Syntax and Data Types ##")
    a = 10          # Integer
    b = 3.14        # Float
    c = "Hello"     # String
    d = True        # Boolean
    e = [1, 2, 3]   # List
    f = (4, 5, 6)   # Tuple
    g = {7, 8, 9}   # Set
    h = {'key': 'value'}  # Dictionary

    print("Integer:")
    print(f"  Value: {a}")
    print(f"  Type: {type(a)}\n")


    print("Float:")
    print(f"  Value: {b}")
    print(f"  Type: {type(b)}\n")


    print("String:")
    print(f"  Value: '{c}'")
    print(f"  Type: {type(c)}\n")

    print("Boolean:")
    print(f"  Value: {d}")
    print(f"  Type: {type(d)}\n")


    print("List:")
    print(f"  Value: {e}")
    print(f"  Type: {type(e)}\n")


    print("Tuple:")
    print(f"  Value: {f}")
    print(f"  Type: {type(f)}\n")


    print("Set:")
    print(f"  Value: {g}")
    print(f"  Type: {type(g)}\n")

    print("Dictionary:")
    print(f"  Value: {h}")
    print(f"  Type: {type(h)}\n")

    # Store variables in a dictionary for organized printing
    variables = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h}

    # Print variables with values
    print("Variables:")
    for name, value in variables.items():
        print(f" - {name}: {value}")

    # Print variable types
    print("\nData Types:")
    for name, value in variables.items():
        print(f" - {name}: {type(value)}")

    # These two are equivalent to the two for loops above - just less pretty and readable
    # print("Variables:", a, b, c, d, e, f, g, h)
    # print("Data Types:", type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

def module_2():
    # 2. Control Structures
    print("\n## Section 2 | Control Structures ##")

    # 1. Basic For Loop
    print("Basic For Loop:")
    for i in range(1, 6):
        print(f"Loop iteration {i}")

    # 2. While Loop
    print("\nWhile Loop:")
    counter = 1
    while counter <= 5:
        print(f"While loop iteration {counter}")
        counter += 1

    # 3. If-Else Condition
    print("\nIf-Else Condition:")
    condition = True
    if condition:
        print("Condition is True")
    else:
        print("Condition is False")

    # 4. Elif Ladder
    print("\nIf-Elif-Else Ladder:")
    value = 15
    if value < 10:
        print("Value is less than 10")
    elif value < 20:
        print("Value is between 10 and 20")
    else:
        print("Value is 20 or greater")

    # 5. Nested Loops
    print("\nNested Loops:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"i={i}, j={j}")

    # 6. Break and Continue
    print("\nUsing Break and Continue:")
    for i in range(1, 6):
        if i == 3:
            print("Breaking loop at i=3")
            break
        if i == 2:
            print("Continuing at i=2")
            continue
        print(f"Loop iteration {i}")

    # 7. For-Else and While-Else
    print("\nFor-Else Loop:")
    for i in range(1, 4):
        print(f"For loop iteration {i}")
    else:
        print("Loop completed without break")

    print("\nWhile-Else Loop:")
    counter = 1
    while counter < 3:
        print(f"While loop iteration {counter}")
        counter += 1
    else:
        print("While loop completed without break")

    # 8. List Comprehension (With Conditionals)
    print("\nList Comprehension with Conditionals:")
    squares = [x * x for x in range(1, 6) if x % 2 == 0]
    print("Even squares:", squares)

    # 9. Dictionary and Set Comprehension
    print("\nDictionary and Set Comprehension:")
    square_dict = {x: x * x for x in range(1, 6)}
    unique_values = {x % 3 for x in range(1, 10)}
    print("Square Dictionary:", square_dict)
    print("Unique Values Set:", unique_values)

    # 10. Pattern Matching with Match-Case (Python 3.10+)
    print("\nPattern Matching (Match-Case):")
    command = "start"
    match command:
        case "start":
            print("Starting the process.")
        case "stop":
            print("Stopping the process.")
        case "pause":
            print("Pausing the process.")
        case _:
            print("Unknown command")

    # 11. Ternary Conditional (Inline If-Else)
    print("\nTernary Conditional (Inline If-Else):")
    age = 18
    status = "Adult" if age >= 18 else "Minor"
    print("Status based on age:", status)

    # 12. Using Enumerate in Loops
    print("\nUsing Enumerate in Loops:")
    colors = ["red", "blue", "green"]
    for index, color in enumerate(colors, start=1):
        print(f"Color {index}: {color}")

    # 13. Zip in Loops
    print("\nUsing Zip in Loops:")
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 95]
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

    # 14. Try-Except for Flow Control (Handling Exceptions)
    print("\nTry-Except for Flow Control:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught a division by zero error.")
    finally:
        print("This runs regardless of an exception.")

    # 15. Lambda with Conditional Logic
    print("\nLambda with Conditional Logic:")
    is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
    print("5 is:", is_even(5))
    print("8 is:", is_even(8))

def module_3():
    # 3. Functions and Modules
    print("\n## Section 3 | Functions and Modules ##")
    
    # 1. Basic Function Definition and Invocation
    print("\n# 1. Basic Function Definition and Invocation")

    def greet(name):
        return f"Hello, {name}!"

    print(greet("Python"))

    # 2. Function with Positional and Keyword Arguments
    print("\n# 2. Function with Positional and Keyword Arguments")

    def introduce(name, age=30, city="New York"):
        return f"My name is {name}, I am {age} years old, and I live in {city}."

    print(introduce("Alice", age=25, city="Los Angeles"))
    print(introduce("Bob"))  # Uses default values for age and city

    # 3. Function with *args and **kwargs
    print("\n# 3. Function with *args and **kwargs")

    def summarize(*args, **kwargs):
        print("Positional arguments (args):", args)
        print("Keyword arguments (kwargs):", kwargs)

    summarize(1, 2, 3, name="Alice", city="New York")

    # 4. Lambda Functions
    print("\n# 4. Lambda Functions")

    # Lambda for addition
    add = lambda x, y: x + y
    print("Lambda addition (5 + 3):", add(5, 3))

    # Lambda for filtering a list
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers using lambda and filter:", even_numbers)

    # 5. Higher-Order Functions (map, filter, reduce)
    print("\n# 5. Higher-Order Functions (map, filter, reduce)")

    from functools import reduce

    # map example
    squares = list(map(lambda x: x * x, numbers))
    print("Squares using map:", squares)

    # filter example
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print("Odd numbers using filter:", odd_numbers)

    # reduce example
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    print("Sum using reduce:", sum_of_numbers)

    # 6. Decorators
    print("\n# 6. Decorators")

    def uppercase_decorator(func):
        def wrapper(name):
            result = func(name)
            return result.upper()
        return wrapper

    @uppercase_decorator
    def greet_decorated(name):
        return f"Hello, {name}!"

    print(greet_decorated("Alice"))  # Output will be uppercase

    # 7. Recursion
    print("\n# 7. Recursion")

    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n - 1)

    print("Factorial of 5:", factorial(5))

    # 8. Importing and Using Modules
    print("\n# 8. Importing and Using Modules")

    # Using the math module
    import math
    print("Square root of 16 using math module:", math.sqrt(16))
    print("Value of pi:", math.pi)

    # Using the random module
    import random
    print("Random integer between 1 and 10:", random.randint(1, 10))
    print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

    # 9. Custom Module (Demonstration)
    # Create a custom module in the same directory named custom_module.py
    # Content of custom_module.py:
    # def custom_greet(name):
    #     return f"Welcome, {name}, to the custom module!"
    #
    # Importing and using the custom module

    try:
        import custom_module
        print("\n# 9. Using a Custom Module")
        print(custom_module.custom_greet("Python Enthusiast"))
    except ModuleNotFoundError:
        print("Custom module 'custom_module.py' not found. Ensure it is in the same directory.")

    # 10. Docstrings and Annotations
    print("\n# 10. Docstrings and Annotations")

    def multiply(x: int, y: int) -> int:
        """
        Multiplies two numbers and returns the result.

        Parameters:
        x (int): The first number.
        y (int): The second number.

        Returns:
        int: The product of x and y.
        """
        return x * y

    print("Multiply 4 and 5 with annotations:", multiply(4, 5))
    print("Function documentation:", multiply.__doc__)
    print("Function annotations:", multiply.__annotations__)

    # 11. Partial Functions (from functools)
    print("\n# 11. Partial Functions")

    from functools import partial

    def power(base, exponent):
        return base ** exponent

    # Create a square function using partial
    square = partial(power, exponent=2)
    print("Square of 5 using partial:", square(5))

def module_4():
    # 4. Strings in Python
    print("\n## Section 4 | Strings in Python ##")

    # Basic string operations
    text = "   Hello, World! This is a Python string example.   "
    print("Original text:", text)
    print("Uppercase:", text.upper())
    print("Title Case:", text.title())
    print("Replacing text:", text.replace("World", "Python"))
    print("Is the text alphabetic?", text.isalpha())

    # Advanced string operations
    # 1. Stripping Whitespace
    print("Stripped of leading whitespace:", text.lstrip())  # Left strip
    print("Stripped of trailing whitespace:", text.rstrip())  # Right strip
    print("Stripped of all whitespace:", text.strip())  # Strip both ends

    # 2. Finding Substrings
    print("Position of first 'o':", text.find('o'))  # Returns index of first occurrence
    print("Position of last 'o':", text.rfind('o'))  # Returns index of last occurrence
    print("Position of first 'Python':", text.index('Python'))  # Raises ValueError if not found
    print("Position of last 'is':", text.rindex('is'))  # Similar to rfind but raises ValueError if not found

    # 3. Counting Substrings
    print("Count of 'i' in text:", text.count('i'))  # Counts occurrences of substring

    # 4. Starts and Ends Checks
    print("Does text start with 'Hello'? :", text.startswith("Hello"))
    print("Does text end with 'example'? :", text.endswith("example."))

    # 5. Case Manipulation
    print("Swapped case:", text.swapcase())  # Swaps case of each character
    print("Casefolded (for case-insensitive comparisons):", text.casefold())  # More aggressive lowercasing
    print("Capitalized:", text.capitalize())  # Capitalizes the first letter

    # 6. Justifying and Padding
    print("Left justified:", text.ljust(40, '-'))  # Left justify with padding
    print("Right justified:", text.rjust(40, '-'))  # Right justify with padding
    print("Centered:", text.center(40, '-'))  # Center align with padding
    print("Zero-padded number:", "42".zfill(5))  # Pads number with zeros

    # 7. Encoding and Decoding
    encoded_text = text.encode("utf-8")  # Encode to bytes using UTF-8
    print("Encoded text (UTF-8):", encoded_text)
    print("Decoded text (UTF-8):", encoded_text.decode("utf-8"))  # Decode bytes back to string

    # 8. Splitting and Joining
    words = text.split()  # Split by whitespace
    print("Split text into words:", words)
    print("Join words with hyphen:", '-'.join(words))  # Join list of strings with separator

    # Splitting by specific delimiter
    print("Split by 'is':", text.split("is"))

    # Advanced splitting
    lines = "Line1\nLine2\nLine3"
    print("Splitlines:", lines.splitlines())  # Split by lines, keeping newlines

    # 9. Translating and Replacing Characters
    trans_table = str.maketrans("aeiou", "12345")  # Create a translation table
    print("Translated text:", text.translate(trans_table))  # Replace characters according to table

    # Removing specific characters with replace
    print("Text with commas removed:", text.replace(",", ""))  # Remove commas

    # 10. Formatting Strings (without f-strings)
    formatted_text = "This is a {adjective} example.".format(adjective="great")
    print("Formatted text using format():", formatted_text)

    # Named placeholders
    print("Named placeholders:", "{name} is {age} years old.".format(name="Alice", age=30))

    # Number formatting
    print("Formatted number with 2 decimal places: {:.2f}".format(3.14159))

    # 11. Checking Content
    print("Is text alphanumeric?", text.isalnum())  # Checks if all characters are alphanumeric
    print("Is text numeric?", text.isnumeric())  # Checks if all characters are numeric
    print("Is text decimal?", text.isdecimal())  # Checks if all characters are decimal
    print("Is text digit?", text.isdigit())  # Checks if all characters are digits
    print("Is text lowercase?", text.islower())  # Checks if all characters are lowercase
    print("Is text uppercase?", text.isupper())  # Checks if all characters are uppercase
    print("Is text title case?", text.istitle())  # Checks if string is title case
    print("Is text printable?", text.isprintable())  # Checks if all characters are printable
    print("Is text whitespace only?", text.isspace())  # Checks if all characters are whitespace

    # 12. Slicing (Advanced)
    print("First 10 characters:", text[:10])  # Slicing to get the first 10 characters
    print("Last 10 characters:", text[-10:])  # Slicing to get the last 10 characters
    print("Every other character:", text[::2])  # Slicing with step to get every other character
    print("Reversed string:", text[::-1])  # Reverse the entire string

    # 13. Raw Strings (For special characters like backslashes)
    raw_path = r"C:\Users\Alice\Documents"
    print("Raw string (file path):", raw_path)

    # 14. Bytes to String Conversion
    byte_string = b"Hello, Byte World!"
    decoded_string = byte_string.decode("utf-8")  # Decode bytes to string
    print("Decoded string from bytes:", decoded_string)

    # Concatenation and repetition
    greeting = "Hello"
    name = "Alice"
    combined = greeting + ", " + name + "!"
    print("Concatenated String:", combined)
    repeated = greeting * 3
    print("Repeated String:", repeated)

    # f-Strings (Formatted String Literals)
    print("\n## f-Strings (Formatted String Literals) ##")

    age = 30
    height = 5.6

    # Simple f-string with variables
    print(f"{name} is {age} years old and {height} feet tall.")

    # Embedding expressions within f-strings
    x, y = 10, 20
    print(f"The sum of {x} and {y} is {x + y}.")  # Embedded arithmetic expression

    # Formatting numbers within f-strings
    pi = 3.141592653589793
    print(f"Pi to three decimal places is {pi:.3f}")  # Limits pi to 3 decimal places

    # Calling functions within f-strings
    print(f"{name.upper()} is excited to learn more about Python!")  # Calling a method in an f-string

    # Demonstrating multiline f-strings
    multiline = f"""
    Hello, {name}!
    Your age is {age}.
    Pi to 3 decimal places is {pi:.3f}.
    """
    print("Multiline f-string content:\n", multiline)

    # String interpolation with dictionary
    info = {"name": "Charlie", "age": 28}
    print(f"{info['name']} is {info['age']} years old.")

    # Raw f-strings for file paths
    path = r"C:\Users\Alice\Documents"
    print(f"Raw file path: {path}")

    # Function without f-string (using concatenation)
    print("\n## Functions and Modules ##")
    def greet(name):
        return "Hello, " + name + "!"

    print(greet("This is the greet function without f-strings using concatenation."))

    # Function without f-string (using str.format())
    print("\n## Functions and Modules ##")
    def greet(name):
        return "Hello, {}!".format(name)

    print(greet("This is the greet function without f-strings using str.format()."))

    # function with f-string
    print("\n## Functions and Modules ##")
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Python"))

def module_5():
    # 5. Importing the math module
    import math
    print("Square root of 16:", math.sqrt(16))

    print("\n## Module 5. The Math Module in Python ##")

    # 1. Basic Constants
    print("Constants:")
    print("math.pi:", math.pi)  # Pi (π), the ratio of the circumference to the diameter of a circle
    print("math.e:", math.e)    # Euler's number (e), the base of the natural logarithm
    print("math.tau:", math.tau)  # Tau (τ), which is 2π
    print("math.inf:", math.inf)  # Infinity
    print("math.nan:", math.nan)  # Not-a-Number (NaN)

    # 2. Basic Arithmetic Functions
    print("\nBasic Arithmetic Functions:")
    print("math.sqrt(16):", math.sqrt(16))  # Square root
    print("math.pow(2, 3):", math.pow(2, 3))  # Exponentiation (2^3)
    print("math.exp(2):", math.exp(2))  # Exponential function (e^2)
    print("math.fabs(-5.5):", math.fabs(-5.5))  # Absolute value
    print("math.ceil(2.3):", math.ceil(2.3))  # Ceiling function (rounds up)
    print("math.floor(2.7):", math.floor(2.7))  # Floor function (rounds down)
    print("math.trunc(5.7):", math.trunc(5.7))  # Truncates decimal, returning the integer part

    # 3. Logarithmic Functions
    print("\nLogarithmic Functions:")
    print("math.log(10):", math.log(10))  # Natural logarithm (base e)
    print("math.log(100, 10):", math.log(100, 10))  # Logarithm with base 10
    print("math.log2(8):", math.log2(8))  # Base-2 logarithm
    print("math.log10(1000):", math.log10(1000))  # Base-10 logarithm
    print("math.expm1(1):", math.expm1(1))  # e^x - 1 (useful for small x values)

    # 4. Trigonometric Functions
    print("\nTrigonometric Functions:")
    print("math.sin(math.pi / 2):", math.sin(math.pi / 2))  # Sine of π/2 radians
    print("math.cos(0):", math.cos(0))  # Cosine of 0 radians
    print("math.tan(math.pi / 4):", math.tan(math.pi / 4))  # Tangent of π/4 radians
    print("math.asin(1):", math.asin(1))  # Arcsine, returns radians
    print("math.acos(0):", math.acos(0))  # Arccosine, returns radians
    print("math.atan(1):", math.atan(1))  # Arctangent, returns radians
    print("math.atan2(1, 1):", math.atan2(1, 1))  # Arctangent of y/x, considering the quadrant
    print("math.hypot(3, 4):", math.hypot(3, 4))  # Hypotenuse (sqrt(x^2 + y^2))

    # 5. Hyperbolic Functions
    print("\nHyperbolic Functions:")
    print("math.sinh(1):", math.sinh(1))  # Hyperbolic sine
    print("math.cosh(1):", math.cosh(1))  # Hyperbolic cosine
    print("math.tanh(1):", math.tanh(1))  # Hyperbolic tangent
    print("math.asinh(1):", math.asinh(1))  # Inverse hyperbolic sine
    print("math.acosh(2):", math.acosh(2))  # Inverse hyperbolic cosine
    print("math.atanh(0.5):", math.atanh(0.5))  # Inverse hyperbolic tangent

    # 6. Angular Conversion
    print("\nAngular Conversion:")
    print("math.degrees(math.pi):", math.degrees(math.pi))  # Converts radians to degrees
    print("math.radians(180):", math.radians(180))  # Converts degrees to radians

    # 7. Special Functions
    print("\nSpecial Functions:")
    print("math.factorial(5):", math.factorial(5))  # Factorial of 5 (5!)
    print("math.gamma(5):", math.gamma(5))  # Gamma function, extends factorial to real numbers
    print("math.lgamma(5):", math.lgamma(5))  # Logarithmic gamma function

    # 8. Rounding Functions
    print("\nRounding Functions:")
    print("math.ceil(4.2):", math.ceil(4.2))  # Round up to nearest integer
    print("math.floor(4.8):", math.floor(4.8))  # Round down to nearest integer
    print("math.trunc(4.5):", math.trunc(4.5))  # Truncate to integer by removing the decimal part
    print("math.copysign(3, -1):", math.copysign(3, -1))  # Copy the sign of the second argument to the first
    print("math.fmod(5.5, 2):", math.fmod(5.5, 2))  # Modulus that works with floats
    print("math.remainder(5.5, 2):", math.remainder(5.5, 2))  # Returns the IEEE remainder of the division

    # 9. Floating Point Arithmetic Functions
    print("\nFloating Point Arithmetic Functions:")
    print("math.isfinite(1000):", math.isfinite(1000))  # Checks if a number is finite
    print("math.isinf(math.inf):", math.isinf(math.inf))  # Checks if a number is infinite
    print("math.isnan(math.nan):", math.isnan(math.nan))  # Checks if a number is NaN
    print("math.modf(4.5):", math.modf(4.5))  # Splits into fractional and integer parts
    print("math.frexp(8):", math.frexp(8))  # Returns mantissa and exponent of a floating-point number
    print("math.ldexp(0.5, 3):", math.ldexp(0.5, 3))  # Computes x * (2**i) for the given x and i

def module_6():
    # 6. File Handling
    print("\n## Module 6. File Handling ##")
    with open("sample.txt", "w") as file:
        file.write("This is a sample file.\nLine 2.\nLine 3.")

    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)

def module_7():
    # 7. Data Structures
    print("\n## Module 7 | Data Structures ##")

    # 1. List Operations
    print("\n# 1. List Operations")
    lst = [5, 3, 8, 6, 1, 9]

    # Basic list operations
    print("Original List:", lst)
    lst.append(10)
    print("After Append:", lst)
    lst.sort()
    print("Sorted List:", lst)
    lst.reverse()
    print("Reversed List:", lst)

    # Slicing
    print("Slicing first three elements:", lst[:3])
    print("Slicing last three elements:", lst[-3:])
    print("Every other element:", lst[::2])

    # List comprehension
    squares_list = [x * x for x in range(1, 6)]
    print("Squares List using comprehension:", squares_list)

    # Stack operations (LIFO) with list
    print("\nStack Operations (using list):")
    stack = []
    stack.append("a")
    stack.append("b")
    stack.append("c")
    print("Stack after pushes:", stack)
    stack.pop()
    print("Stack after one pop:", stack)

    # Queue operations (FIFO) with list
    print("\nQueue Operations (using list):")
    queue = []
    queue.append("x")
    queue.append("y")
    queue.append("z")
    print("Queue after enqueuing:", queue)
    queue.pop(0)
    print("Queue after dequeuing:", queue)

    # 2. Tuple Operations
    print("\n# 2. Tuple Operations")
    tup = (10, 20, 30, 40, 50)
    print("Original Tuple:", tup)
    print("First element:", tup[0])
    print("Sliced Tuple (first three):", tup[:3])
    print("Count of 20 in tuple:", tup.count(20))
    print("Index of 30 in tuple:", tup.index(30))

    # Named tuples for better readability
    from collections import namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(2, 3)
    print("Named Tuple:", p)
    print("Accessing x:", p.x, "| Accessing y:", p.y)

    # 3. Dictionary Operations
    print("\n# 3. Dictionary Operations")
    dict_a = {"name": "Alice", "age": 25, "city": "New York"}
    print("Original Dictionary:", dict_a)

    # Accessing, adding, and updating elements
    print("Name:", dict_a["name"])
    dict_a["age"] = 26  # Update value
    dict_a["country"] = "USA"  # Add new key-value pair
    print("Updated Dictionary:", dict_a)

    # Dictionary methods
    print("Keys:", list(dict_a.keys()))
    print("Values:", list(dict_a.values()))
    print("Items:", list(dict_a.items()))

    # Dictionary comprehension
    squares_dict = {x: x * x for x in range(1, 6)}
    print("Squares Dictionary using comprehension:", squares_dict)

    # Nested dictionary
    nested_dict = {
        "person1": {"name": "Alice", "age": 30},
        "person2": {"name": "Bob", "age": 25}
    }
    print("Nested Dictionary:", nested_dict)
    print("Accessing nested value (person1's name):", nested_dict["person1"]["name"])

    # 4. Set Operations
    print("\n# 4. Set Operations")
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    # Basic set operations
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Union:", set_a | set_b)
    print("Intersection:", set_a & set_b)
    print("Difference (A - B):", set_a - set_b)
    print("Symmetric Difference:", set_a ^ set_b)

    # Set comprehension
    even_squares = {x * x for x in range(1, 11) if x % 2 == 0}
    print("Even squares using set comprehension:", even_squares)

    # 5. Deque (Double-Ended Queue)
    print("\n# 5. Deque (Double-Ended Queue)")
    from collections import deque

    dq = deque([1, 2, 3])
    print("Original Deque:", dq)
    dq.append(4)  # Append to right
    dq.appendleft(0)  # Append to left
    print("Deque after append operations:", dq)
    dq.pop()  # Remove from right
    dq.popleft()  # Remove from left
    print("Deque after pop operations:", dq)

    # 6. Using Defaultdict for Handling Missing Keys
    print("\n# 6. Defaultdict (Handling Missing Keys)")
    from collections import defaultdict

    dd = defaultdict(lambda: "N/A")  # Default value is "N/A"
    dd["name"] = "Alice"
    print("Name:", dd["name"])
    print("Age (not set):", dd["age"])  # Accessing a non-existing key returns default

    # 7. Using Counter for Frequency Counting
    print("\n# 7. Counter (Frequency Counting)")
    from collections import Counter

    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_count = Counter(words)
    print("Word count:", word_count)
    print("Most common words:", word_count.most_common(2))

    # 8. OrderedDict to Preserve Insertion Order
    print("\n# 8. OrderedDict (Preserves Insertion Order)")
    from collections import OrderedDict

    ordered_dict = OrderedDict()
    ordered_dict["a"] = 1
    ordered_dict["b"] = 2
    ordered_dict["c"] = 3
    print("OrderedDict:", ordered_dict)

    # 9. ChainMap for Merging Dictionaries
    print("\n# 9. ChainMap (Merging Dictionaries)")
    from collections import ChainMap

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = ChainMap(dict1, dict2)
    print("Merged dictionaries with ChainMap:", merged)
    print("Value of 'b':", merged["b"])  # Takes 'b' from the first dictionary in ChainMap

def module_8():
    # 8. Object-Oriented Programming (OOP)
    print("\n## Module 8 | Object-Oriented Programming (OOP) ##")

    # 1. Basic Class and Inheritance
    print("\n# 1. Basic Class and Inheritance")
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return f"{self.name} makes a sound."

    class Dog(Animal):  # Inheriting from Animal
        def speak(self):  # Overriding the speak method
            return f"{self.name} barks."

    dog = Dog("Buddy")
    print(dog.speak())  # Output: Buddy barks

    # 2. Encapsulation and Properties
    print("\n# 2. Encapsulation and Properties")

    class Person:
        def __init__(self, name, age):
            self._name = name  # Protected attribute
            self.__age = age   # Private attribute

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            if age >= 0:
                self.__age = age
            else:
                print("Age cannot be negative.")

    person = Person("Alice", 30)
    print(f"Name: {person._name}, Age: {person.age}")
    person.age = 35
    print(f"Updated Age: {person.age}")

    # 3. Polymorphism
    print("\n# 3. Polymorphism")

    class Cat(Animal):
        def speak(self):
            return f"{self.name} meows."

    animals = [Dog("Buddy"), Cat("Whiskers"), Animal("Generic Animal")]

    for animal in animals:
        print(animal.speak())  # Calls the overridden method based on the object type

    # 4. Abstraction
    print("\n# 4. Abstraction")

    from abc import ABC, abstractmethod

    class Vehicle(ABC):
        @abstractmethod
        def start(self):
            pass

    class Car(Vehicle):
        def start(self):
            return "The car starts with a key."

    class Bike(Vehicle):
        def start(self):
            return "The bike starts with a button."

    car = Car()
    bike = Bike()
    print(car.start())
    print(bike.start())

    # 5. Special Methods (__str__ and __repr__)
    print("\n# 5. Special Methods (__str__ and __repr__)")

    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            return f"'{self.title}' by {self.author}"

        def __repr__(self):
            return f"Book(title='{self.title}', author='{self.author}')"

    book = Book("1984", "George Orwell")
    print("Using __str__:", book)        # Calls __str__
    print("Using __repr__:", repr(book))  # Calls __repr__

    # 6. Class and Static Methods
    print("\n# 6. Class and Static Methods")

    class MathOperations:
        count = 0

        def __init__(self):
            MathOperations.count += 1

        @classmethod
        def get_instance_count(cls):
            return f"Number of instances created: {cls.count}"

        @staticmethod
        def add(x, y):
            return x + y

    math1 = MathOperations()
    math2 = MathOperations()
    print(MathOperations.get_instance_count())
    print("Static method add(5, 3):", MathOperations.add(5, 3))

    # 7. Using super() to Access Parent Class
    print("\n# 7. Using super() to Access Parent Class")

    class Bird(Animal):
        def __init__(self, name, color):
            super().__init__(name)  # Call the parent class's __init__
            self.color = color

        def describe(self):
            return f"{self.name} is a {self.color} bird."

    parrot = Bird("Polly", "green")
    print(parrot.describe())
    print(parrot.speak())  # Inherited method from Animal

    # 8. Multiple Inheritance
    print("\n# 8. Multiple Inheritance")

    class Flyable:
        def fly(self):
            return "This object can fly."

    class FlyingBird(Bird, Flyable):  # Multiple inheritance
        pass

    flying_bird = FlyingBird("Eagle", "brown")
    print(flying_bird.describe())
    print(flying_bird.fly())

    # 9. Object Introspection
    print("\n# 9. Object Introspection")

    print("Is parrot an instance of Bird?", isinstance(parrot, Bird))
    print("Does parrot have attribute 'color'?", hasattr(parrot, 'color'))
    print("Attributes of parrot:", dir(parrot))

def module_9():
    # 9. Error Handling
    print("\n## Module 9 | Error Handling ##")

    # Basic try-except-finally
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught a ZeroDivisionError:", e)
    finally:
        print("This runs regardless of an exception.\n")

    # Handling Multiple Exception Types
    print("Handling Multiple Exception Types:")
    try:
        num = int("not_a_number")
    except ValueError as e:
        print("Caught a ValueError:", e)
    except TypeError as e:
        print("Caught a TypeError:", e)

    # Using Else with try-except-finally
    print("\nUsing Else in try-except-finally:")
    try:
        result = 10 / 2
    except ZeroDivisionError as e:
        print("Caught a ZeroDivisionError:", e)
    else:
        print("No exception occurred, result is:", result)
    finally:
        print("This block always runs.\n")

    # Custom Error Messages and Logging
    print("Custom Error Messages:")
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError as e:
        print("Custom error message:", e)
    else:
        print("Valid age entered:", age)

    # Raising Custom Exceptions
    print("\nRaising Custom Exceptions:")
    class CustomError(Exception):
        """A custom exception for demonstration purposes."""
        pass

    try:
        raise CustomError("This is a custom error.")
    except CustomError as e:
        print("Caught a CustomError:", e)

    # Nested try-except Blocks
    print("\nNested try-except Blocks:")
    try:
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("Inner try-except: Division by zero caught.")
            raise ValueError("Re-raising as ValueError.")
    except ValueError as e:
        print("Outer try-except caught:", e)

    # Using assert for Error Checking
    print("\nUsing assert for Error Checking:")
    try:
        x = -1
        assert x >= 0, "x must be non-negative"
    except AssertionError as e:
        print("AssertionError:", e)

    # Cleanup Code with try-finally
    print("\nCleanup Code with try-finally:")
    file = None
    try:
        file = open("example.txt", "w")
        file.write("Writing to the file.")
        print("File written successfully.")
    finally:
        if file:
            file.close()
            print("File closed in finally block.")

def module_10():
    # 10. Data Analysis (using Pandas)
    print("\n## Data Analysis with Pandas ##")
    import pandas as pd

    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [24, 27, 22, 32],
            'Salary': [50000, 60000, 45000, 70000]}
    df = pd.DataFrame(data)
    print("DataFrame:\n", df)

    # Basic statistics
    print("Mean Salary:", df['Salary'].mean())

def module_11():
    # 11. Web Requests
    print("\n## Web Requests ##")
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Response JSON:", response.json())

def module_12():
    # 12. Web Scraping
    print("\n## Web Scraping ##")
    from bs4 import BeautifulSoup

    html_content = "<html><body><h1>Welcome to Web Scraping!</h1></body></html>"
    soup = BeautifulSoup(html_content, 'html.parser')
    print("Scraped Text:", soup.h1.text)

def module_13():
    # 13. Simple Visualization (using Matplotlib)
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

def module_14():
    # 14. Machine Learning (using scikit-learn)
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

def run_modules(x, y):
    for i in range(x, y+1):
        func_name = f"module_{i}"  # Construct function name as a string
        func = globals().get(func_name)  # Get the function from the global scope
        if func:  # Check if the function exists
            func()  # Call the function
        else:
            print(f"Function {func_name} does not exist.")

print("## Base Libraries Python Section ##")

run_modules(1, 2)

# run_modules(1, 9)

# print("## Custom Libraries Python Section ##")

# run_modules(10, 14)