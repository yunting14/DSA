class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data
    
    def get_next(self):
        return self.__next
    
    def set_next(self, next_node):
        self.__next = next_node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def display(self):
        temp = self.__head
        
        while (temp != None):
            print(temp.get_data())
            temp = temp.get_next()
        
        print("(Head:", self.get_head().get_data(), ",Tail:", self.get_tail().get_data(), ")")

    def add(self, data):
        new_node = Node(data)
        
        # LL empty, make head node and tail node refer to new node
        if (self.__head == None):
            self.__head = new_node
            self.__tail = self.__head
            return
        
        # not empty
        # if 1 item, head = tail
        self.__tail.set_next(new_node)
        self.__tail = new_node
        
def count_nodes(linked_list):
    count=0
    curr_node = linked_list.get_head()
    while (curr_node != None):
        count += 1
        curr_node = curr_node.get_next()
    return count

biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

# print(count_nodes(biscuit_list))

def merge_list(list1, list2):
    merged_data=""
    
    if (len(list1) != len(list2)):
        return
    
    for i in range(len(list1)):
        if (list1[i] == None):
            merged_data += ""
        else:
            merged_data += list1[i]
        if (list2[-(i+1)] == None):
            merged_data += ""
        else:
            merged_data += list2[-(i+1)]
        merged_data += " "
    
    return merged_data[:-1]

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
# print(merged_data)


# ASSIGNMENT SET 1
class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program

class Service:
    def __init__(self, car_list):
        self.car_list = car_list
    
    def find_cars_by_year(self, year):
        cars = []
        for car in self.car_list:
            if car.get_year() == year:
                cars.append(car)
        
        if len(cars) == 0:
            print("None found")
        else:
            for c in cars:
                print(c.__str__())
    
    def add_cars(self, new_car_list):
        if (len(new_car_list) == 0):
            return 
        
        self.car_list = self.car_list + new_car_list
        
        def condition(c):
            return c.get_year()
        
        self.car_list.sort(key=condition)
        
        for c in self.car_list:
            print(c.__str__()) 
    
    def remove_cars_from_karnataka(self):
        removed = []
        for car in self.car_list:
            reg_no = car.get_registration_number()
            if (reg_no[:2] == "KA"):
                self.car_list.remove(car)
                removed.append(car)
        if len(removed) == 0:
            print("No cars from Karnataka found")
        else:
            print(len(removed),"cars removed")
            for c in removed:
                print(c.__str__())

car_serve = Service(car_list)
# cars = car_serve.find_cars_by_year(2013)
car6=Car("Kia",2010,"KA09 3056")
car7=Car("Hondai", 2011, "MH10 6776")
car8=Car("Toyota", 2015,"KA12 9098")
new_cars = [car6,car7,car8]
# car_serve.add_cars(new_cars)
# print()
# car_serve.remove_cars_from_karnataka()

def check_double(list1,list2):
    new_list=[]
    
    if (len(list1)==0 or len(list2)==0):
        return None
    
    for num in list1:
        double = num*2
        if list2.__contains__(double):
            new_list.append(num)
    
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
# print(check_double(list1, list2))

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
    def __init__(self,players_list):
        if (player_list == None or len(players_list)==0):
            return None
        
        self.player_list = player_list
    
    def sort_players_based_on_experience(self):
        self.player_list.sort(key=lambda player: -player.get_experience())
    
    def shift_player_to_new_position(self, old_index_position, new_index_position):
        player = self.player_list[old_index_position]
        self.player_list.remove(player)
        self.player_list.insert(new_index_position, player)
    
    def display_player_details(self):
        self.sort_players_based_on_experience()
        self.shift_player_to_new_position(0, 3)
        for player in self.player_list:
            print(player.__str__())

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)

player_list = [player1,player2,player3,player4,player5,player6,player7,player8,player9,player10]
game1 = Game(player_list)
# game1.display_player_details()

#LINKED LIST SEARCH AND INSERT OPERATION
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
    
