# Stacks in Python
## Overview
### Attributes
Entity Type: Data Structure

### Notes
(1) Linear Data Structure

(2) Follows Last In, First Out (LIFO) Principle

### Usages
(1) Backtracking & Tracking State...

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