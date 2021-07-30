def add(a,b):
    result=a+b
    return result
def sub(a,b):
    return (a-b)
def mult(a,b):
    print("Mult function from Function Demo Developer Function")
    return a*b
def div(a,b):
    return (a/b)



a1,b1=input("enter 2 Intezer for Arithmetic Operations").split()
a1=int(a1)
b1=int(b1)
sum=add(a1,b1)
print("Sum of 2 numbers {} and {}".format(a1,b1,add(a1,b1,add(a1,b1)))
#print("Subtract of 2 numbers %i and %i is %i" %(a1,b1,sub(a1,b1)))
#print("Multiplication of 2 numbers %d and %d is %d" %(a1,b1,mult(a1,b1)))
#print("Divide of 2 numbers %d and %d is %f" %(a1,b1,div(a1,b1)))    
