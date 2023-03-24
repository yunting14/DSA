'''
Assignment Level 1
'''
def make_change(denomination_list, amount):
    # sort denomination list
    for i in range(len(denomination_list)-1):
        swapped = False
        for j in range(len(denomination_list)-i-1):
            if denomination_list[j] < denomination_list[j+1]:
                temp = denomination_list[j]
                denomination_list[j] = denomination_list[j+1]
                denomination_list[j+1] = temp
                swapped = True
        if swapped == False:
            break
    
    # amount smaller than all denomination
    if amount < denomination_list[-1]:
        return -1

    # get count of notes
    count_notes = 0
    remanining = amount
    for d in denomination_list:
        if remanining >= d:
            remainder = remanining % d
            count_notes += (remanining - remainder) // d
            remanining = remainder
        else:
            continue
    
    return count_notes
#Pass different values to the function and test your program
# amount= 30
# denomination_list = [20,2,3,1]
amount= 20
denomination_list = [1,15,10]
# print(make_change(denomination_list, amount))

'''
Assignment Level 2
'''
def sort(activity_list, start_time_list):
    for i in range(len(activity_list)-1):
        swapped = False
        for k in range(len(activity_list)-i-1):
            if start_time_list[k] > start_time_list[k+1]:
                temp = start_time_list[k]
                start_time_list[k] = start_time_list[k+1]
                start_time_list[k+1] = temp

                temp2 = activity_list[k]
                activity_list[k] = activity_list[k+1]
                activity_list[k+1] = temp2

                swapped = True
        if swapped == False:
            break
    return activity_list, start_time_list

def find_maximum_activities(activity_list,start_time_list, finish_time_list):
    no_of_activities = len(activity_list)
    possible_activities = []
    
    # find first activity, may not be 1
    first_activity_index = 0
    earliest = start_time_list[0]
    for st_idx in range(no_of_activities):
        st = start_time_list[st_idx]
        if st < earliest:
            earliest = st
            first_activity_index = st_idx
    possible_activities.append(activity_list[first_activity_index])
    
    # append first activity
    # first_act_index = start_time_list.index(1)
    # possible_activities.append(activity_list[first_act_index])

    # append the other activities
    for i in range(len(activity_list)):
        last_act = possible_activities[-1]
        last_act_index = activity_list.index(last_act)
        last_act_end_time = finish_time_list[last_act_index]

        unsorted_start_list = start_time_list[:last_act_index] + start_time_list[last_act_index+1:]
        unsorted_activity_list = activity_list[:last_act_index] + activity_list[last_act_index+1:]
        sorted_activity_list, sorted_start_time = sort(unsorted_activity_list, unsorted_start_list)
        
        for k in range(len(sorted_activity_list)):
            if sorted_start_time[k] > last_act_end_time:
                possible_activities.append(sorted_activity_list[k])
                break
    
    return possible_activities


#Pass different values to the function and test your program
# test case 1 - passed (failed in lex)
activity_list=[11, 12, 32, 44, 53, 62]
start_time_list=[12, 14, 21, 31, 16, 18]
finish_time_list= [20, 16, 25, 35, 17, 20]

# test case 2 - passed
# activity_list=[1, 2, 3, 4, 5, 6]
# start_time_list=[5, 4, 8, 2, 3, 1]
# finish_time_list= [13, 6, 16, 7, 5, 4]

# test case 3 - passed
# activity_list = [1, 2, 3, 4, 5, 6]
# start_time_list = [1, 3, 0, 5, 8, 5]
# finish_time_list = [2, 4, 6, 7, 9, 9]

print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)
