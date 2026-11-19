class solution(object):
    def twoSum(self,numbers,target):
        l=0
        r=len(numbers)-1
        summ=0
        while l<r:
            summ=numbers[l]+numbers[r]
            if summ==target:
                return(l+1,r+1)
            if summ > target:
                r-=1
            else:
                l+=1
        return []

if __name__ == "__main__":
    print(solution().twoSum([2,7,11,15],9))