import random
import pylab


def LVMethod():
    
    numTries = 1000
    balls = ["w", "b"]
    total_tries = [0] * numTries
    #total_flips = [0] * numTries
    
    for trial in range (numTries):
        ball = "b"
        tries = 0
        #total_flips[trial] = trial        
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

def MCMethod():
    
    numTries = 1000
    balls = ["w", "b"]
    total_tries = [0] * numTries
    #total_flips = [0] * numTries
    
    for trial in range (numTries):
        ball = "b"
        tries = 0
        #total_flips[trial] = trial        
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
    


MCMethod()
