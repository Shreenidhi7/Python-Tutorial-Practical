import random

# random() -> returns random float between 0.0 and 1.0(excluded)
print("Random Function")
print(random.random())

# randint(a, b) -> returns random integer value between a and b (both included)
print(f"\nRandInt Function")
print(random.randint(0,10))

# choice(sequence) -> returns a random item from the sequence
print(f"\nChoice Function")
nums = [10, 3, 7, 2, 6, 1, 0]
print(random.choice(nums))
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

# shuffle(sequence) -> returns the elements shuffled in random order
print(f"\nShuffle Function")
fruitsAgain = ['mango','pineapple','mango', 'strawberry']
random.shuffle(fruitsAgain)
print(fruitsAgain)