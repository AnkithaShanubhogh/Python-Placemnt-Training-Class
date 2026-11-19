# dict={
#     "college":"smvitm",
#     "session":4,
#     "location":"udupi"
# }
# print(dict)
# print(dict["college"])
# print(dict.get("location"))

# detail={
#     "Name":"ankitha",
#     "age":15,
#     "salary":1500000
# }
# print(detail,id(detail))
# detail["salary"]=1900000
# print(detail,id(detail))

# movie={"name":"Durandar","package":600000}
# print(movie)
# movie["Actor"]="Ranveer"
# del movie["package"]
# print(movie)

# dict={
#     "college":"smvitm",
#     "session":4,
#     "location":"udupi"
# }
# for k in dict.keys():
#     print(k)
# for v in dict.values():
#     print(v)
# print()

# for k,v in dict.items():
#     print(k,"=",v)

# d={}
# print(d,type(d))

# #display frequency count of ecah character from the given string
# str="hellogood"
# dict={}
# for ch in str:
#     if ch in dict:
#         dict[ch]+=1
#     else:
#         dict[ch]=1
# print(dict)

#find the first non-repeating character from the given string
'''str="hellogood"
dict={}
flag=0
for ch in str:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
print(dict)

for key,val in dict.items():
    if dict[key]==1:
        print("non repeating char:",key)
    else:
        flag=1
        break
if flag==0:
    print(-1)'''

str="moon"