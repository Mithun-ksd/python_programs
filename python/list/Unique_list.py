numlist=[]
n=int(input("Enter number of elements to be insert:\n"))
for i in range(n):
    ele=int(input(f"Enter elements {i+1} :"))
    numlist.append(ele)
    print("The elements in the list are")
    print(numlist)
uniquelist=[]
for ele in numlist:
    c=numlist.count(ele)
    if(c==1):
        uniquelist.append(ele)
print("The unique elements in the list are : \n",uniquelist)
