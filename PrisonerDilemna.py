#Code by Andrew DeVoss, viewed by Michael Naguib
import random
import copy
class Delinquent():
    def __init__(self, biteString):
        self.biteString = biteString
        self.choice = biteString[len(biteString) - 1]
        self.characteristics = biteString[:(len(biteString) - 1)]
        self.score = 0
        self.opponentList = []

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
    left = 0
    right = 0
    while right < len(newPop):
        while right < len(newPop) and newPop[right].biteString == newPop[left].biteString:
            right = right + 1
        assignScores(newPop[left:right], newPop)
        left = right


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
        return copy.deepcopy(population)

def assignScores(partialPopulation, population):
    # The last byte in byteString represents the delinquent's decision
    # 1 represents cooperative
    # 0 represents defector
    if len(partialPopulation) == 1:
        # should choose a random member of the whole population other than himself and compare
        delinquent = partialPopulation[0]
        opponent = partialPopulation[0]
        while opponent == partialPopulation[0]:
            opponent = population[random.randint(0, len(population)-1)]
        delDecision = delinquent.biteString[len(delinquent.biteString) - 1]
        opDecision = opponent.biteString[len(opponent.biteString) - 1]
        # delinquent.opponentList.append(opponent.biteString)
        # opponent.opponentList.append(delinquent.biteString)
        if delDecision == 1:
            if opDecision == 1:
                delinquent.score = delinquent.score + 3
            else:
                delinquent.score = delinquent.score + 1
        else:
            if opDecision == 0:
                delinquent.score = delinquent.score + 2
            else:
                delinquent.score = delinquent.score + 4
    else:
        # compares each delinquent to the a random delinquent with the same characteristics
        # (this is the partial population)
        for index in range(0, len(partialPopulation)):
            delinquent = partialPopulation[index]
            delDecision = delinquent.biteString[len(delinquent.biteString) - 1]
            opponent = partialPopulation[0]
            while opponent == partialPopulation[0]:
                opponent = population[random.randint(0, len(population) - 1)]
            opDecision = opponent.biteString[len(opponent.biteString) - 1]
            # delinquent.opponentList.append(opponent.biteString)
            # opponent.opponentList.append(delinquent.biteString)
            if delDecision == 1:
                if opDecision == 1:
                    delinquent.score = delinquent.score + 3
                else:
                    delinquent.score = delinquent.score + 1
            else:
                if opDecision == 0:
                    delinquent.score = delinquent.score + 2
                else:
                    delinquent.score = delinquent.score + 4


def main():
    # used to fix assignScore and test the evolvePop
    """
    population = evolvePopulation(7, 3)
    for delinquent in population:
        print("biteString, score, opponentList: ", delinquent.biteString, delinquent.score, delinquent.opponentList)
    """
    # used to test assignScores (modified so that population is initialized as None)
    """
    population = evolvePopulation(4, 2)
    assignScores(population)
    for i in range(0, len(population)):
        print(population[i], population[i].getScore())
    """
    # used to test mergeSortPop
    """
    population = evolvePopulation(10, 6)
    print(len(population))
    population2 = mergeSortPopulation(population, 6)
    print(len(population2))
    for i in range(0, len(population2)):
        print(population2[i])
    """
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



