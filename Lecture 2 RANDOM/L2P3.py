import random
def deterministicNumber():
    random.seed(0) # This will be discussed in the video "Drunken Simulations"
    return random.randrange(10,21,2)
print deterministicNumber()