import constants as c
import copy
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        os.system("del world*.sdf")

        tempSolution = SOLUTION(0)
        tempSolution.Create_World()
        tempSolution.Generate_Body()

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            

    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):

            self.Evolve_For_One_Generation()
        pass
    
    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        

    def Spawn(self):
        
        self.children = {}

        for key in self.parents.keys():

            child = copy.deepcopy(self.parents[key])
            child.Set_ID(self.nextAvailableID)
            self.children[key] = child

            self.nextAvailableID += 1
        

    def Mutate(self):

        for key in self.children.keys():

            self.children[key].Mutate()

    def Select(self):

        for key in self.parents.keys():
            
            if (self.children[key].fitness < self.parents[key].fitness):
                self.parents[key] = self.children[key]

    def Print(self):

        for key in self.parents.keys():

            print(f"\nFitness of parent at key {key}: {self.parents[key].fitness}")
            print(f"Fitness of child at key {key}: {self.children[key].fitness}\n")


    def Show_Best(self):

        bestParent = self.parents[0]

        for i in range(c.populationSize):

            if self.parents[i].fitness > bestParent.fitness:

                bestParent = self.parents[i]
        
        bestParent.Start_Simulation('GUI')

    def Evaluate(self, solutions):

        for i in range(c.populationSize):

            solutions[i].Start_Simulation('DIRECT')

        for i in range(c.populationSize):

            solutions[i].Wait_For_Simulation_To_End()