'''
Implementations for Linear and Binary Search
'''

import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #Remove pass and write the logic to search num in element_list using linear search algorithm
    #Return the total number of guesses made
    guesses = 0

    for n in element_list:
        if n == num:
            print(f"Right answer! It is {num}")
            return guesses
        else:
            guesses += 1
            continue
    print("Try again")

# only for sorted list 
def find_it_binary(num,element_list):
    guesses = 0
    start_idx = 0
    end_idx = len(element_list) - 1
    middle_idx = (end_idx + 1 - start_idx) // 2 + start_idx
    elem_selected = element_list[middle_idx]
    while num != elem_selected:
        guesses += 1
        if elem_selected > num:
            start_idx = start_idx
            end_idx = middle_idx - 1
        elif elem_selected < num:
            start_idx = middle_idx + 1
            end_idx = end_idx
        middle_idx = (end_idx + 1 - start_idx) // 2 + start_idx
        elem_selected = element_list[middle_idx]
    print(f"Right answer! It is {num}.\nYou took {guesses} guesses.")

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]

    # Ascending
    for i in range(1, n+1):
        list_of_elements.append(i)

    # Descending 
    # for i in range(n, 0, -1):
        # list_of_elements.append(i)
    
    # randomizer
    # mid=n//2
    # for j in range(0,n):
    #     index1=random.randrange(0,mid)
    #     index2=random.randrange(mid,n)
    #     num1=list_of_elements[index1]
    #     list_of_elements[index1]=list_of_elements[index2]
    #     list_of_elements[index2]=num1
    return list_of_elements

def play(n):
    nums = initialize_list_of_elements(n)
    number = random.choice(nums)

    print("Linear Search:")
    start = timer()
    no_guesses = find_it_linear(number, nums)
    end = timer()
    print(f"You took {no_guesses} guesses")
    print("Linear search algorithm took {0:.7f} seconds\n".format(end-start))
    
    print("Binary Search:")
    start = timer()
    find_it_binary(number, nums)
    end = timer()
    print(f"Binary search algorithm took {0:.7f} seconds\n".format(end-start))

#Pass different values to play() and observe the output
play(10000)