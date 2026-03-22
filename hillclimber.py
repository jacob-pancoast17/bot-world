import constants as c
import copy
from solution import SOLUTION

class HILL_CLIMBER:

    def __init__(self):

        self.parent = SOLUTION()

    def Evolve(self):

        self.parent.Evaluate('DIRECT')

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):

        self.child.Mutate()

    def Select(self):

        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def Print(self):

        print()
        print(f"Parent's fitness: {self.parent.fitness} | Child's fitness: {self.child.fitness}")
        print()

    def Show_Best(self):

        self.parent.Evaluate('GUI')