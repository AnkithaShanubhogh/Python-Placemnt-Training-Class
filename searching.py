# def linear_search(li,tar):
#     n=len(li)
#     for i in range(n):{
#         if(target==li[i]):{
#             return i;
#         }
#     return -1;
#     }
#     li=[1,2,3,4,5,6]
#     tar=2
#     index=linear_search(li,tar)
#     if index==-1:
#         print("target is missing")
#     else:
#         print("target found at index :",index)


'''Binary search!'''
def binaryS(li,tar):
    n=len(li)
    l=0
    r=n-1
    while (l<=r):
        mid=(l+r)//2
        if(li[mid]==tar):
            return 0
        if tar<li[mid]:
            r=mid-1
        if tar>li[mid]:
            l=mid+1
    return -1
li=[1,2,3,4,5]
tar=5
index=binaryS(li,tar)
if index==-1:
    print("target is missing")
else:
    print("target found at index :",index)
