def listConditional():
    numberList = [0, 5, 10, 15, 20, 25, 30, 35,  40, 45, 50]
    qualifyingList = []
    userQualifyingList = []

    print("The list is: ")
    print numberList
    print(100 * "-")
    
    for number in numberList:
        if (number <= 40):
            qualifyingList.append(number)
    print("Example:")
    print("The elements of the list that are less than or equal to 40 are: ")
    print qualifyingList

    print(100 * "-")
    
    boundary = input("Please enter a number that you would like to filter the list with: ")
    boundaryString = str(boundary)

    for number2 in numberList:
        if (number2 <= boundary):
            userQualifyingList.append(number2)

    print("The elements of the list that are less than " + boundaryString + " are: ")
    print(userQualifyingList)

    print(100 * "-")
    
listConditional()
