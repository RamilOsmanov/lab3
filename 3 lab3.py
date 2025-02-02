def solve(numheads, numlegs):
    #solve syst of eq
     y = (numlegs - 2 * numheads) // 2  
     x = numheads - y
     return x,y
   
   
   


numheads=int(input())
numlegs=int(input())
chickens, rabbits = solve(numheads, numlegs)

print("Chickens : ", chickens,", Rabbits : ",rabbits)