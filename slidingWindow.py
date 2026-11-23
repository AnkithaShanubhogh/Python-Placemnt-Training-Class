def maxSubArray(li,k):
    n=len(li)
    curS=sum(li[0:k])
    maxS=curS
    for i in range(n-k):
        curS=curS-li[i]+li[i+k]
        maxS=max(curS,maxS)
    return maxS
li=[2,7,3,1,9]
k=3
print(maxSubArray(li,k))