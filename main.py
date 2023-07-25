#Heads or Tails

import random
import time

print("This program is a random coin toss.")
time.sleep(2)
print("You will get heads or tails in 5 seconds")
time.sleep(1)
print("You will get heads or tails in 4 seconds")
time.sleep(1)
print("You will get heads or tails in 3 seconds")
time.sleep(1)
print("You will get heads or tails in 2 seconds")
time.sleep(1)
print("You will get heads or tails in 1 seconds")
time.sleep(1)
random_number = random.randint(0,1)
if random_number == 0:
    print("Heads.")
else:
    print("Tails.")