class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_head(self):
        return self.head
    
    def set_head(self, node):
        self.head = node
    
    def get_tail(self):
        return self.tail
    
    def set_tail(self, node):
        self.tail = node
    
    def add(self, data):
        new_node = Node2(data)
        # if empty
        if (self.head == None):
            self.head = self.tail = new_node
            return
        
        self.tail.set_next(new_node)
        self.tail = new_node
            
    def display(self):
        curr = self.head
        while (curr != None):
            print(curr.get_data())
            curr = curr.get_next()
    
    def find_node(self, data):
        curr = self.head
        while (curr != None):
            if (curr.get_data() == data):
                return curr
            curr = curr.get_next()
        return None
    
    def insert(self, data, data_before):
        new_node = Node2(data)
        node_before = None
        
        curr_node = self.head
        while (curr_node != None):
            if (curr_node.get_data() == data_before):
                node_before = curr_node
                break
            curr_node = curr_node.get_next()
        
        if (node_before == None):
            print(data_before,"not found in list.",data,"will be added to the top of the list.")
            new_node.set_next(self.head)
            self.head = new_node
            
            if new_node.get_next() == None:
                self.tail = new_node
            
        else:
            node_after = node_before.get_next()
            node_before.set_next(new_node)
            new_node.set_next(node_after)
            
            if (new_node.get_next()==None):
                self.tail = new_node     
    
    def delete(self, data):
        node_to_delete = self.find_node(data)
        
        # if found
        if (node_to_delete != None):
            
            # if it is head node
            if (node_to_delete == self.head):
                self.head = self.head.get_next()
            # if it is also tail node
                if (node_to_delete == self.tail):
                    self.tail == None
                return
            
            if (node_to_delete != self.head):
                node_before = None
                curr_node = self.head
                while (curr_node != node_to_delete):
                    node_before = curr_node
                    curr_node = curr_node.get_next()
                node_after = node_to_delete.get_next()
                node_before.set_next(node_after)
                
                if (node_to_delete == self.tail):
                    self.tail == node_before
                
                return
        # not found
        else:
            print("List does not contain data")
                

llist1=LinkedList2()
#Add all the required element(s)
#Search for the required node
llist1.add("Flour")
llist1.add("Tea")
llist1.add("Coffee")
llist1.add("Sugar")
llist1.insert("Jam", "Coffee")
llist1.delete("Sugar")
# llist1.display()

# node=llist1.find_node("Sugar")
# if(node!=None):
#     print("Node found")
# else:
#     print("Node not found") 

def find_total_nodes(mem_block):
    curr_node = mem_block.get_head()
    count = 0
    while (curr_node != None):
        count += 1
        curr_node = curr_node.get_next()
    return count

def maximum_contiguous_free_blocks(mem_block):
    curr_node = mem_block.get_head()
    count_max_cont_free = 0
    arr_cont_free = []
    
    while (curr_node != None):
        curr_data = curr_node.get_data()
        if (curr_data == "Free"):
            count_max_cont_free += 1
        if (curr_data == "Occupied"):
            arr_cont_free.append(count_max_cont_free)
            count_max_cont_free = 0
        curr_node = curr_node.get_next()
    arr_cont_free.append(count_max_cont_free)
    
    count_total = find_total_nodes(mem_block)
    max_free = max(arr_cont_free)
    return (max_free / count_total) * 100

def total_free_blocks(mem_block):
    curr_node = mem_block.get_head()
    count_free = 0
    
    while (curr_node != None):
        data = curr_node.get_data()
        if (data == "Free"):
            count_free += 1
        curr_node = curr_node.get_next()
    
    count_total = find_total_nodes(mem_block)
    return (count_free / count_total) * 100


