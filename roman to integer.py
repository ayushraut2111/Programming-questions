class Mysolution:
    def solve(self, s):
            roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,   'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
            num=0
            for i in range(len(s)-1):
                j=i+1
                if roman[s[i]]<roman[s[j]]:
                    num-=roman[s[i]]
                else:
                    num+=roman[s[i]]
            num+=roman[s[len(s)-1]]
            return num
p1=Mysolution()
s=input()
print(p1.solve(s))