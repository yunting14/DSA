'''
Assignment on Brute Force Approach on List - Level 2
'''

#lex_auth_0127667393053655043361
def getChar(n):
    alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z")
    return alphabet[n+1]

def create_combinations(digit_list):
    if digit_list is []:
        return [""]

    output1 = []
    string1 = ""
    for digit in digit_list:
        string1 += getChar(digit)
    output1.append(string1)

    return []

def count_decoding(digit_list):
    
    pass

#Pass different values to the function and test your program
digit_list=[9,8,1,5]
# print("Number of possible decodings for the given sequence is:",count_decoding(digit_list))

'''
Assignment on Greedy Approach - Level 2
'''
#lex_auth_0127667363417702403454
def find_number_of_platforms(arrival_time_list,departure_time_list):
    # sort time list by arrival time
    for i in range (len(arrival_time_list)-1):
        swapped = False
        for k in range(len(departure_time_list)-i-1):
            if arrival_time_list[k] > arrival_time_list[k+1]:
                temp1 = arrival_time_list[k]
                arrival_time_list[k] = arrival_time_list[k+1]
                arrival_time_list[k+1] = temp1

                temp2 = departure_time_list[k]
                departure_time_list[k] = departure_time_list[k+1]
                departure_time_list[k+1] = temp2

                swapped = True
        if swapped == False:
            break
    
    train_dict = {}
    for num in range(len(arrival_time_list)):
        train_dict[num+1] = []

    for a in range(len(arrival_time_list)):
        arr_time = arrival_time_list[a]
        # get all departure times of trains in train_dict and compare if any is scheduled to leave
        for platform, time in train_dict.items():
            if time != []:
                dep_time = time[1]
                if dep_time <= arr_time:
                    train_dict[platform] = [arr_time, departure_time_list[a]]
                    break
            else:
                train_dict[platform] = [arr_time, departure_time_list[a]]
                break
    
    number_platforms = 0
    for platform, time in train_dict.items():
        if time != []:
            number_platforms += 1
    
    return number_platforms
    

#Pass different values to the function and test your program
# arrival_time_list = [800,810]
# departure_time_list = [2300,2000]

# arrival_time_list = [800,850,600,1120,1050,900]
# departure_time_list = [1110,1200,1400,1130,1700,2200]

# arrival_time_list = [800,850,600, 1350, 1120,1050,900]
# departure_time_list = [1110,1200,830, 1400, 1130,1700,2200]

arrival_time_list=[800, 810, 900, 740, 1200, 1400]
departure_time_list=[2300, 2000, 1200, 1349, 1500, 2120]
# print("The arrival time of the trains:", arrival_time_list)
# print("The departure time of the trains:",departure_time_list)
# print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))

'''
Assignment on Brute Force Approach - Level 2
'''
'''
K : size of string 
First We Generate All string starts with '0'
initialize n = 1 . 
GenerateALLString ( K  , Str , n )
  a. IF n == K 
     PRINT str.
  b. IF previous character is '1' :: str[n-1] == '1'
     put str[n] = '0'
     GenerateAllString ( K , str , n+1 )
  c. IF previous character is '0' :: str[n-1] == '0'
     First We Put zero at end and call function 
      PUT  str[n] = '0'
           GenerateAllString ( K , str , n+1 )  
      PUT  str[n] = '1'
           GenerateAllString ( K , str , n+1 )

Second Generate all binary string starts with '1'
DO THE SAME PROCESS
'''

def count_strings(number):
    if number < 1:
        print(arr)
    
    arr[number-1] = "0"
    count_strings(number-1)
    arr[number-1] = "1"
    count_strings(number-1)


#Pass different values to the function and test your program
number=3
arr = [] * number
print("The number of strings that can be made are:",count_strings(number))

# arr = [[1,2,3], [1], [1,2]]
# print(len(arr))