def memory_compaction(mem_block):
    curr_node = mem_block.get_head()
    first_occupied_node = None
    last_occupied_node = None
    first_free_node = None 
    last_free_node = None
    
    while (curr_node != None):
        data = curr_node.get_data()
        if (data == "Free"):
            if (first_free_node == None):
                first_free_node = curr_node
                last_free_node = curr_node
            else:            
                last_free_node.set_next(curr_node)
                last_free_node = curr_node
        if (data == "Occupied"):
            if (first_occupied_node == None):
                first_occupied_node = curr_node
                last_occupied_node = curr_node
            else:
                last_occupied_node.set_next(curr_node)
                last_occupied_node = curr_node
        curr_node = curr_node.get_next()
    
    # linking all the blocks up
    mem_block.set_head(first_occupied_node)
    mem_block.set_tail(last_free_node)
    last_occupied_node.set_next(first_free_node)
            

mem_block=LinkedList2()
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Free")

# print("Before compaction")
# print("_________________")
# print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block),"%")
# print("Total free blocks:",total_free_blocks(mem_block),"%")
#
# memory_compaction(mem_block)
#
# print()
# print("After compaction")
# print("________________")
# print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block),"%")
# print("Total free blocks:",total_free_blocks(mem_block),"%")

myList = LinkedList2()
myList.add(1)
myList.add(4)
myList.add(9)
myList.add(16)

def fun(head):
    if(head==None):
        return
    if head.get_next().get_next()!= None:
        print(head.get_data()," ", end='')
        fun(head.get_next())
    print(head.get_data()," ",end='')

# fun(myList.get_head())

def fun2(head):
    next_node = head.get_next()
    while(head!=None and next_node != None):
        head.set_data(head.get_data()+next_node.get_data())
        head = head.get_next()
        next_node = head.get_next()
        if(next_node != None):
            head.set_data(head.get_data()+next_node.get_data())
fun2(myList.get_head())
# myList.display()

# Given a linked list containing whole numbers, 
# write a python function which finds and returns the sum of 
# all the elements at the odd position in the given linked list.

def find_sum(number_list):
    sum = 0
    count = 1
    curr_node = number_list.get_head()
    while (curr_node != None):
        if count % 2 != 0:
            sum += curr_node.get_data()
        count += 1
        curr_node = curr_node.get_next()
    return sum

# Write a python program to find the maximum value in a 
# linked list and replace it with a given value.
# Assume that the linked list is populated with whole numbers 
# and there is only one maximum value in the linked list.

def replace_maximum(number_list,new_value):
    curr_node = number_list.get_head()
    max = 0
    while (curr_node != None):
        data = curr_node.get_data()
        if (data > max):
            max = data
        curr_node = curr_node.get_next()
    
    curr_node = number_list.get_head()
    while (curr_node != None):
        data = curr_node.get_data()
        if data == max:
            curr_node.set_data(new_value)
            break
        curr_node = curr_node.get_next()
    return number_list

number_list=LinkedList2()
number_list.add(200)
number_list.add(95)
number_list.add(140)
number_list.add(110)
number_list.add(40)

new_value=100
number_list=replace_maximum(number_list,new_value)
# number_list.display()


# Circle and Shape LL exercise.
class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
    
    def __str__(self):
        return (self.color+" "+str(self.radius))
    
    def get_color(self):
        return self.color
    
    def get_radius(self):
        return self.radius

class Shape:
    def __init__(self, circle_list):
        self.circle_list = circle_list
    
    def get_circle_list(self):
        return self.circle_list
    
    # unable to pass the test case... don't understand the inputs
    def insert_circle(self, new_circle):
        if (new_circle == None):
            return
        
        new_node = Node2(new_circle)
        head = self.circle_list.get_head()
        new_node.set_next(head)
        self.circle_list.head = new_node
        
circle1=Circle("Red",4)
circle2=Circle("Green",5)
circle3=Circle("Purple",3.5)
new_circle=Circle("Blue",6)

circle_list=LinkedList2()
circle_list.add(circle1)
circle_list.add(circle2)
circle_list.add(circle3)

shape=Shape(circle_list)
shape.insert_circle(new_circle)
shape.get_circle_list().display()    

