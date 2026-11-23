#selection sort
# def selectionS(li):
#     n=len(li)
#     for i in range(n-1):
#         min_index=i
#         for j in range(i+1,n):
#             if li[j]<li[min_index]:
#                 min_index=j
#         li[i],li[min_index]=li[min_index],li[i]
#     return li
# li=[11,22,333,44,55,66]
# print(selectionS(li))

#quick sort
# def quickS(li):
#     if len(li)<=1:
#         return li
#     pivot=li[-1]
#     left=[]
#     right=[]
#     for val in li[:-1]:
#         if val<=pivot:
#             left.append(val)
#         else:
#             right.append(val)
#     sorted_left=quickS(left)
#     sorted_right=quickS(right)

#     return sorted_left+[pivot]+sorted_right
# li=[1,2,3,4,8,6,5,2,3,9]
# print(quickS(li))

##bubble sort

def bubbleS(li):
    n=len(li)
    for i in range(1,n):
        for j in range (n-i):
            if li[j]<li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li
li=[1,2,4,9,5,7,8,47,98]
print(bubbleS(li))