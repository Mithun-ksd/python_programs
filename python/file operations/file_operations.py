with open("example.txt","w")as f: 
    f.write("The BCA course.\nHas a very good scope.\nand has a total 9 subjects.") 
with open("example.txt","r")as f: 
    text=f.read()
    print(text)
num_char=len(text) 
num_words = len(text.split()) 
num_lines=len(text.split("\n")) 
print(f"Number of characters:{num_char}") 
print(f"Number of words:{num_words}") 
print(f"Number of lines:{num_lines}")
