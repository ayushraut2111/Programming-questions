# if __name__ == '__main__':
#     a=[]
#     s=set()
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         b=[name,score]
#         a.append(b)
#         s.add(score)
#     l=list(s)
#     l.sort()
#     a.sort()
#     for i in a:
#         if i[1]==l[1]:
#             print(i[0])



# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     a=list(student_marks[query_name])
#     x=sum(a)/len(a)
#     limit_float = round(x, 2)
#     print(limit_float)

# a='ayush'
# b='anish'
# if a[0]==b[0]:
#     print("yes")
# else:
#     print("no")

l=[1,2,3,4,5]
l[0],l[1]=l[1],l[0]
print(l)