# Replace * or / Question
def create_new_sentence(word_list):
    new_sentence=""
    
    check = ["/", "*"]
    
    curr_node = word_list.get_head()
    while (curr_node != None):
        char = curr_node.get_data()
        next_char = ""
        if (curr_node.get_next() != None):
            next_char = curr_node.get_next().get_data()
        
        # is a single instance
        if (check.__contains__(char) == True and check.__contains__(next_char)==False):
            curr_node.set_data(" ")
        # double instance
        elif (check.__contains__(char) == True and check.__contains__(next_char)==True):
            curr_node.set_data(" ")
            curr_node.get_next().set_data("")
            curr_node.get_next().get_next().set_data(curr_node.get_next().get_next().get_data().upper())
        
        curr_node = curr_node.get_next()
    
    curr_node = word_list.get_head()
    while (curr_node != None):
        new_sentence += curr_node.get_data()
        curr_node = curr_node.get_next()
     
    return new_sentence

word_list=LinkedList2()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result=create_new_sentence(word_list)
# print(result)

class Child:
    def __init__(self,name,item_to_perform):
        self.__name=name
        self.__item_to_perform=item_to_perform

    def __str__(self):
        return(self.__name+" "+self.__item_to_perform)

    def get_name(self):
        return self.__name

    def get_item_to_perform(self):
        return self.__item_to_perform

class Performance:
    def __init__(self, children_list):
        self.children_list = children_list
        
    def get_children_list(self):
        return self.children_list
        
    def count_children(self):
        count = 0
        curr_node = self.children_list.get_head()
        while (curr_node != None):
            count += 1
            curr_node = curr_node.get_next()
        return count
    
    # Used to change the position of the child passed as the
    # argument to the middle position
    def change_position(self, child):
        child_middle_pos = self.count_children() // 2 + 1
        count = child_middle_pos
        middle_node = None
        
        curr_node = self.children_list.get_head()
        while True:
            middle_node = curr_node
            curr_node = curr_node.get_next()
            count -= 1
            
            if (count == 0):
                break
        
        middle_child_name = middle_node.get_data()
        self.children_list.insert(child, middle_child_name)
        
        second_node = self.children_list.get_head().get_next()
        self.children_list.head = second_node
    
    def add_new_child(self, child):
        new_node = Node2(child)
        tail = self.children_list.get_tail()
        tail.set_next(new_node)
        self.children_list.tail = new_node

child1=Child("Rahul","solo song")
child2=Child("Sheema","Dance")
child3=Child("Gitu","Plays Flute")
child4=Child("Tarun","Gymnastics")
child5=Child("Tom","MIME")

#Add different values to the list and test the program
children_list=LinkedList2()
children_list.add(child1)
children_list.add(child2)
children_list.add(child3)
children_list.add(child4)
children_list.add(child5)
performance=Performance(children_list)
# print("The order in which the children would perform:")
# performance.get_children_list().display()
# print()
# print("After Rahul's performance, the schedule would change to:")
# performance.change_position(child1)
# performance.get_children_list().display()
# print()
# child6=Child("Swetha","Vote of Thanks")
# print("After Swetha has joined, the schedule is:")
# performance.add_new_child(child6)
# performance.get_children_list().display()

# Remove duplicate numbers from linked list
def remove_duplicates(duplicate_list):
    ref_node = duplicate_list.get_head()
    ref_data = ref_node.get_data()
    curr_node = duplicate_list.get_head()
    
    while(curr_node != None):
        # tail
        if (curr_node.get_data() == duplicate_list.get_tail().get_data()):
            duplicate_list.set_tail(ref_node)
            break
        
        if (curr_node.get_data() == ref_data):
            curr_node = curr_node.get_next()
            continue
        else:
            ref_node.set_next(curr_node)
            ref_node = curr_node
            curr_node = curr_node.get_next()
    
    return duplicate_list

duplicate_list=LinkedList2()
duplicate_list.add(30)
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

# remove_duplicates(duplicate_list).display()

