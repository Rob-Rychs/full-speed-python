# Solutions for full-speed-python.
#TODO: Need to Condense + review answers + add question headers for first 6 chapters

>>> 3/2
1.5
>>> 3//2
1
>>> (3//2)
1
>>> 1.5/2
0.75
>>> 3%2
1
>>> 3**2
9
>>> (2+4)+(4+8+9)+(12+(14/6)+15)
56.333333333333336
>>> pi = 3.1415
>>> (4/3)*pi*(5**3)
523.5833333333333
>>> 1%1
0
>>> 1%2
1
>>> 5%2
1
>>> 1%2
1
>>> 20%2
0
>>> (60/7)%2
0.5714285714285712
>>> x = .1
>>> y = 1
>>> x < 1/3 < y
True
>>> s = "abc"
>>> len(s)
3
>>> s[0]+"aa"
'aaa'
>>> s
'abc'
>>> s[0]
'a'
>>> s[0]+'aa'+s[1]+'bb'+s[2]+'cc'
'aaabbbccc'
>>> s = "aaabbbccc"
>>> s.rfind('b')
5
>>> s.rindex('b')
5
>>> s.find('b')
3
>>> s.find('ccc')
6
>>> s.replace('a', 'X')
'XXXbbbccc'
>>> s.replace('a', 'a')
'aaabbbccc'
>>> s.replace('a', 'X', 1)
'Xaabbbccc'
>>> s = "aaa bbb ccc"
>>> s.swapcase()
'AAA BBB CCC'
>>> s.swapcase().replace('BBB', 'bbb')
'AAA bbb CCC'
>>> l = [1,4,9,10,23]
>>> l[1:3]
[4, 9]
>>> l[3:5]
[10, 23]
>>> l.append(90)
>>> l
[1, 4, 9, 10, 23, 90]
>>> sum(l[0:len(l)])
137
>>> sum(l[0:len(l)])/len(l)
22.833333333333332
>>> l[1:3]
[4, 9]
>>>
>>> l
[1, 4, 9, 10, 23, 90]
>>> squares = [x*x for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [x*x for x in range(20)]
>>> squares = [x*x for x in range(20)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> squares = [x*x for x in range(20) if x%2 == 0]
>>> squares
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
>>> squares = [x*x for x in range(20) if x%2 == 1]
>>> squares
[1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
>>> squares = [x*x for x in range(20) if x%2 == 0]
>>> sum
<built-in function sum>
>>> (squares)
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
>>> sum(squares)
1140
>>> squares = [x*x for x in range(20) if x%2 == 0 and x%3 !=0]
>>> squares
[4, 16, 64, 100, 196, 256]
>>> import math
>>> math.cos
<built-in function cos>
>>> math.cos(0.0)
1.0
>>> math.gcd(15,21)
3
>>> math.gcd(152,200)
8
>>> math.gcd(1988,9765)
7
>>> math.log2(1)
0.0
>>> math.log2(2)
1.0
>>> math.log2(6)
2.584962500721156
>>> def trig_num1():
...     num = input('pick a number: ')
...     num = int(num)
...     sine = math.sin(num)
...     print(sine)
...
>>> trig_num1()
pick a number: 4
-0.7568024953079282
>>> def trig_num():
...     num = input('pick a number: ')
...     num = int(num)
...     sine = math.sin(num)
...     cose = math.cos(num)
...     tang = math.tan(num)
...     print(sine, cose, tang)
...
>>> trig_num()
pick a number: 90
0.8939966636005579 -0.4480736161291701 -1.995200412208242
>>> def add_two(x,y):
...     x = int(x)
...     y = int(y)
...     summ = x + y
...     return summ
...
>>> add_two(7,7)
14
>>> def add_three(x,y,z):
...     summ = x+y+z
...     return summ
...
>>> add_three(1,2,3)
6
>>> def greatest(x,y):
...     if x > y:
...             return x
...     elif y > x:
...             return y
...
>>> greatest(1,2)
2
>>> def is_divisible(a,b):
...     if a%b == 0:
...             return True
...     else:
...             return False
...
>>> is_divisible(20,3)
False
>>> def average(x):
...     return sum(x[0:len(x)])/len(x)
...
>>> average([1,2,3,4,5])
3.0
>>> def factorial(x):
...     if x == 0:
...             return 1
...     else:
...             return x * factorial(x-1)
...
>>> factorial
<function factorial at 0x10394ed90>
>>> factorial(10)
3628800
>>> factorial(3)
6
>>> sum_n_integers(n):
  File "<stdin>", line 1
    sum_n_integers(n):
                     ^
SyntaxError: invalid syntax
>>> def sum_n_integers(n):
...     if n == 0:
...             return 0
...     else:
...             return n + (n-1)
...
>>> sum_n_integers(3)
5
>>> def fib(n):
...     if n == 0:
...             return 0
...     elif n == 1:
...             return 1
...     else:
...             return fib(n-1) + fib(n-2)
...
>>> fib(10)
55
>>> fib(1)
1
>>> fib(2)
1
>>> fib(0)
0
>>> fib(3)
2
>>> fib(12)
144
>>> fib(4)
3
>>> fib(1)
1
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3
>>> fib(5)
5
>>> fib(6)
8
>>> fib(7)
13
>>> fib(8)
21
>>> fib(9)
34
>>> def add(x):
...     sum = 0
...     for num in x:
...             sum = sum + num
...     print(sum)
...
>>> add([1,2,3,4,5])
15
>>> def maximum(x):
...     max = 0
...     for num in x:
...             if num > max:
...                     max = num
...     return max
...
>>> maximum([100,2,5])
100


PROBLEM#6.3
>>> def maximuml(x):
...     max = 0
...     position = 0
...     for i, value in enumerate(x):
...             if value > max:
...                     max = value
...                     position = i
...     return [max, position]
...
>>> maximuml([100, 4, 4,70, 5400])
[5400, 4]

PROBLEM#6.4
#############

QUESTIONS (problems using list.reverse() inside a function and getting the list to RETURN, still does the reverse though, see below. implemented also with new_reverse, see below)

>>> def reverse_list(x):
...     return x.reverse
...
>>> reverse_list([1,2,3])
<built-in method reverse of list object at 0x1040652c8>
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> value(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'value' is not defined
>>> evaluate(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'evaluate' is not defined
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> def reverse_list(x):
...     y = x.reverse()
...     return y
...
>>> reverse_list([1,2,3])
>>>
>>> def reverse_list(x):
...     return x.reverse()
...
>>> reverse_list([1,2,3])
>>> def reverse_list(x):
...     newlist = x.reverse()
...     return newlist
...
>>> reverse_list([1,2,3])
>>> list = [1,2,3]
>>> list
[1, 2, 3]
>>> reverse_list(list)
>>> list
[3, 2, 1]
>>>
>>> def new_reverse(x):
...     y = []
...     for v in x:
...             y.append(v)
...     return y
...
>>> new_reverse([1,2,3])
[1, 2, 3]
>>> def new_reverse(x):
...     y = []
...     for v in x:
...             y.insert(v)
...     return y
...
>>> new_reverse([1,2,3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in new_reverse
TypeError: insert() takes exactly 2 arguments (1 given)
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x=[1,2,3]
>>> new_reverse(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in new_reverse
TypeError: insert() takes exactly 2 arguments (1 given)
>>> def new_reverse(x):
...     y = []
...     for v in x:
...             y.insert(0,v)
...     return y
...
>>> x
[1, 2, 3]
>>> new_reverse(x)
[3, 2, 1]
>>>

PROBLEM#6.5
##############
>>> def is_sorted(x):
...     y = x.copy()
...     x.sort()
...     if y == x:
...             return True
...     else:
...             return False
...
>>> x
[1, 2, 3]
>>> is_sorted(x)
True
>>> x = [3,2,1]
>>> is_sorted(x)
False
>>>

PROBLEM#6.6
###############
>>> def is_sorted_desc(x):
...     y = x.copy()
...     x.sort(reverse=True)
...     if y == x:
...             return True
...     else:
...             return False
...
>>> x
[1, 2, 3]
>>> is_sorted_desc(x)
False
>>> reverse(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reverse' is not defined
>>> x = [3,2,1]
>>> x
[3, 2, 1]
>>> is_sorted_desc(x)
True
>>>

PROBLEM#6.7
################
(Had to research a snippet on SO: https://stackoverflow.com/questions/1541797/check-for-duplicates-in-a-flat-list  Still missing a double for loop implementation...)

>>> def has_duplicates(x):
...     for i in x:
...             for i+1 in x:
...
  File "<stdin>", line 4

    ^
IndentationError: expected an indented block
>>> def has_duplicates(x):
...     return len(x) != len(set(x))
...
>>> x
[3, 2, 1]
>>> has_duplicates(x)
False
>>> x = [1,2,3,4,5,5]
>>> has_duplicates(x)
True
>>>

PROBLEM#6.8 (while problem)
###############################
(COME BACK TO IT)

PROBLEM#7.1
##################

>>> ages = {
...     "Peter": 10,
...     "Isabel": 11,
...     "Anna": 9,
...     "Thomas": 10,
...     "Bob": 10,
...     "Joseph": 11,
...     "Maria": 12,
...     "Gabriel": 10,
... }
>>> len(ages)
8
>>>

PROBLEM#7.2
#######################

>>> ages = {
...     "Peter": 10,
...     "Isabel": 11,
...     "Anna": 9,
...     "Thomas": 10,
...     "Bob": 10,
...     "Joseph": 11,
...     "Maria": 12,
...     "Gabriel": 10,
... }
>>> def average_of(ages):
...     sum = 0
...     for name, age in ages.items():
...             sum = sum + age
...     return sum/len(ages)
...
>>> average_of(ages)
10.375

PROBLEM#7.3
###################

>>> ages = {
...     "Peter": 10,
...     "Isabel": 11,
...     "Anna": 9,
...     "Thomas": 10,
...     "Bob": 10,
...     "Joseph": 11,
...     "Maria": 12,
...     "Gabriel": 10,
... }
>>> def oldest(ages):
...      oldest = 0
...      oldest_name = ''
...      for name, age in ages.items():
...              if age > oldest:
...                      oldest = age
...                      oldest_name = name
...      return oldest_name
...
>>> oldest(ages)
'Maria'

PROBLEM#7.4
###################
(not working!!! Need to find out why)

def new_ages(ages, n):
	n_ages = ages.copy()
	for name, age in n_ages.items():
		age + n
	return n_ages

>>> new_ages(ages, 10)
{'Peter': 10, 'Isabel': 11, 'Anna': 9, 'Thomas': 10, 'Bob': 10, 'Joseph': 11, 'Maria': 12, 'Gabriel': 10}

PROBLEM#7.5 (sub-directories0.1)
####################################

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
>>> len(students)
3

PROBLEM#7.6 (sub-directories0.2) (this one took me a while, remember dicts are not hashable)
###################################

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
def avg_age(students):
    sum = 0
    for x in students:
        name = x
        sum = sum + students[name]['age']
    return sum/len(students)
>>> avg_age(students)
10.0

PROBLEM#7.7 (sub-dictionaries0.3)
#####################################

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
def find_students(students, x):
    lst = []
    for n in students:
        if students[n]['address'] == x:
            lst.append(n)
    return lst
>>> find_students(students, 'Lisbon')
['Peter', 'Anna']

PROBLEM#8.1 (have not checked this code yet, getting tabs/spaces errors)
#############

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return height() * width()

    def circumference(self):
        return (2*height()) + (2*width())

    def __str__(self):
        return (self.x1, self.y1)(self.x2, self.y2)

