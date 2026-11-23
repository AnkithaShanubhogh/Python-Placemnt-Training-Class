str="abcbaad"
n=len(str)
st=set()
l=0
maxL=0
for r in range(n):
    while str[r] in st:
        st.remove(str[l])
        l+=1
    st.add(str[r])
    curL=r-l+1
    maxL=max(curL,maxL)
print(maxL)