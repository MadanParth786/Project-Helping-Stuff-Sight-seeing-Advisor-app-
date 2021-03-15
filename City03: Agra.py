#Code for city 03: Agra
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
    print("****Welcome To Agra****")
    print("Top 5 places for Sightseeging in a day are:[0->Agra Fort,1->Taj Mahal,2->Fatehpur Sikari,3->Akbar Tomb,4->Moti Masjid ]")
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
    Data = [ [0,2,37,14,1],
            [2,0,41,16,4],
            [37,41,0,36,38],
            [14,16,36,0,11],
            [1,4,38,11,0]
           ]
    print(hillclimbing(Data))
    print("***Hope you will Enjoy alot***")
    
    
if __name__ == "__main__":
    main()
