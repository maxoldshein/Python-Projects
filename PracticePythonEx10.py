import random

def listOverlapComprehension():
    common = []
    #list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list1 = random.sample(range(20), 10)
    list2 = random.sample(range(20), 8)
    
    common = [x for x in list1 for y in list2 if  (x== y  and not(x in common))]
    
    print("The first list is: " + str(list1))
    print("The second list is: " + str(list2))
    print("The common elements between them are: " + str(sorted(common)))
    
listOverlapComprehension()
