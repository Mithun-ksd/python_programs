tp1=(1,2,5,7,9,2,4,6,8,10) 
Tupleeven=() 
print("The elements of the first tuple are:",tp1) 
print("The first half of the tuple are",tp1[:5]) 
print("The second half of the tuple in the next line are",tp1[5:]) 
print("Tuple items=",tp1) 
print("\n The even number in the tuple are:") 
listeven=list(Tupleeven) 
for i in range(len(tp1)): 
    if(tp1[i]%2==0): 
        listeven.append(tp1[i]) 
Tupleeven=tuple(listeven) 
print(Tupleeven) 
tp2=(11,13,15) 
print("The elements of the second tuple are:",tp2) 
tp3=tp1+tp2 
print("The elements of the tuple after concatenation:",tp3) 
print("The maximum number in the tuple is:",max(tp3)) 
print("The minimum number in the tuple is:",min(tp3))
