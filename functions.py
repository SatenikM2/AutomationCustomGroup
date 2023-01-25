c# https://www.w3schools.com/python/python_functions.asp
#
# 1. Write a function to multiply all the numbers in a given list
def foo(number1, number2, number3):
    print(number1 * number2 * number3)
foo(1, 2, 3)


# 2. Write a function that takes a list and returns a new list with unique elements of the first list
def my_unicelement():
    print(set(mylist))

mylist = [1, 2, 1 ,1, 2, 3, 4]
my_unicelement()


# 3. Write a function to print the even numbers from a given list.

myNumberList = [2, 4, 5, 6, 7, 8]
def is_even_num(myNumberList):
    enum = []
    for n in myNumberList:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#       Sample String : 'The quick Brow Fox'
#       Expected Output :
#       No. of Upper case characters : 3
#       No. of Lower case Characters : 12

sentence = 'The quick Brow Fox'
def string_test(sentence):
    d={"upper_case":0, "lower_case":0}
    for i in sentence:
        if i.isupper():
           d["upper_case"]+=1
        elif i.islower():
           d["lower_case"]+=1
        else:
           pass
    print ("Original String : ", sentence)
    print ("No. of Upper case characters : ", d["upper_case"])
    print ("No. of Lower case Characters : ", d["lower_case"])

string_test('The quick Brown Fox')



# 5. Write a Python function that takes a number as a parameter and check the number is prime or not

number = int(input("Please input the number:  "))

def devide(number):
    print(number%2 != 0)
    return True

devide(number)
