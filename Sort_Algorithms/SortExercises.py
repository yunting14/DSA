# using selection sort 
def order_heights(student_list,height_list):
    for i in range(len(height_list)):
        for k in range(i, len(height_list)):
            if height_list[k] < height_list[i]:
                temp = height_list[i]
                height_list[i] = height_list[k]
                height_list[k] = temp

                temp2 = student_list[i]
                student_list[i] = student_list[k]
                student_list[k] = temp2
    return[student_list,height_list]

student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
# print("Initial student details :")
# print("The students:",student_list)
# print("Their heights:",height_list)
# print()
# result=order_heights(student_list,height_list)
# print("After arranging the students in the order of their height:")
# print("The students :",result[0])
# print("Their heights:",result[1])

'''
Exercise on Sorting List of Strings - Level 2
'''
def arrange_tickets(tickets_list):
    with_vacancies = ["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10",
                      "T11","T12","T13","T14","T15","T16","T17","T18","T19","T20"]
    for i in range(20):
        if with_vacancies[i] not in tickets_list:
            with_vacancies[i] = "V"
    
    group1 = with_vacancies[:10]
    group2 = with_vacancies[10:]
    
    for i in range(10):
        if group1[i] == "V":
            t_from_group2 = ""
            for k in range(10):
                if group2[k] != "V":
                    t_from_group2 = group2[k]
                    group2[k] = "V"
                    break
            group1[i] = t_from_group2
        else:
            continue

    return group1


tickets_list = ['T20','T5','T10','T1','T2','T8','T16','T17','T9','T4','T12','T13', 'T18']
# print("Ticket ids of all the available students :")
# print(tickets_list)
# result=arrange_tickets(tickets_list)
# print()
# print("Ticket ids of the ten students in Group-1:")
# print(result)

'''
Assignment on Sorting List of Objects - Level 2
'''
#Implement Item class here
class Item:
    def __init__(self,item_name,author_name,published_year):
        self.item_name = item_name
        self.author_name = author_name
        self.published_year = published_year
    
    def get_item_name(self):
        return self.item_name
    
    def get_author_name(self):
        return self.author_name
    
    def get_published_year(self):
        return self.published_year
    
    def __str__(self):
        return f"Item name: {self.item_name} | Author: {self.author_name} | Published year: {self.published_year}"

#Implement Library class here
class Library:
    def __init__(self, item_list):
        self.item_list = item_list
    
    def get_item_list(self):
        return self.item_list
    
    # using bubble sort
    def sort_item_list_by_author(self,new_item_list):
        for i in range(len(new_item_list)-1):
            swapped = False
            for k in range(len(new_item_list)-i-1):
                author1 = new_item_list[k].get_author_name()
                author2 = new_item_list[k+1].get_author_name()

                author_before = ""
                shorter_name = author1
                if len(author2) > len(author1):
                    shorter_name = author2

                for c in range(len(shorter_name)):
                    if author1[c].upper() == author2[c].upper():
                        continue

                    if author1[c].upper() < author2[c].upper():
                        author_before = author1
                        break
                    else:
                        author_before = author2
                        break
                
                if author_before == author1:
                    continue
                elif author_before == author2:
                    temp = new_item_list[k]
                    new_item_list[k] = new_item_list[k+1]
                    new_item_list[k+1] = temp
                    swapped = True
            if swapped == False:
                break
        
        return new_item_list
    
    def add_new_items(self,new_item_list):
        self.item_list = self.item_list + new_item_list
        self.item_list = self.sort_item_list_by_author(self.item_list)
    
    # bubble sort
    def sort_items_by_published_year(self):
        item_count = len(self.item_list)
        
        for i in range(item_count-1):
            swapped = False
            for k in range(item_count-i-1):
                year1 = self.item_list[k].get_published_year()
                year2 = self.item_list[k+1].get_published_year()
                if year1 > year2:
                    temp = self.item_list[k]
                    self.item_list[k] = self.item_list[k+1]
                    self.item_list[k+1] = temp
                    swapped = True
                elif year1 == year2:
                    arranged = self.sort_item_list_by_author([self.item_list[k], self.item_list[k+1]])
                    self.item_list[k] = arranged[0]
                    self.item_list[k+1] = arranged[1]
                    swapped = True
                else:
                    continue
            if swapped == False:
                break
        
        return self.item_list

#Use different values for item and test your program
item1=Item("A Mission In Kashmir","Andrew Whitehead",1995)
item2=Item("A Passage of India","E.M.Forster",2012)
item3=Item("A new deal for Asia","Mahathir Mohammad",1999)
item4=Item("A Voice of Freedom","Nayantara Sehgal",2001)
item5=Item("A pair of blue eyes","Thomas Hardy",1998 )

item_list=[item1,item2,item3,item4,item5]
library=Library(item_list)
# print("The current items in the library are:")
# for item in library.get_item_list():
#     print(item)

item11=Item("Broken Wing","Sarojini Naidu",2012)
item12=Item("Guide","R.K.Narayanan",2001)
item13=Item("Indian Summers","John Mathews",2001)
item14=Item("Innocent in Death","J.D.Robb",2010)
item15=Item("Life of Pi","Yann Martel",2010 )
item16=Item("Sustainability","Johny",2016)
item17=Item("Look Ahead","E.M.Freddy",2012 )

# new_item_list=[item11,item12,item13,item14,item15,item16,item17]
# print()
# print("The new items to be added are:")
# for item in new_item_list:
#     print(item)

# new_item_list_sorted=library.sort_item_list_by_author(new_item_list)
# print()
# print("The new items after sorting based on the author name are:")
# for item in new_item_list_sorted:
#     print(item)

