#lex_auth_0127667360846643203336

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

# last in last out (top -largest, bottom - smallest)
def merge_stack(stack1,stack2):
    list = []
    for i in range(stack1.get_max_size()+1):
        num1 = stack1.pop()
        if num1 != None: 
            list.append(num1)
    for k in range(stack2.get_max_size()+1):
        num2 = stack2.pop()
        if num2 != None: 
            list.append(num2)
    
    # sort
    for j in range(len(list)-1):
        swapped = False
        for l in range(len(list)-j-1):
            if list[l] > list[l+1]:
                temp = list[l]
                list[l] = list[l+1]
                list[l+1] = temp
                swapped = True
        if swapped == False:
            break
    
    new_stack = Stack(len(list))
    for data in list:
        new_stack.push(data)
    
    return new_stack

#Pass different values to the function and test your program
stack2=Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)

stack1=Stack(4)
stack1.push(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)

print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack=merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()