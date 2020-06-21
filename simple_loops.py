
candylist = ["Snickers", "Kit Kat", "Sour Patch Kids", "Skittles"]
for candy in range(len(candylist)):
    print("[" + str(int(candy)+1) + "] " + candylist[candy])

index = 3
candycart=[]

while index >0:
    candy_choice= int(input('What kind of candy would you like? '))
    #validate the choice of candy. limits type of inputs and test for bad data
    while (candy_choice <0 or (candy_choice > len(candylist)-1)):
        print('ERROR')
        candy_choice= int(input('What kind of candy would you like? '))
    
    candycart.append(candylist[candy_choice])
    index -= 1
for candy in candycart:
    print(candy)

