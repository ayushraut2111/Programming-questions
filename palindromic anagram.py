class Solution:
    def solve(self, s):
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
            
        if len(s)%2==0:
            for key,value in dict.items():
                if value%2!=0:
                    return False
            return True
        else:
            count=0
            for key,value in dict.items():
                if value%2!=0:
                    count+=1
            if count==1:
                return True
            else:
                return False