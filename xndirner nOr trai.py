# print("1. Write a Python function to find the Max of three numbers?")
# def two_numbers(x,y):
#     if x > y:
#         return x
#     return y
# def three_numbers (x, y, z):
#     return two_numbers(x, two_numbers(y, z))
# print(three_numbers(1, 3, 6))


# print("2. Write a Python function to sum all the numbers in a list? /Sample List: (8, 2, 3, 0, 7)/ExpectedOutput: 20 ")
# def sum (numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
# print(sum((8,2,3,0,7)))

# print("3. Write a Python function to multiply all the numbers in a list.?")
# SampleList = (8, 2, 3, -1, 7)
# ExpectedOutput = -336
#
# def multiply_numbers(SampleList):
#     total = 1
#     for i in SampleList:
#         total *= i
#     return total

# SampleList = (8, 2, 3, -1, 7)
# print(multiply_numbers(SampleList))
#
# print("4. Write a Python program to reverse a string.?")
# ExpectedOutput = "dcba4321"
#
# def reverse_string (SampleString):
#     SampleString2 = " "
#     index = len(SampleString)
#     while index > 0:
#        SampleString2 += SampleString[index -1]
#        index = index -1
#     return SampleString2
#
#
# SampleString = "1234abcd"
# print(reverse_string(SampleString))
#
# print ("5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.")
#
# def factorial_number(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_number(n-1)
# n = int(input("Please input the number: "))
# print(factorial_number(n))
#
# print("6. Write a Python function to check whether a number falls in a given range. Go to the editor")

# def given_range(i):
#     if i in range(1, 10):
#         print(str(i), "is in range")
#     else:
#         print(str(i), " is not in range")
# given_range(13)

# print(" 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.")
#
#
# print("8 Write a Python function that takes a list and returns a new list with unique elements of the first list.")
# def unique_elemnts(samplelist):
#     x = []
#     for i in samplelist:
#         if i not in x:
#             x.append(i)
#     return x
#
# samplelist = [1,2,3,3,3,3,4,5]
# print(unique_elemnts(samplelist))
# print("9. Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor")
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself
# def prime_number(n):
#     if (n == 1):
#         return False
#     elif (n == 2):
#         return True
#     else:
#         for i in range (2,n):
#             if (n % 2==0):
#                 return False
#             return True
# print(prime_number(10))

# print("10. Write a Python program to print the even numbers from a given list.")
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# def even_numbers (Samplelist):
#     enum = []
#     for i in Samplelist:
#         if i % 2 == 0:
#             enum.append(i)
#     return enum
#
# Samplelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even_numbers(Samplelist))

# print("11. Write a Python program to calculate the length of a string. Go to the editor")
# def string_length(name):
#     count = 0
#     for char in name:
#         count += 1
#     return count
# name = "satenik"
# print(string_length(name))
#
# print("12 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.")
# def name_string(name):
#     if len(name) < 2:
#         return " "
#     return name[0:2] + name[-2:]
# name = "w3resource"
# # print(name_string(name))
# print("13 Write a Python program to sum all the items in a list.")
# def my_list(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i
#     return sum
# mylist = [1, 2, 3, 4, 5]
# print(my_list(mylist))

# print("14 Write a Python program to multiply all the items in a list.")
#
# def my_list(mylist):
#     sum = 1
#     for i in mylist:
#         sum *= i
#     return sum
# mylist = [1, 2, 3, 4]
# print(my_list(mylist))

# print("15 Write a Python program to get the largest number from a list.")
# def my_list_number(num1):
#     max = num1[0]
#     for i in num1:
#         if i > max:
#             max = i
#     return max
# num1 = [1,3,7,2]
# print(my_list_number(num1))
#
# print("16. Write a Python program to get the smallest number from a list. Go to the editor")
# def minimum (mylist2):
#     min =  mylist2[0]
#     for i in mylist2:
#         if i < min:
#             min = i
#     return min
# mylist2 = [1,3,-7,2]
# print(minimum(mylist2))

# print("17 Write a Python program to remove duplicates from a list.")
# def duplicate_list (number):
#     print(set(number))
#
# number = [1,2,3,3,2,1,1,1,5]
# duplicate_list(number)


# print("18. Write a Python program to check a list is empty or not.")
# def empty_list(mylist):
#     if not mylist:
#         print("List is empty")
#     else:
#         print("List is not empty:")
#
# mylist = []
# print(empty_list(mylist))
#
# print("19. Write a Python program to clone or copy a list. Go to the editor")
# list1 =  [1,2,3,5]
# mylist1 = list1
# print(mylist1)
# print(list1)
#
# print("20 Write a Python program to find the list of words that are longer than n from a given list of words.")
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))




