def nearly_equal(a,b):
    if len(a)!=len(b):
        return false
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    if count==1:
        return True
    else:
        return False

a=input("Enter first string: ")
b=input("Enter second string: ")
if a==b:
    print("Strings are equal")
if nearly_equal(a,b):
    print("Strings are nearly equal")
else:
    print("Strings are not equal")
