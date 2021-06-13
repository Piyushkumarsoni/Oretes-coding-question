def countOccurrences(word):
     
    # split the string by spaces in a
    a = word.split(" ")
 
    #removing duplicates word in a and store in new list.
    newstringset = []
    for num in a:
        if num not in newstringset:
            newstringset.append(num)

    valuecount=[]
    for i in range(0, len(a)):
        count = 0
        for j in range(0, len(a)):
        # if match found increase count
            if (a[i] == a[j]):
                count = count + 1
        valuecount.append(count)
#printing output...
    for k in range(0,len(newstringset)):
        print(newstringset[k]+" "+str(len(newstringset[k]))+" "+str(valuecount[k]))
        
            
    return      
 
# Driver code
if __name__=="__main__":
    word=input()
    countOccurrences(word)


