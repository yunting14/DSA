# Using dynamic programming 
def longest_increasing_subsequence(num_list):
    # L = longest length ending at each number in the number list
    L = [1] * len(num_list)
    
    # prev = to store index reference of previous smaller number
    prev = [-1] * len(num_list)
    
    # filling in L - longest length of subsequence ending at each number
    for i in range(1, len(L)):
        # sub = [L[k] for k in range(i) if num_list[k] < num_list[i]]
        sub = []
        for k in range(i):
            if num_list[k] < num_list[i]:
                sub.append(L[k])
                prev[i] = k
        L[i] = 1 + max(sub, default=0)
    longest_length = max(L, default=0)
    
    # to get the list of longest increasing subsequence 
    LIS = [-1] * longest_length
    previous_index = prev[L.index(longest_length)]
    LIS[longest_length-1] = num_list[L.index(longest_length)]
    for l in range(longest_length-2, -1, -1):
        LIS[l] = num_list[previous_index]
        previous_index = prev[previous_index]
    
    return LIS

def lis_dynamic(num_list):
    L = [1] * len(num_list)
    
    # prev = to store index reference of previous smaller number
    prev = [-1] * len(num_list)
    
    # filling in L - longest length of subsequence ending at each number
    for i in range(1, len(L)):
        # sub = [L[k] for k in range(i) if num_list[k] < num_list[i]]
        sub = []
        for k in range(i):
            if num_list[k] < num_list[i]:
                sub.append(L[k])
                prev[i] = k
        L[i] = 1 + max(sub, default=0)
    return max(L, default=0)

# Using recursion
global maximum
def lis_recursion(num_list, n):
    global maximum

    if n==1:
        return 1
    
    maxEndingHere = 1

    for i in range(1,n):
        res = lis_recursion(num_list, i)
        if num_list[i-1] < num_list[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res+1 

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere

def lis(num_list):
    global maximum

    n = len(num_list)
    maximum = 1

    lis_recursion(num_list, n)
    return maximum

# nums = [3, 1, 8, 4, 5, 4]
nums = [5,2,8,6,3,6,9,5]
print(lis_recursion(nums, len(nums)))
# print(longest_increasing_subsequence(nums))