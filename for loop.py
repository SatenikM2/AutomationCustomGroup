# 1. Перемножить все не чётные значения в диапазоне от 9173 до 9435;
result = 1
for i in range (9173, 9435,2):
    result *= i
print(result)


# 2*. Print the following pattern
#     5 4 3 2 1
#     4 3 2 1
#     3 2 1
#     2 1
#     1
rows = 5
for i in range(rows, 0,-1):
    for j in range(i,0, -1):
        print(j, end=' ')
    print("\r")

# 3. Display numbers from -10 to -1 using for loop

for i in range(-10, 0, 1):
    print(i)

# 4. Calculate the cube of all numbers from 1 to a given number from usernum1

num1 = int(input("Please input the number"))
Cubes = []
for i in range((num1+1)):
   Cubes.append(i**3)
   print(Cubes)

# 5. Find the factorial of a given number
num = int(input("Please input a number: "))
fac = 1
for i in range(1, num+1):
    fac = fac * i
print("the fac of ", num, " is", fac )