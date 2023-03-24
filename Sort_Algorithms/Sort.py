'''
Swapping
'''
def swap(num_list, first_index, second_index):
    first = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = first
    return num_list


#Pass different values to the function and test your program
num_list=[2,3,89,45,67]
# print("List before swapping:",num_list)
# swap(num_list, 1, 2)
# print("List after swapping:",num_list)

'''
Selection Sort
'''
# EXERCISE 1
def find_next_min(num_list,start_index):
    min = num_list[start_index]
    min_index = start_index
    for i in range(start_index, len(num_list)):
        if num_list[i] < min:
            min = num_list[i]
            min_index = i
        else:
            continue
    return min_index

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=1
# print("Index of the next minimum element is", find_next_min(num_list,start_index))

# EXERCISE 2
def swap(num_list, first_index, second_index):
    first = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = first
    return num_list

def find_next_min(num_list,start_index):
    min = num_list[start_index]
    min_index = start_index
    for i in range(start_index, len(num_list)):
        if num_list[i] < min:
            min = num_list[i]
            min_index = i
        else:
            continue
    return min_index

def selection_sort(num_list):
    no_of_passes = 0
    for i in range(len(num_list)):
        no_of_passes += 1
        next_min_index = find_next_min(num_list, i)
        swap(num_list, i, next_min_index)
    # return num_list
    return no_of_passes

#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
# print("Before sorting;",num_list)
# selection_sort(num_list)
# print("After sorting:",num_list)

'''
Bubble Sort
'''
def swap(num_list, first_index, second_index):
    global no_of_swaps
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
    no_of_swaps+=1

def bubble_sort(num_list):
    # global no_of_passes
    no_of_passes = 0

    # because we are alwauys comparing a pair, so the max number of times we need to compare is no. of elements-1
    for i in range(len(num_list)-1): 
        swapped = False
        no_of_passes += 1
        
        # seems like there is no diff for -1 or -i-1
        for k in range(len(num_list)-1):
            if num_list[k] > num_list[k+1]:
                swap(num_list, k, k+1)
                swapped = True

        if swapped == False:
            break
    
    # print("At the end of pass-",no_of_passes,":",num_list)
    return no_of_passes

no_of_swaps=0
no_of_passes=0
num_list=[5,4,3,2,1]
# print("In the beginning:",num_list)
# print("______________________________________________")
# bubble_sort(num_list)
# print("______________________________________________")
# print("At the end:",num_list)
# print("______________________________________________")
# print("No. of swaps:", no_of_swaps)
# print("No. of passes:",no_of_passes)

'''
Exercise on Selection & Bubble Sort - Level 1
'''
num_list=[8,2,19,34,23, 67, 91]
#num_list=[91,8,19,23,34,67,2]
# print("Selection Sort - No. of passes:",selection_sort(num_list))

num_list=[8,2,19,34,23, 67, 91]
#num_list=[91,8,19,23,34,67,2]  
# print("Bubble Sort - No. of passes:",bubble_sort(num_list))

'''
Merge Sort
'''
def merge(left_list, right_list):
    sorted = []
    i = 0 # left
    j = 0 # right
    while (i < len(left_list) and j < len(right_list)):
        if left_list[i] <= right_list[j]:
            # right element bigger, append left element
            sorted.append(left_list[i])
            i += 1 # move to next element in the left list
        else:
            # left element bigger, append right element
            sorted.append(right_list[j])
            j += 1 # move to next element in the right list
    
    # If there are any elements left in left_list, append it to sorted_list
    if i < len(left_list):
        for i in range(i, len(left_list)):
            sorted.append(left_list[i])
    
    # If there are any elements left in right_list, append it to sorted_list
    if j < len(right_list):
        for j in range(j, len(right_list)):
            sorted.append(right_list[j])
    return sorted

def merge_sort(num_list):
    low = 0
    high = 0
    if len(num_list) == 1:
        high = 0
    elif len(num_list) > 1:
        high = len(num_list) - 1

    if low == high: # only 1 item
        return num_list
    else:
        # middle = (high+low) // 2 + 1
        middle = len(num_list) // 2
        left_list = num_list[:middle]
        right_list = num_list[middle:]

        # will keep dividing list until list becomes individual elements
        listL = merge_sort(left_list)
        listR = merge_sort(right_list)

        # recursively merge lists, starting from the smallest unit
        sorted = merge(listL, listR)
        return sorted

num_list=[45, 2, 51, 90, 12, 23, 68]
# print("Before sorting:",num_list)
# sorted_list = merge_sort(num_list)
# print("After sorting:",sorted_list)

'''
Quick Sort 
'''
def partition(list, low, high):
    # element at i should be smaller than pivot
    i = low + 1 

    # element at j should be greater than pivot
    j = high
    pivot = list[low]
    done = False

    # this while loop is to make the elements smaller than pivot be on the left and the ones larger on the right
    while not done:        
        # i and j has not crossed
        while i<=j and list[i] <= pivot:
            i += 1 
        # i done incrementing as it has found an element that is more than pivot
        # it is not j's turn to keep decrementing until it found an element that is lower than pivot
        while j>=i and list[j] >= pivot:
            j -= 1
        
        # found left element that is larger than pivot and right element that is smaller than pivot
        # if not crossed
        if (j > i):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        # i and j crossed
        else:
            done = True
    # swap is done for current pivot.
    # elements on the left is smaller than pivot and on the right is larger than pivot
    # swap pivot and j (j < i)
    temp = list[low]
    list[low] = list[j]
    list[j] = temp

    return j # new pivot position

def quick_sort(list, low, high):
    if low >= high:
        return
    
    pivot_index = partition(list, low, high)
    quick_sort(list, low, pivot_index-1)
    quick_sort(list, pivot_index+1, high)

num_list=[3,1,0,4,2]
print("Before sorting:",num_list)
quick_sort(num_list, 0, len(num_list)-1)
print("After sorting:",num_list)
