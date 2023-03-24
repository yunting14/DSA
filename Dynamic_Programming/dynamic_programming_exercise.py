'''
Exercise on Dynamic Programming - Level 2
'''

#lex_auth_0127667323215544323487
def max_sum_is(num_list):
    lis = [[num_list[i]] for i in range(len(num_list))]

    for i in range(len(num_list)):
        sub = []
        for k in range(i):
            if num_list[k] < num_list[i]:
                sub.append(lis[k]+[num_list[i]])
        max1 = 0
        for list in sub:
            sum1 = 0
            for n in list:
                sum1 += n
            if sum1 > max1:
                max1 = sum1
                lis[i] = list
    
    max_sum_is = 0
    for list1 in lis:
        sum_is = sum(list1)
        if sum_is > max_sum_is:
            max_sum_is = sum_is
    return max_sum_is

#Pass different values to the function and test your program
nums=[1,2,3,4,5]
print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(nums))