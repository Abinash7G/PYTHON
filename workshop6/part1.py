a=7
b=5
sum = a+b
print ('sum=',sum)
print(sum==12) #True and True

print (sum==12,sum<12, sum>12) #True and False or True

print (sum==13, sum==11,sum==12) #False or False and True

print (sum==12, ) #False or 0
print (sum==12,) #not (False) and True
print (sum==13,) #not (True or not(False and False))
    

