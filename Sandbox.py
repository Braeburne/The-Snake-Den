fruit_basket = []

def CheckFruitBasket():
    for fruit in fruit_basket:
        print(fruit)

def isFruitBasketEmpty():
    if not fruit_basket:
        print("Fruit basket is empty.")

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