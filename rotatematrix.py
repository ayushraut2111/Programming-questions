def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

def rotateby90Anti(A):
	n = len(A)
	a,b,c,d = 0,0,0,0
	for i in range(n // 2):

		for j in range(n - 2 * i - 1):
			a = A[i + j][i]
			b = A[n - 1 - i][i + j]
			c = A[n - 1 - i - j][n - 1 - i]
			d = A[i][n - 1 - i - j]

			A[i + j][i] = d
			A[n - 1 - i][i + j] = a
			A[n - 1 - i - j][n - 1 - i] = b
			A[i][n - 1 - i - j] = c
			

n=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))[:n]
    a.append(b)
s=input()
l=s.count('L')
r=s.count('R')
diff=abs(l-r)%4
if diff==0:
    print(a)
else:
    if l>r:
        while diff:
            rotateby90Anti(a)
            diff-=1
    else:
        while diff:
            rotate90Clockwise(a)
            diff-=1
    print(a)


