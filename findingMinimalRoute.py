portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 1, 2, 3, 4]

def permutations(route, ports):
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    global smallest
    global bestroute
    for i in ports:
        route.append(i)
        if len(route) == len(portnames):
            if (set(route) == set(range(5))):
                distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                
                emissions = distance * co2
                if emissions < smallest:
                    smallest = emissions
                    bestroute = route
        else:
            permutations(route, [x for x in ports if x != i])
        route.pop()
    pass

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))
    
    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
