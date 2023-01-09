print("/// list of vowels from a  word ///\n ")
txt=str(input("Enter the word:\n"))
v="aeiouAEIOU" #Flist of vowels selected from a given word
nls=set( [n for n in txt if n in v])

print("list of vowels\n",list(nls))