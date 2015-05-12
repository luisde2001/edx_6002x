import random
def sampleQuizzes():
    score = 0.0
    for i in range(10000):
        midTerm1 = random.randrange(50,81)
        midTerm2 = random.randrange(60,91)
        finalExam = random.randrange(55,96)
        grade = midTerm1*0.25 + midTerm2*0.25 + finalExam*0.50
        if grade >= 70 and grade <= 75:
            score += 1.0

    return score/10000

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """

def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores,bins = 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()


print sampleQuizzes()