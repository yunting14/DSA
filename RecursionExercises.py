# https://www.cs.cornell.edu/courses/cs2110/2014sp/L07-Recursion/recursion_practice.pdf

'''
Q1: Compute the Factorial of a number N. Fact(N) = N × (N − 1)···1.
'''
def factorial(n):
    if n==1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

'''
Q2: Compute the sum of natural numbers until N.
'''
def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)

print(sum(5))

'''
Q3: Write a function for mutliply(a,b), where a and b are both positive integers, 
but you can only use the + or − operators.
'''
def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

def multiply_recursive(a,b):
    if b==1:
        return a
    return a + multiply_recursive(a, b-1)

print(multiply(3,2))
print(multiply_recursive(3,2))

'''
Q4: In the lecture, we discussed a method to raise a double 
to an integer power. In this question, write a recursive 
function that allows raising to a negative integer power as well.
'''
def power(num, p):
    if p==0:
        return 1
    if p==1:
        return num
    
    if p > 0:
        return num * power(num, p-1)
    else:
        return 1/num * 1/power(num, -p-1)
    
print(power(3,-2))

'''
Q5: Find Greatest Common Divisor (GCD) of 2 numbers using recursion.
'''
def greatest_common_divisor(num1, num2):
    divisor = 0
    if num1>num2:
        divisor = num2
    else:
        divisor = num1
    
    gcm = 0
    for i in range(divisor, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcm = i
            break
    return gcm

def greatest_common_divisor_recursive(num1, num2):
    if (num2 == 0):
        return num1
    
    return greatest_common_divisor_recursive(num2, num1%num2)

print(greatest_common_divisor(12,6))

'''
Q6: Write a recursive function to reverse a string. Write a recursive function to reverse the words in a string,
i.e., ”cat is running” becomes ”running is cat”.
'''
def reverse_string(str1):
    arr = str1.split(" ", 1)
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return
    
    return reverse_string(arr[-1]) + " " + arr[0]

print(reverse_string("cat is running"))


'''
Q7: A word is considered elfish if it contains the letters: 
e, l, and f in it, in any order. For example, we would say that the 
following words are elfish: whiteleaf, tasteful, unfriendly, and waffles, 
because they each contain those letters. Write a predicate function called 
"elfish" that, given a word, tells us if that word is elfish or not.
'''
def elfish(word):
    
    if word in ["e", "f", "l"]:
        arr = word.split(word, 1)
        return arr[0] + elfish(arr[1])
    else:
        return

'''
https://codingbat.com/prob/p107330
''' 
def bunnyears(num_of_bunnnies):
    if num_of_bunnnies == 0:
        return 0
    
    count = 0
    if num_of_bunnnies % 2 == 0:
        count = 3
    else:
        count = 2
    
    return count + bunnyears(num_of_bunnnies-1)

print(bunnyears(5))

'''
https://codingbat.com/prob/p194781
'''
def triangle(no_of_rows):
    if no_of_rows==0:
        return 0
    if no_of_rows==1:
        return 1
    
    return no_of_rows + triangle(no_of_rows-1)

print(triangle(4))

'''
https://codingbat.com/prob/p163932
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
'''
def sumDigits(number):
    if number == 0:
        return 0
    
    digit = number % 10
    next = number // 10

    return digit + sumDigits(next)

print(sumDigits(49))

'''
https://codingbat.com/prob/p101409
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops).

count7(717) → 2
count7(7) → 1
count7(123) → 0
'''
def count7(num):
    if num == "":
        return 0
    
    count = 0
    if str(num)[0] == "7":
        count = 1

    return count + count7(str(num)[1:])

print(count7(7777))

'''
https://codingbat.com/prob/p192383
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. 

count8(8) → 1
count8(818) → 2
count8(8818) → 4
'''
def count8(number):
    if number == 0:
        return 0
    
    num_string = str(number)
    count=0
    
    if len(num_string) == 1:
        if num_string[-1] == "8":
            count = 1
        else:
            count = 0

    if len(num_string) > 1:
        if num_string[-1] == "8" and num_string[-2] == "8":
            count = 2
        elif num_string[-1] == "8":
            count = 1

    next = number // 10
    return count + count8(next)

print(count8(88)) # 3
# print(count8(8818)) # 4

'''
https://codingbat.com/prob/p170371
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
'''
def countX(text):
    if len(text) == 0:
        return 0
    
    count = 0
    if text[0] == "x":
        count = 1
    
    return count + countX(text[1:])

print(countX("hi"))

'''
https://codingbat.com/prob/p184029
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.


countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
'''
def countHi(text):
    if len(text) == 0:
        return 0
    
    hi_index = text.find("hi")
    count = 0
    if hi_index == -1:
        return 0
    else:
        count = 1
    
    next = text[hi_index+2:]
    return count + countHi(next)

print(countHi("xhixhix"))

'''
https://codingbat.com/prob/p101372
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.


changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
'''
def changeXY(text):
    if len(text) == 0:
        return
    
    if len(text) == 1:
        if text == "x":
            return "y"
        else:
            return text
    
    return changeXY(text[0]) + changeXY(text[1:])

print(changeXY("codex"))

'''
https://codingbat.com/prob/p170924
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
'''
def changePi(text):
    pi_index = text.find("pi")
    if pi_index == -1:
        return text
    
    text = text[:pi_index] + "3.14" + text[pi_index+2:]
    return changePi(text)

print(changePi("pip"))

'''
https://codingbat.com/prob/p118230
Given a string, compute recursively a new string where all the 'x' chars have been removed.

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
'''
def removeX(text):
    x_index = text.find("x")
    if x_index == -1:
        return text
    
    text = text[:x_index] + text[x_index+1:]
    return removeX(text)

print(removeX("xabc"))

'''
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
'''
def array6(num_list, index=0):
    if index == len(num_list):
        return False
    
    if num_list[index] == 6:
        return True
    
    return array6(num_list, index+1)

nums = [1,6,4]
print(array6(nums))

'''
https://codingbat.com/prob/p173469
Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
'''
def arrayTimes10(num_list, index=0):
    if index == len(num_list)-1:
        return False
    
    if num_list[index] * 10 == num_list[index+1]:
        return True
    
    return arrayTimes10(num_list, index+1)

nums = [3, 4]
print(arrayTimes10(nums))

'''
https://codingbat.com/prob/p183394
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
'''
def allStar(text):
    if len(text) <= 1:
        return text
    
    return text[0] + "*" + allStar(text[1:])

print(allStar("abc"))

'''
https://codingbat.com/prob/p158175
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".


pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
'''
def pairStar(text):
    if len(text) <= 1:
        return text
    
    if text[0] == text[1]:
        result = text[0] + "*" + text[1]
        next = text[2:]
    else:
        result = text[0]
        next = text[1:]

    return result + pairStar(next)

print(pairStar("xxyy"))

'''
https://codingbat.com/prob/p105722
Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
'''
def endX(text):
    if text == "":
        return text
    
    if text[0] == "x":
        return endX(text[1:]) + "x"
    else:
        return text[0] + endX(text[1:])

print(endX("xxre"))

'''
https://codingbat.com/prob/p154048
We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.

countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
'''
def countPairs(text):
    if text == "":
        return 0
    
    if text[1:].find(text[0]) == -1:
        return 0 + countPairs(text[1:])
    else:
        return 1 + countPairs(text[1:])
    
print(countPairs("axaxa"))

'''
https://codingbat.com/prob/p161124
Count recursively the total number of "abc" and "aba" substrings that appear in the given string.

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
'''
def countAbc(text):
    abc_index = text.find("abc")
    aba_index = text.find("aba")
    if abc_index == -1 and aba_index == -1:
        return 0
    elif abc_index >= 0:
        return 1 + countAbc(text[abc_index+3:])
    elif aba_index >= 0:
        return 1 + countAbc(text[aba_index+3:]) 

def countAbc_withoutFind(text):
    if len(text) <= 2:
        return 0
    
    if text[:3] != "abc" and text[:3] != "aba":
        a_index = text.find("a")
        return 0 + countAbc_withoutFind(text[a_index:])
    elif text[:3] == "abc" or text[:3] == "aba":
        return 1 + countAbc_withoutFind(text[3:])
    
print("Count abc and aba - 1:",countAbc("abcxxabcaba"))
print("Count abc and aba - 2:",countAbc_withoutFind("abcxxabcaba"))

'''
Given a string, compunte recursively (no loops) the number of "11" substrings in the string. The "11" substrings should ot overlap.

count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
'''
def count11(text):
    index_11 = text.find("11")
    if index_11 == -1:
        return 0
    else:
        return 1 + count11(text[index_11+2:])
    
print(count11("abc11x11x11"))

'''
Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".

stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
'''
def stringClean(text):
    if len(text) <= 1:
        return text

    if text[0] == text[1]:
        return stringClean(text[1:])
    else:
        return text[0] + stringClean(text[1:])
    
print(stringClean("travveller"))

'''
Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
'''
def countHi2(text):
    hi_index = text.find("hi")
    if hi_index == -1:
        return 0
    
    if text[hi_index-1] == "x":
        return 0 + countHi2(text[hi_index+2:])
    else:
        return 1 + countHi2(text[hi_index+2:])
    
print(countHi2("xhixhi"))

'''
Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".

parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
'''
def parenBit(text):
    if text == "":
        return ""
    
    if text[0] != "(":
        return parenBit(text[1:])
    
    if text[-1] != ")":
        return parenBit(text[:-1])
    else:
        return text
    
print(parenBit("x(hello)"))

'''
https://codingbat.com/prob/p183174
Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.

nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
'''
def nestParen(text):
    if text == "":
        return True
    
    if text[0] == "(" and text[-1] == ")":
        return nestParen(text[1:-1])
    else:
        return False
    
print(nestParen("x(())x"))

'''
https://codingbat.com/prob/p186177
Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.

strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
'''
def strCount(text, sub):
    if text == "":
        return 0

    if text[:len(sub)] == sub:
        return 1 + strCount(text[len(sub)+1:], sub)
    else:
        return 0 + strCount(text[1:], sub)
    
print(strCount("catcowcat", "dog"))

'''
https://codingbat.com/prob/p118182
Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true
'''
def strCopies(text, sub, n):
    if text == "":
        if n==0:
            return True
        else:
            return False
    
    if text[:len(sub)] == sub:
        n-=1
        return strCopies(text[len(sub)+1:], sub, n)
    else:
        return strCopies(text[1:], sub, n)
print(strCopies("catcowcat", "cow", 2))

'''
https://codingbat.com/prob/p195413
Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.

strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
'''
def strDist(text, sub):
    if text[:len(sub)] == sub and text[-len(sub):] == sub:
        return len(text)
    
    if text[:len(sub)] != sub:
        return strDist(text[1:], sub)
    else: # front is ok
        if text[-len(sub):] != sub:
            return strDist(text[:-1], sub)

print(strDist("appletreeisfullofapplesthatcanbemadeintoapplejuice", "apple"))

'''
https://codingbat.com/prob/p145416
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target?

groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false
'''
def groupSum(start_index, num_list, target):
    if start_index >= len(num_list):
        if target == 0:
            return True
        else:
            return False
    
    # use the int that we are on --> minus the int
    new_target = target - num_list[start_index]
    if (groupSum(start_index+1, num_list, new_target)):
        return True
    
    # don't use the int we are on --> don't minus the int
    if (groupSum(start_index+1, num_list, target)):
        return True
    
    return False

print(groupSum(0, [2, 4, 8], 9))

'''
https://codingbat.com/prob/p199368
Given an array of ints, is it possible to choose a group of some of the ints, 
beginning at the start index, such that the group sums to the given target? 
However, with the additional constraint that all 6's must be chosen. (No loops needed.)

groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
'''
def groupSum6(start, nums, target):
    if start >= len(nums):
        if target == 0:
            return True
        else:
            return False

    # if the number is 6, use it. minus from target
    if nums[start] == 6:
        return groupSum6(start+1, nums, target-6)
    else:
        # num is not 6. use this num and minus from target
        if groupSum(start+1, nums, target-nums[start]):
            return True
        
        # don't use this num, skip to the following one
        if groupSum6(start+1, nums, target):
            return True
    
    # # num is not 6. use this num and minus from target
    # if groupSum(start+1, nums, target-nums[start]):
    #     return True
    
    # # don't use this num, skip to the following one
    # if groupSum6(start+1, nums, target):
    #     return True
    return False
print("Group Sum 6:",groupSum6(0, [5, 6, 2], 7)) # prints True when it is supposed to be false
    
    
