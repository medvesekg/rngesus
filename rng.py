import random
import re

def rng(length, low = 10, high = 99):
    random_number = random.randint(low, high)
    
    if length <= 0:
        return random_numbers
    
    elif random_number in random_numbers:
        return rng(length, low, high)
    
    else:
        random_numbers.append(random_number)
        
       
        return rng(length - 1, low, high)
    

###############################################################

    
print "Welcome to the random number generator. Simply enter how many random numbers you would like to generate and the program will generate them for you. Optionally you can also enter a range in which you would like the numbers to be generated e.g. '5 1-1000', by default this is 10 to 99. To exit please type 'exit'."

while True:
    random_numbers = []

    userInput = raw_input("How many random numbers do you want?: ")
    
    if "exit" in userInput.lower():
        break

    userNumbers = re.findall('\d+', userInput)

    if len(userNumbers) >= 3:
        print rng(int(userNumbers[0]), int(userNumbers[1]), int(userNumbers[2]))
    else:
        print rng(int(userNumbers[0]))

print "Bye bye"