# library.add_new_items(new_item_list_sorted)
# print()
# print("The final set of items after adding the new item list are:")
# for item in library.get_item_list():
#     print(item)

# items = library.sort_items_by_published_year()
# print()
# print("The final set of items sorted by published year are:")
# for item in library.get_item_list():
#     print(item)

# print("\n\n")

'''
Assignment on Sorting Lists - Level 3
'''
"""*********************Queue*****************************"""
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

"""*********************Stack*****************************"""
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

#Global variables
flight_details=["AI890:BAN:MUM:1400","AI678:BAN:LON:1200","AI345:BAN:CAN:1410","AF780:BAN:AGF:1340","AI001:BAN:AUS:1500","AI404:BAN:NY:1220"]

passenger_details_dict=\
{"LW101":["Amanda","AI678","C7",25],"LW103":["John","AI345","A2",10],"LW107":["Alex","AI678","G5",12],\
"TW700":["Hary","AF780","D2",26],"LW167":["Kate","AI001","G3",25],"LT890":["Wade","AI404","G3",25],\
"TW677":["Preet","AF780","D3",25],"LA106":["Henry","AI001","B5",25.5],"LA104":["Ajay","AI001","A7",23],\
"LW202":["Amy","AI345","C3",24.5],"LT673":["Susan","AI404","J8",5],"TW709":["Tris","AF780","H5",22.5],\
"LA188":["Cameron","AI890","H4",22],"LA902":["Scofield","AI678","G4",23],"TW767":["Pom","AF780","H4",2],\
"LW787":["Burrows","AI890","B4",29],"LW898":["Sara","AI678","E4",14],"LW104":["Williams","AI890","C4",10] }

def find_flights(flight_time):
    flights_in_range = []
    for flight in flight_details:
        values = flight.split(":")
        time = int(values[3])
        if (time >= flight_time and time <= flight_time+200 ):
            flights_in_range.append(flight)

    return flights_in_range

def sort_flight_list(flight_list):
    for i in range(len(flight_list)-1):
        flight1 = flight_list[i]
        flight2 = flight_list[i+1]
        flight1_time = int(flight1.split(":")[3])
        flight2_time = int(flight2.split(":")[3])

        if (flight1_time > flight2_time):
            flight_list[i] = flight2
            flight_list[i+1] = flight1
    
    return flight_list

def get_passenger_details(flight_detail):
    flight_name = flight_detail.split(":")[0]
    list_passengers = []

    for pnr in passenger_details_dict:
        flight_info = passenger_details_dict[pnr]
        flight_num = flight_info[1]
        if flight_name == flight_num:
            list_passengers.append(pnr)

    return list_passengers

def security_check(passenger_pnr_list):
    cleared = []
    for p in passenger_pnr_list:
        pass_info = passenger_details_dict[p]
        baggage = int(pass_info[3])
        if baggage >= 0 and baggage <=25:
            cleared.append(p)
    return cleared

def sort_passengers(passenger_pnr_list):
    for i in range(len(passenger_pnr_list)-1):
        pnr1 = passenger_pnr_list[i]
        pass_details1 = passenger_details_dict[pnr1]
        seat_num1 = pass_details1[2]

        pnr2 = passenger_pnr_list[i+1]
        pass_details2 = passenger_details_dict[pnr2]
        seat_num2 = pass_details2[2]

        if (seat_num1[0] > seat_num2[0]):
            passenger_pnr_list[i] = pnr2
            passenger_pnr_list[i+1] = pnr1
        elif (seat_num1[0] == seat_num2[0]):
            seat_digits1 = int(seat_num1[1:])
            seat_digits2 = int(seat_num2[1:])

            if seat_digits1 > seat_digits2:
                passenger_pnr_list[i] = pnr2
                passenger_pnr_list[i+1] = pnr1
    return passenger_pnr_list

def boarding(passenger_pnr_list):
    new_queue = Queue(len(passenger_pnr_list))
    for p in passenger_pnr_list:
        new_queue.enqueue(p)
    return new_queue

def seating(passenger_queue):
    new_stack = Stack(passenger_queue.get_max_size())
    for i in range(passenger_queue.get_max_size()):
        passenger = passenger_queue.dequeue()
        new_stack.push(passenger)
    return new_stack

print("The flight details :")
print(flight_details)
print()
print("The passenger details at the airport:")
print(passenger_details_dict)
print()
time=1130
print("Details of the flight between the timings",time,"and",time+200,"are:")
flight_list=find_flights(time)
flight_list=sort_flight_list(flight_list)
print(flight_list)
print()
print("Details of the passengers boarding the flights between the timings ",time,"and",(time+200),"are:")
print()
for i in range(0,len(flight_list)):
    flight_data=flight_list[i].split(':')
    flight_name=flight_data[0]

    passenger_pnr_list=get_passenger_details(flight_list[i])
    print("PNR details of the passengers boarding the flight",flight_name,":")
    print(passenger_pnr_list)

    print()
    updated_passenger_pnr_list=security_check(passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," whose baggage has been cleared:")
    print(updated_passenger_pnr_list)

    sorted_passenger_pnr_list=sort_passengers(updated_passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," sorted based on seating number:")
    print(sorted_passenger_pnr_list)

    print()
    print("The PNR details of the passengers at the queue",flight_name,":")
    passenger_queue=boarding(updated_passenger_pnr_list)
    passenger_queue.display()

    print()
    seating_stack=seating(passenger_queue)
    print("The PNR details of the passengers in the flight",flight_name,":")
    seating_stack.display()