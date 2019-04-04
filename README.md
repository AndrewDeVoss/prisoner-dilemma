# prisoner-dilemma
Testing the effect of dividing a population on the sustainability of cooperators in the prisoner's dilemma scenario.

## ```PrisonerDilemma.py``` 
- description: the main entry point of the code
### Class: ```Delinquent```
- description: each delinquent is a person that will either cooperate or defect determined by the last character in the
in the ```biteString```. The rest of the ```biteString``` determines the characteristics of the individual and this
will be used to divide the population into subgroups.
- Constructor: ```__init__(self,biteString)``` creates a new instance of the class where ```biteString``` is a list of 1's and 0's example ```[0,1,1,1,0]```
- Method: ```getBiteString(self)``` is a getter method for  ```biteString``` ... returns this value
- Method: ```getCharacteristics(self)``` is a getter method for  ```characteristics``` ... returns this value
- Method: ```getScore(self)``` is a getter method for  ```score``` ... returns this value
- to String: ```__str__(self)``` returns the ```bitString``` list as a string ex: ```__str__() #>>> '[0,1,1,1,0]'```
- greater than: ```__gt__(self,otherDelinquent)``` where ```otherDelinquent``` is an instance of the ```Delinquent``` class; returns ```True``` if the caller instance
represents a greater binary number in its ```self.characteristics``` comparativly and ```False```  otherwise;

### Global Methods:
- ```makeBiteString(length)```: returns a list of 1's and 0's of length ```length```
- ```mergeSortPopulation(population,numCharacteristics)```: takes an input list of delinquent instances ```population``` 
and returns a new list sorted from greatest to least by comparing each delinquent's ```self.bitString```;
```numCharacteristics``` is the integer length of the ```bitString```;  (sorting done by mergesort)
