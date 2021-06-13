if __name__=="__main__":
    n=int(input())
    p1=[]
    p2=[]
    point1=0
    point2=0
    player1=input("Enter player1 name:-")
    
    #player1 score
    for i in range(n):
        score1=int(input())
        p1.append(score1)
    player2=input("Enter player2 name:-")
    for j in range(n):
        score2=int(input())
        p2.append(score2)

    for k in range(n):
        if(p1[k]>p2[k] and p1[k]!=p2[k]):
            point1=point1+1
        elif(p1[k]<p2[k] and p1[k]!=p2[k]):
            point2=point2+1
        else:
            point1=point1
            point2=point2
    
    print(player1 + " "+str(point1))
    print(player2 + " "+str(point2))
    if(point1>point2):
        print(player1+" won the competition.")
    else:
        print(player2+" won the competition.")
