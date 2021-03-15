#Code for City 04: Chandigarh
import random
def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []
    for i in range (len(tsp)):
        randomCity = cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
        
        
    return solution

def routeLen(tsp,solution):
    routelen =0
    for i in range(len(solution)):
        routelen += tsp[solution[i-1]] [solution[i]]
        
    return routelen  
    

def getneibours(solution):
    neibours =[]
    length =[]
    for i in range (len(solution)):
        for j in range (i+1,len(solution)):
            neibour = solution.copy()
            neibour[i] = solution[j]
            neibour[j] =solution[i]
            neibours.append(neibour)
            
    return neibours      
        

def getsoln(tsp,neibours):
    bestlen =routeLen(tsp,neibours[0])
    bestsoln = neibours[0]
    for neibour in neibours:
        
        currentroutelen =routeLen(tsp,neibour)
        if currentroutelen <bestlen:
            
            bestlen = currentroutelen
            bestsoln =neibour
                
    return bestsoln,bestlen    
    
    
    
    

def hillclimbing(tsp):
    print("****Welcome To Chandigarh****")
    print("Top 5 places for Sightseeging in a day are:[0->Rose garden,1->Rock Garden,2->Sukhna Lake ,3->Fun City,4->Chandigarh Museum ]")
    print("Current Optimal(Random) Solution: ")
    currentsoln = randomSolution(tsp)
    print(currentsoln)
    currentroutelen =routeLen(tsp,currentsoln)
    print("Total Distance:")
    print(currentroutelen)
    neibour =getneibours(currentsoln)
    print("All possible Ways for Sightseeing are: ")
    print(neibour)
    bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
    while bestsolutionlen <currentroutelen:
        currentsoln = bestsolution
        currentroutelen = bestsolutionlen
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
        print("Best Optimal Order for Sightseeing is:")
    return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
def main():
    Data = [ [0,5,6,8,3],
            [5,0,6,8,2],
            [6,6,0,7,3],
            [8,8,7,0,7],
            [3,2,3,7,0]
           ]
    print(hillclimbing(Data))
    print("***Hope you will Enjoy alot***")
    
    
if __name__ == "__main__":
    main()
