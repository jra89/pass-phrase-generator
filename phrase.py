import random
import re

file = open('1-1000.txt', 'r')

arr = []
for line in file:
    regex = re.compile('[^a-zA-Z]')
    if len(line.strip()) <= 6 and len(line.strip()) >= 3:
        arr.append(regex.sub('', line.strip().lower()))

output = open('phrases.txt', 'a')
secure_random = random.SystemRandom()

for x in range(1000):
    wordOne = secure_random.choice(arr)
    wordTwo = secure_random.choice(arr)
    wordThree = secure_random.choice(arr)
    phrase = wordOne + '-' + wordTwo + '-' + wordThree
    output.write(phrase + "\n")
output.close()

