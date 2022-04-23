if __name__ == '__main__':
    N = int(input())
    list=[]
    while(N>0):
        n=input()
        if(n=='insert'):
            a,b=map(int,input().split())
            list.insert(a,b)
            print(list)
        
        elif(n=='append'):
            a=int(input())
            list.append(a)
            print(list)
        elif(n=='print'):
            print(list)
        elif(n=='remove'):
            a=int(input())
            for i in range(len(list)):
                if list[i]==a:
                    del list[i]
                    break
            print(list)
        elif(n=='sort'):
            list.sort()
            print(list)
        elif n=='pop':
            list.pop()
            print(list)
        elif n=='reverse':
            list.reverse()
            print(list)
        else:
            break
                    
    N=N-1