# Allocation and De-allocation table
class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList2()
    
    def get_occupied_table_list(self):
        return self.__occupied_table_list.display()
    
    # allocate the table that is the smallest non-occupied
    def allocate_table(self):
        min_avail = 1
        curr_table = self.__occupied_table_list.get_head()
        while (curr_table != None):
            if curr_table.get_data() == min_avail:
                min_avail += 1
                curr_table = curr_table.get_next()
            else:
                break
        
        if (min_avail == 10):
            self.__occupied_table_list.add(min_avail)
        elif (min_avail == 1):
            if (self.__occupied_table_list.get_head() == None):
                self.__occupied_table_list.head = Node2(min_avail)
            else:
                new_table = Node2(min_avail)
                new_table.set_next(self.__occupied_table_list.get_head())
                self.__occupied_table_list.set_head(new_table)
        elif (min_avail > 1 and min_avail < 10):
            self.__occupied_table_list.insert(min_avail, min_avail-1)
        
        print("Table allocated:", min_avail)

 
    def deallocate_table(self, table_number):
        self.__occupied_table_list.delete(table_number)

bakehouse = BakeHouse()
# bakehouse.allocate_table()
# bakehouse.allocate_table()
# bakehouse.allocate_table()
# bakehouse.allocate_table()
# bakehouse.allocate_table()
# bakehouse.deallocate_table(1)
# bakehouse.deallocate_table(4)

# print()
# bakehouse.get_occupied_table_list()
# print()
#
# bakehouse.allocate_table()
# bakehouse.get_occupied_table_list()
#
# print()
# bakehouse.allocate_table()
# bakehouse.get_occupied_table_list()

# Reverse Linked List
def reverse_linkedlist(reverse_list):
    head = reverse_list.get_head()
    tail = reverse_list.get_tail()
    count = 0
    
    curr = head
    while(curr != None):
        count += 1
        curr = curr.get_next()
    
    newList = LinkedList2()
    for i in range (count):
        node_to_add = head
        for k in range (count-i-1):
            node_to_add = node_to_add.get_next()
        newList.add(node_to_add.get_data())
    
    return newList

reverse_list=LinkedList2()
reverse_list.add(1)
reverse_list.add(2)
reverse_list.add(3)
reverse_list.add(4)
reverse_list.add(5)
reversed_linkedlist=reverse_linkedlist(reverse_list)
# reversed_linkedlist.display()


# TRAIN AND COMPARTMENT QUESTION
class Compartment:
    def __init__(self,compartment_name,no_of_passengers,total_seats):
        self.__compartment_name=compartment_name
        self.__no_of_passengers=no_of_passengers
        self.__total_seats=total_seats

    def get_compartment_name(self):
        return self.__compartment_name

    def get_no_of_passengers(self):
        return self.__no_of_passengers

    def get_total_seats(self):
        return self.__total_seats

class Train:
    def __init__(self,train_name,compartment_list):
        self.__train_name=train_name
        self.__compartment_list=compartment_list

    def get_train_name(self):
        return self.__train_name
    
    def get_compartment_list(self):
        return self.__compartment_list
    
    def count_compartments(self):
        count=0
        curr = self.__compartment_list.get_head()
        while (curr != None):
            count += 1
            curr = curr.get_next()
        return count
    
    def check_vacancy(self):
        count=0
        curr = self.__compartment_list.get_head()
        while (curr != None):
            no_pass = curr.get_data().get_no_of_passengers()
            no_seats = curr.get_data().get_total_seats()
            percent_vacant = (no_seats - no_pass) / no_seats * 100
            if (percent_vacant > 50):
                count += 1
            curr = curr.get_next()
        return count

#Use different values for compartment and test your program
compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
compartment_list=LinkedList2()
compartment_list.add(compartment1)
compartment_list.add(compartment2)
compartment_list.add(compartment3)
compartment_list.add(compartment4)
compartment_list.add(compartment5)
train1=Train("Shatabdi",compartment_list)
count=train1.count_compartments()
# print("The number of compartments in the train:",count)
# vacancy_count=train1.check_vacancy()
# print("The number of compartments which have more than 50% vacancy:",vacancy_count)