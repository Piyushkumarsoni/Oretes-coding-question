if __name__=="__main__":
    page=[]
    price=[]
    chapter=[]
    book=[]
    n=int(input())
    #book details
    for i in range(n):
        print("Book"+str(i+1)+" detils:-")
        s=input()
        book.append(s.split(" "))
    
    Arr=int(input())
    if(Arr==1):
        book.sort()
        for i in range(3):
            print(book[i])
    elif(Arr==2):
        book.sort(reverse=True)
        for i in range(3):
            print(book[i])
