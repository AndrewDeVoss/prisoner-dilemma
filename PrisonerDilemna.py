#Code by Andrew DeVoss, viewed by Michael Naguib
import random
class Delinquent():
    def __init__(self, biteString):
        self.biteString = biteString
        self.choice = biteString[len(biteString) - 1]
        self.characteristics = biteString[:(len(biteString) - 1)]
        self.score = None
    def getBiteString(self):
        return self.biteString
    def getChoice(self):
        return self.choice
    def getCharacteristics(self):
        return self.characteristics
    def getScore(self):
        return self.score
    def __str__(self):
        return str(self.biteString)
    def __gt__(self, otherDelinquent):
        equal = True
        greaterThan = True
        index = 0
        while equal and (index < len(self.characteristics)):
            if self.characteristics[index] == otherDelinquent.characteristics[index]:
                index = index + 1
            elif self.characteristics[index] > otherDelinquent.characteristics[index]:
                equal = False
            else:
                greaterThan = False
                equal = False
        return greaterThan


def makeBiteString(length):
    bs = []
    for i in range(0, length):
        bs.append(random.randint(0,1))
    return bs

def evolvePopulation(desiredPopulationSize, lenBiteString, population=None):
    if population is None:
        population = []
    delinquentsNeeded = desiredPopulationSize - len(population)
    for newDelinquent in range(0, delinquentsNeeded):
        x = Delinquent(makeBiteString(lenBiteString))
        population.append(x)
    newPop = mergeSortPopulation(population, lenBiteString)

    return newPop

def mergeSortPopulation(population, numCharacteristics):
    sortedPop = []*len(population)
    if len(population) > 1:
        mid = len(population)//2
        left = mergeSortPopulation(population[:mid], numCharacteristics)
        right = mergeSortPopulation(population[mid:], numCharacteristics)
        # merge the two halves
        lcounter = 0
        rcounter = 0
        while lcounter < len(left) and rcounter < len(right):
            if left[lcounter] > right[rcounter]:
                sortedPop.append(left[lcounter])
                lcounter = lcounter + 1
            else:
                sortedPop.append(right[rcounter])
                rcounter = rcounter + 1
        while lcounter < len(left):
            sortedPop.append(left[lcounter])
            lcounter = lcounter + 1
        while rcounter < len(right):
            sortedPop.append(right[rcounter])
            rcounter = rcounter + 1

        return sortedPop
    else:
        return population

def main():
    # used to test mergeSortPop
    population = evolvePopulation(10, 6)
    print(len(population))
    population2 = mergeSortPopulation(population, 6)
    print(len(population2))
    for i in range(0, len(population2)):
        print(population2[i])

    # used to test greater than method
    """
    x = Delinquent(makeBiteString(6))
    y = Delinquent(makeBiteString(6))
    print(x.characteristics)
    print(y.characteristics)
    print(x>y)
    """
    # used to test evolvePopulation method
    """
    population = evolvePopulation(1, 4)
    print(population)
    print(population[0].getBiteString())
    print(population[0].getChoice())
    print(population[0].getCharacteristics())
    """
main()



