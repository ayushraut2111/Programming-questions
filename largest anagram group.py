words = ["ab", "ba", "abc","hgd", "cba", "bca", "ddddd"]
for i in range(len(words)):
    words[i]=''.join(sorted(words[i]))
words.sort()
ans=0
s=set()
for i in words:
    s.add(i)
print(s)
for i in s:
    ans=max(ans,words.count(i))
print(ans)