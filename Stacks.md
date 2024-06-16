# 💵Stacks in Python
## Overview
### Attributes
Entity Type: Data Structure

### Notes
(1) Linear Data Structure

(2) Follows Last In, First Out (LIFO) Principle

### Usages
(1) **Backtracking & Tracking State**
- *Functional Use:* Storing previous states to backtrack through choices.
- *Applications:* Solving puzzles (like Sudoku or N-Queens problem), pathfinding algorithms.
- *Real-World Examples:* Puzzle-solving algorithms in games like Sudoku solvers, AI decision-making in chess engines (e.g., Stockfish).

(2) **Recursive Function Calls**
- *Functional Use:* Storing function call contexts and local variables.
- *Applications:* Recursive algorithms such as factorial calculation, tree traversal.
- *Real-World Examples:* Compiler implementations (e.g., handling function calls and variable scopes in programming languages like Python, Java).

(3) **Expression Evaluation and Syntax Parsing**
- *Functional Use:* Evaluating mathematical expressions, parsing languages.
- *Applications:* Arithmetic operations (e.g., infix to postfix conversion), parsing JSON/XML data.
- *Real-World Examples:* Programming language interpreters and compilers (e.g., Python interpreter, C++ compiler).

(4) **Depth-First Search (DFS)**
- *Functional Use:* Traversing graphs or trees depth-wise.
- *Applications:* Finding connected components, cycle detection in graphs.
- *Real-World Examples:* Maze solving algorithms, network routing algorithms.

(5) **Undo Mechanisms in Editors**
- *Functional Use:* Storing previous states of documents or actions.
- *Applications:* Storing previous states of documents or actions.
- *Real-World Examples:* Text editors like Sublime Text or VSCode, IDEs like Visual Studio.

(6) **Function Call Stack in Programming**
- *Functional Use:* Managing function calls and local variables during program execution.
- *Applications:* Handling nested function calls, managing memory in recursive algorithms.
- *Real-World Examples:* Operating systems for managing process execution (e.g., Linux kernel), web browsers for managing web page rendering and execution contexts.

(7) **Browser History Management**
- *Functional Use:* Storing previously visited URLs to facilitate backward navigation.
- *Applications:* Navigating through visited web pages, implementing the back button functionality.
- *Real-World Examples:* Web browsers like Chrome, Firefox, Safari.

(8) **Call Stack in Operating Systems**
- *Functional Use:* Managing system resources and function calls in kernel mode.
- *Applications:* Handling interrupts, managing system calls.
- *Real-World Examples:* Operating systems like Linux, Windows, macOS.

(9) **Task Management in Operating Systems**
- *Functional Use:* Managing tasks and processes in a multitasking environment.
- *Applications:* Process scheduling, handling task priorities.
- *Real-World Examples:* Task managers in operating systems (e.g., Task Manager in Windows, Activity Monitor in macOS).

(10) **Postfix Evaluation in Calculators**
- *Functional Use:* Evaluating mathematical expressions in postfix notation.
- *Applications:* Performing arithmetic operations (e.g., addition, multiplication) based on user input.
- *Real-World Examples:* Scientific calculators, programming calculators.

(11) **Transaction Management in Databases**
- *Functional Use:* Managing operations that can be rolled back in case of failure.
- *Applications:* Committing changes to a database, rolling back transactions.
- *Real-World Examples:* Database management systems (e.g., PostgreSQL, MySQL).

(12) **Component Rendering in GUI Systems**
- *Functional Use:* Storing the hierarchy of components to render in a GUI.
- *Applications:* Drawing components (e.g., buttons, menus) in a windowing system.
- *Real-World Examples:* Graphical user interfaces (e.g., Qt framework, GTK+).

### Performance
The operations append() and pop() on a list in Python are both O(1) on average, making stacks efficient for most applications.

## Initialization
Stacks are implemented as lists in Python. An empty stack can be initialized like this:
```python
stack = []
```
## Operations
### Notes
The stack data structure operations are known colloqiually as the following across most programming languages:

(1) Push - usually called "push" because one would push things onto the stack if they wanted to put something on the stack. The method is implemented as "append" in Python via the list data structure. This is our "add."

 (2) Pop - Simply undoes a push operation. Think of the example of "popping" a Pringles chip of a a Pringles can. You're popping a chip from the stack of other Pringles chips. The method is implemented as "pop" in Python via the list data structure. This is our "remove."

(3) Peek - lets us take a peek at the top of the stack, without committing to changing it. The list data structure doesn't have a defined peek method. Typically, we implement the logic for it as below.

(4) Empty - Checks if the stack is empty. Also no defined method for this in the Python list data structure. Typically implemented as below.

Let's explore these implementations in Python.

### Push
```python
stack.append(item)
```

### Pop
```python
item = stack.pop()
```

### Peek
```python
peek = stack[-1]
```

### Empty
```python
if not stack:
    # stack is empty
```

## Examples

### Sample 1 - Input
```python
stack = []

stack.append(1)    # push 1
stack.append(2)    # push 2
stack.append(3)    # push 3

top = stack.pop()  # pop 3 (last in)
print(top)         # prints 3

top = stack.pop()  # pop 2
print(top)         # prints 2

peek = stack[-1]   # peek at top element, which is 1
print(peek)        # prints 1
```

### Sample 1 - Output
```
3
2
1
```

### Sample 2 - Input
```python
def CheckFruitBasket():
    for fruit in fruit_basket:
        print(fruit)

def isFruitBasketEmpty():
    if not fruit_basket:
        print("fruit basket is empty.")

fruit_basket = []

print("loading fruit basket...")
fruit_basket.append("apple")       # push an apple
fruit_basket.append("banana")      # push a banana
fruit_basket.append("pear")        # push a pear
CheckFruitBasket()
isFruitBasketEmpty()

print("\npeeking at the top of the fruit basket...")
peek = fruit_basket[-1]
print(peek)

print("\nremoving pear...")
fruit_basket.pop()
CheckFruitBasket()
isFruitBasketEmpty()

print("\npeeking at the top of the fruit basket...")
peek = fruit_basket[-1]
print(peek)

print("\nremoving banana...")
fruit_basket.pop()
CheckFruitBasket()
isFruitBasketEmpty()

print("\npeeking at the top of the fruit basket...")
peek = fruit_basket[-1]
print(peek)

print("\nremoving apple...")
fruit_basket.pop()
CheckFruitBasket()

print("\nchecking if fruit basket is empty...")
isFruitBasketEmpty()
```

### Sample 2 - Output
```
loading fruit basket...
apple
banana
pear

peeking at the top of the fruit basket...
pear

removing pear...
apple
banana

peeking at the top of the fruit basket...
banana

removing banana...
apple

peeking at the top of the fruit basket...
apple

removing apple...

checking if fruit basket is empty...
fruit basket is empty.
```