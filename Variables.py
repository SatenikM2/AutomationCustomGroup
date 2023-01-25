# > < >= <=  == |=
var1 =71
var2 =31
if var1 == var2:
    print("given variable are aquel")
    print(var1, "=" ,var2)
elif var1>var2:
    print(var1, "greather then" , var2)
else:
    print("number not equal")


print ()


userAge = 17
fromGyumri= True

if userAge>=18 and userAge <60:
    print("you can enter succesfuly")
elif userAge>=16 and userAge <18:
    if fromGyumri:
        print("Welcome")
    else:
        print("you can enter with older people")
elif userAge<16:
    print("you can not enter")
elif userAge >=60:
    print("you should go to the  next dooR")



print()

#myvar=input("please input some value: ")
#print(type(myvar))
#print("My value is: ", myvar)


bar1=int(input("please input your number: "))
bar2=int(input("please input your height: "))

if bar1>bar2:
    print(bar1, "greatist then" , bar2)
elif bar1<bar2:
    print(bar1, "lenn then", bar2)
else:
    print("bar are equal")
