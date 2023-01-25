
# 1. Write a program to construct the following pattern.
#       *
#       * *
#       * * *
#       * * * *
#       * * * * *
#       * * * *
#       * * *
#       * *
#       *
symbol = " *"
i = 1
while i < 5:
    print(i * symbol)
    i += 1
while i > 0:
    print(i * symbol)
    i -= 1
# 2. Write a program to create the multiplication table (from 1 to 10) of a number.
#       Input a number: 6
#       6 x 1 = 6
#       6 x 2 = 12
#       6 x 3 = 18
#       6 x 4 = 24
#       6 x 5 = 30
#       6 x 6 = 36
#       6 x 7 = 42
#       6 x 8 = 48
#       6 x 9 = 54
#       6 x 10 = 60
num1 = int(input("Please input the number: "))
num2 = int(input("Please input the number: "))


while num2 <= 10:
    print(num1, "*", num2, "=", num1*num2)
    num2 += 1


# 3. Write a program to print alphabet pattern 'O'
#    Expected Output:
#          *
#        *   *
#        *   *
#        *   *
#        *   *
#        *   *
#          *
print (" * ")
i = 5
while i > 0:
    print("*" + 2*"  "+"*")
    i -= 1
print(" * ")


# 4. Calculate the sum of all numbers from 1 to a given number from user

num = int(input('Enter a positive number: '))
sum = 0

# use while loop to iterate until zero
while num > 0:
    sum += num
    num -= 1
print("The sum is", sum)




# 5. Write a program to check whether a specified list is sorted or not
mylist = [1, 3, 6, 7]
index = 1
listlenght = len(mylist) - 1
result = True
while index < listlenght:
    if mylist[index] < mylist[index-1]:
        result = False
    index += 1

print(result)