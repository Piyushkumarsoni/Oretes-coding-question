def getPairsCount(arr, n, m):

    for i in arr:
        for j in range(i+1, n):
            if arr[i] + arr[j] == m:
                data1=str(i+1)
                data2=str(j+1)
                print(data1+" "+data2)     
    return 0
 
 
# Driver function
if __name__=="__main__":

    arr = []
    n = int(input())
    sum = int(input())
    for i in range(n):
        a=int(input())
        arr.append(a)
    getPairsCount(arr, n, sum)