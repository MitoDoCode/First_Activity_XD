sentence = input("Enter A Message:")
search = input("what word are you looking for:")

missing  = sentence.find(search)

if missing >= 0:
    print("the word:"+search+ " is found at index:"+ str(missing))

else:
    print("The word '" + search + "' is not found.")