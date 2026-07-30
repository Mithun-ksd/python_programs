def calculate(str): 
        str=input("Enter the string: ") 
        charCount={} 
        for i in str: 
            if i in charCount: 
                charCount[i]+=1 
            else: 
                charCount[i]=1 
        return charCount
print("Frequence of each letter\n",calculate(str))
