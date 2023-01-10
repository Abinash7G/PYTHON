def calculator():
    """Here, input is given by user and we are adding number given user"""
    a=int(input("enter any number"))
    b=int(input ("enter any number"))
    sum= float(a+b)
    return sum
print(calculator.__doc__)
print(calculator())
def calculator1():
"""Here, input is given by user and we are subtract number given user"""
    a=int(input("enter any number"))
    b=int(input ("enter any number"))
    sub= float(a-b)
    return sub
print(calculator2.__doc__)
print(calculator1())
def calculator2():
    """Here, input is given by user and we are multiply number given user"""
    a=int(input("enter any number"))
    b=int(input ("enter any number"))
    mul= float(a*b)
    return mul
print(calculator2.__doc__)
print(calculator2())

def calculator3():
    a=int(input("enter any number"))
    b=int(input ("enter any number"))
    div= float(a/b)
    return div
print(calculator3())
def calculator4():
    a=int(input("enter any number"))
    b=int(input ("enter any number"))
    #truncated division
    truncate = float(a//b)
    return truncate
print(calculator4())
def calculator5():
   a=int(input("enter any number"))
   b=int(input ("enter any number"))
    #truncated division
   modulus = float(a%b)
   return modulus 
print(calculator5())
def calculator6():
    a=int(input("enter any number"))
    b=int(input ("enter any number"))
    #exponentiation
    exp = float(a**b)
    return exp 
print(calculator6())

    break


    
