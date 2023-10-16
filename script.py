1.
def find_short(s):
    return (min(map(len, s.split())))
2. 
def string_to_array(s):
    return s.split(" ")
3. 
def longest(a1, a2):
    s="".join(set(a1).union(set(a2)))
    return ''.join(sorted(s))
4. 
def summation(num):
    return (num * (num +1) // 2)
5. 
def remove_char(s):
    return (s [1:-1])
6.
def greet():
    return("hello world!")
7. 
def say_hello(name):
    return "Hello, " + name
8. 
def reverse_seq(n):
    return list(range(n, 0, -1))
9. 
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
10. 
def square(n):
    return n*n
11. 
def find_uniq(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i
12. 
def get_volume_of_cuboid(length, width, height):
    return length*width*height
13.
def min_max(lst):
    return [min(lst), max(lst)]
14.
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
15.
def solution(s):
    new=""
    for letter in s:
        if ord(letter) in range(65,91):
            new+=" "
        new+=letter
    return new
16.
def square_sum(numbers):
    a=[]
    for i in range(len(numbers)):
        a.append(numbers[i]**2)
    return sum(a)
17.
def find_it(seq):
    return [x for x in set(seq) if seq.count(x)%2!=0][0]
18.
def simple_multiplication(number) :
    return(number*8 if number%2 == 0 else number*9)
19.
def remove_every_other(my_list):
    return my_list[::2]
20.
def to_alternating_case(string):
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
21.
def get_sum(a,b):
    if a == b: 
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
22.
def powers_of_two(n):
    powers = []
    for i in range (n+1):
        powers.append(2**i)
    return powers
23.
def between(a,b):
    return [i for i in range(a, b+1)]
24.
def move(position, roll):
    return (position + (2*roll))
25.
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
26.
def is_even(n): 
    return n % 2 == 0
27.
def high_and_low(numbers):
    a = list(map(int, numbers.split()))
    b = [max(a), min(a)]
    return (' '.join(map(str, b)))
28.
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - son_years_old * 2)
29.
def maps(a):
    return [x * 2 for x in a]
30.
def better_than_average(class_points, your_points):
    sum_points=sum(class_points)+your_points
    len_points=len(class_points)+1
    average_point=sum_points/len_points
    if average_point>your_points:
        return False
    else:
        return True
31.
def greet(name):
    #Good Luck (like you need it)
    return "Hello, " + name + " how are you doing today?"
32.
def remove_exclamation_marks(s):
    return s.replace("!", "")
33.
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
34.
def abbrev_name(name):
    name = name.upper()
    lst = name.split(" ")  
    return lst[0][0] + "." + lst[1][0]
35.
def area_or_perimeter(l , w):
    if (l != w):
        return (2*l)+(2*w)
    else:
        return l*w
36.
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)
37.
def find_average(numbers):
    return sum(numbers)/len(numbers) if numbers else 0
38.
def double_integer(i):
    return i * 2
39.
def no_space(x):
    return x.replace(" ","")
40.
def opposite(number):
    return - number
41.
def find_smallest_int(arr):
    return min(arr)
42.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
43.
def number_to_string(num):
   return str(num)
44.
def make_negative( number ):
    return -abs( number )
45.
def solution(string):
    reverse = ""
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    return reverse  
46.
def make_upper_case(s):
    return s.upper()
47.
def positive_sum(arr):
    sum = 0
    for m in arr:
        if m > 0:
            sum = sum + m
    return sum    
48.
from operator import xor
def lovefunc( flower1, flower2 ):
    return xor(flower1 % 2 == 0, flower2 % 2 == 0)
49.
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else: 
        return "Odd"
50.
def century(year):
    if year % 100 != 0:
        return (year // 100) + 1
    else:
        return (year // 100)
51.
def past(h, m, s):
    return s * 1000 + m * 60 * 1000 + h * 60 * 60 * 1000
52.
def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    else:
        return 0
53.
def boolean_to_string(b):
    return str(b)
54.
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum    
55.



















