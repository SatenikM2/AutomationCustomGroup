#1*. Write a Python program that accepts a word from the user and reverse it.
user = "Satenik"
print(len(user))
print(user[-7:])
print(user[::-1])

#2. Write a Python program to count that user inputed number is even or odd.

#number = int(input("Please write a number: "))
#result = number % 2
#if result == 0:
	#print("The number is even")
#else:
	#print("The number is odd")


#3. Write a Python program to find the inputed number from 100 to 400 (both included).

#var1 = int(input("The number from 100 to 400: "))
#if 100 <= var1  or var1 <= 400:
	#print("True")
#else:
	#print("False")


#4. Write a Python program that get 2 numbers from user and retur Biggest, Median, Sum, Multiply, Divide and Subtract
x=5
y=2

#biggest
if x > y:
	print ("The 5 is biggest then 2")
else:
	print("The 5 isn't begges then 2")

# Median
median=(x+y)/2
print("the median  5 and 2 is: " , median)

# +
result=x+y
print("5", "+", "2", "=", result)

# -
result=x-y
print("5", "-", "2", "=", result)

# /
result=x/y
print("5", "/", "2", "=", result)

# **
result=x**y
print("5", "**", "2", "=", result)

# %
result=x%y
print("5", "%" , "2", "=", result)


#5. Write a Python program to get next day of a given date.
	#Expected Output:

	#Input a year: 2016
    #Input a month [1-12]: 8
	#Input a day [1-31]: 23
	#The next date is [yyyy-mm-dd] 2016-8-24
year=int(input("year"))
monthlen = 12
month = int(input("Input a month [1-12]: "))
day = int(input('Input a day' :))
if month


# year=int(input("year"))
#
# monthlen=12
# month=int(input("Input a month [1-12]: "))
# if "month == 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12" :
# 	print(monthlen == 31)
# elif month==4 or month==6 or month==9 or month==11:
#     print(monthlen==30)
# elif month == 2:
# 	print(monthlen == 28)
# else:
# 	print(monthlen ==30)
#
# day = int(input("Input a day : "))
# if day < monthlen:
# 	print(year, month, day + 1)
# if "day == monthlen" and "month == 12":
# 	print(year+ 1, 1,1)
# if "day == monthlen" and monthlen < 12:
#     print(year, month+1, 1)
# else:
# 	print("the next day is", year ,"-", month , "-",day)

