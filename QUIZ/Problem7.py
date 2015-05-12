import random
import pylab

def LVMethod():
    
    numTries = 1000
    balls = ["w", "b"]
    
    total_tries = [0] * numTries
    
    
    for trial in range (numTries):
        ball = "b"
        tries = 0
        while ball != "w":
            tries += 1
            ball = random.choice(balls)
        total_tries[tries] += 1
    
    pylab.plot(total_tries)
    pylab.title("LV Method")
    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.legend(loc = 1)
    pylab.show()
    
    

'''
def noReplacementSimulation(numTrials):
    true = 0
    for n in range(numTrials):
        if draw():
            true += 1
    return float(true)/float(numTrials)
'''

LVMethod()
