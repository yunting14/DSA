'''
Exercise on Searching a String - Level 1
'''
def pattern_search(text, pattern):
    count = 0
    text = text
    while True:
        index_found = text.find(pattern)
        if index_found == -1:
            break
        count += 1 
        text = text[index_found+len(pattern):]
    return count

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
# print("The given text:",text)
# print("Pattern:",pattern)
# print("No. of occurrences of the pattern :",result)

'''
Exercise on Searching an Index - Level 1
'''
def find_decreasing_start(list1,start,end):
        for i in range (len(list1)):
            if int(str(list1[i])) < int(str(list1[i+1])):
                continue
            
            if int(str(list1[i])) > int(str(list1[i+1])):
                return i+1

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
# result=find_decreasing_start(list1,start,end)
# print("The index position at which the increasing array starts decreasing is:",result)

'''
Assignment on Searching in Stack & Queue - Level 1
'''
# first in first out 
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*max_size
        self.__rear=-1
        self.__front=0
    
    def is_full(self):
        if (self.__rear == self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if (self.__front > self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data
        
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
    
    def max_size(self):
        return self.__max_size

# first in last out / last in first out
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if (self.__top == self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if (self.__top == -1):
            return True
        return False
    
    def push(self, data):
        if self.is_full():
            print("The stack is empty")
        else:
            self.__top += 1
            self.__elements[self.__top] = data
    
    def pop(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data
    
    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index = index-1
    
    def get_max_size(self):
        return self.__max_size
    
    def top(self):
        return self.__elements[self.__top]
    
def separate_boxes(box_stack):
    max_size = box_stack.get_max_size()

    primary = []

    new_queue = Queue(max_size)

    for i in range(max_size):
        color = box_stack.pop()
        if color == None:
            break

        if color not in ["Red", "Green", "Blue"]:
            new_queue.enqueue(color)
        else:
            primary.append(color)

    if box_stack.is_empty():
        for i in range(len(primary)-1, -1, -1):
            box_stack.push(primary[i])

    return new_queue  

def separate_boxes2(box_stack):
    max_size = box_stack.get_max_size()

    primary = []

    new_queue = Queue(max_size)

    for i in range(max_size):
        color = box_stack.top()
        if color == None:
            break
        if color not in ["Red", "Green", "Blue"]:
            box_stack.pop()
            new_queue.enqueue(color)
        else:
            primary.append(color)
            box_stack.pop()
    
    if box_stack.is_empty():
        for i in range(len(primary)-1, -1, -1):
            box_stack.push(primary[i])
    
    return new_queue
            

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
# print("Boxes in the stack:")
# box_stack.display()
# result=separate_boxes(box_stack)
# print()
# print("Boxes in the stack after modification:")
# box_stack.display()
# print("Boxes in the queue:")
# result.display()

'''
Assignment on Searching in Dictionary - Level 2
'''
def find_matches(country_name):
    list_matches = []

    for match in match_list:
        values = match.split(":")
        if values[0] != country_name:
            continue
        list_matches.append(match)
    
    return list_matches

def max_wins():
    max_wins_dict = {}

    for match in match_list:
        values = match.split(":")
        championship = values[1]
        if championship not in max_wins_dict:
            max_wins_dict[championship] = [match]
        else:
            max_wins_dict[championship].append(match)
    
    for champ in max_wins_dict:
        matches = max_wins_dict[champ]
        current_highest = 0
        highest_wins_countries = []
        for m in matches:
            values = m.split(":")
            country = values[0]
            win = values[3]
            if int(str(win)) < int(str(current_highest)):
                continue
            elif int(str(win)) == int(str(current_highest)):
                highest_wins_countries.append(country)
            elif int(str(win)) > int(str(current_highest)):
                current_highest = win
                highest_wins_countries = [country]
        max_wins_dict[champ] = highest_wins_countries
    
    return max_wins_dict

def find_winner(country1,country2):
    country1_wins = 0
    country2_wins = 0

    for match in match_list:
        values = match.split(":")
        country = values[0]
        wins = int(values[3])
        if country == country1:
            country1_wins += wins
        elif country == country2:
            country2_wins += wins
    
    if country1_wins == country2_wins:
        return "Tie"
    elif country1_wins > country2_wins:
        return country1
    else:
        return country2

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
# print("The match status list details are:")
# print(match_list)
# print()

# print(find_matches("AUS"))
# print(max_wins())
# print(find_winner("AUS","IND"))

'''
Assignment on Searching in List of Strings - Level 2
'''

def find_unknown_words(text,vocabulary):
    output = set()
    words = text.replace(".","").split(" ")
    for word in words:
        if word.lower() not in vocabulary and word not in output:
            output.add(word)
    
    if len(output) == 0:
        return -1 
    
    return output

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
# print("The unknown words in the file are:",unknown_words)

'''
Assignment on Searching in List of Numbers - Level 1
Try to do by binary search
'''
def last_instance(num_list,  start,  end,  key):
    start = start
    end = end
    middle = (end + 1 - start) // 2 + start
    num = num_list[middle]
    count = 0
    while num != key:
        count += 1
        if num > key:
            end = middle
        elif num < key:
            start = middle
        middle = (end + 1 - start) // 2 + start
        num = num_list[middle]
        if (count == len(num_list)):
            return -1

    # an occurence of key found
    index_last_occur = middle
    for i in range(middle, end+1):
        if num_list[i] == key:
            index_last_occur = i
    
    return index_last_occur

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")