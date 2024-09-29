# PYTHON

# Easy(1P)

# 1. 

def maxnum(lst):
    return max(lst)

# 2. 

def counter(lst):
    result = True
    for num in lst:
        if lst.count(num) > 1:
            result = False
    return result

# 3.
list = [1,2,3,4,5,6,7,8]
list0 = []
for i in range (len(list)):
    if list[i] % 2 == 0:
        list0.append(list[i])

print(list0)

# 4.

def even(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result    

# 5. 

def plus1():
    input1 = int(input("enter the number:  "))
    no1 = input1
    while input1 % no1 == 0:
       no1 += 1
    return input1 , " cant divide on" , no1


print(plus1())



# Hard(2P)
 	
# 1. 
def slice_string(s):
    return s[1::2]

result = slice_string("hello")

# 2. 

def check_even_length(lst):
    return len(lst) % 2 == 0

result = check_even_length([4, 6, 3, 7, 4, 9, 8]) 

# 3. 

def nth_smallest(lst, n):
    return sorted(lst)[n-1]

result = nth_smallest([3, 5, 8, 7, 2], 4)

# 4.

def goa(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

result = goa

# 5. 

def calculate_expression(s, indices):
    total = 0
    for i in indices:
        if s[i] == '+':
            total += i
        elif s[i] == '-':
            total -= i
    return total

result = calculate_expression("+-++----", [0, 1, 2, 1, 2, 3, 4])