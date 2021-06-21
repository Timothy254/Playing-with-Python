import random

# a function to create a list where range is the largest number in the list
def list_range(r):
    #int(range)
    list = []
    r=pp
    for i in range(r):
        list.append(i)
        if i != r-1:
            continue
    return list


# a function that will do the main task to randomise and return a number from your range
def randomise(list):
    print("Your random value from the given range is ",random.choice(list))


print("Hello! \n This program will randomise and return a value between 0 and the given range of your choice.\n")
pp=input("What your desired range?\n")
list=list_range(pp)
randomise(list)