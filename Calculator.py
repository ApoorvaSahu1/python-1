def Addition(x,y):
    return x+y

def Subtraction(x,y):
    return x-y

def Multiplication(x,y):
    return x*y
     
def Division(x,y):
    return x/y

def Greater(x,y):
    if(x>y):
        return x
    else:
        return y

def Power(x,y):
    return x**y

print("Select Operation And The No. Alloted :- ")
print("1.Addition")
print("2.Subtraction")
print("3.Mutliplication")
print("4.Division")
print("5.Greater")
print("6.Power")

while True:

    var1=input("Enter the Option No.")

    if var1 in ('1','2','3','4','5','6'):
        var2=float(input("Enter First number :"))
        var3=float(input("Enter Second number :"))

        if var1 == '1':
            print("Addition of the number is :",Addition(var2,var3))
        
        elif var1 == '2':
            print("Subtraction of the number is :",Subtraction(var2,var3))

        elif var1=='3':
            print("Multiplication of the number is :",Multiplication(var2,var3))

        elif var1=='4':
            print("Division of the number is :",Division(var2,var3))

        elif var1=='5':
            print("Greater In The Given Number Is : ",Greater(var2,var3))
    
        elif var1=='6':
            print("Total Of The Given Power Number Is : ",Power(var2,var3))
        
        repeat=input("Continue?(yes/no)")
        if repeat=='no':
            break
    else:
        print("Option No. Does'nt Exist ")
        repeat=input("Continue?(yes/no)")
        if repeat=='no':
            break