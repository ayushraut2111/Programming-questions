def count_substring(string, sub_string):
    a=len(sub_string)
    count=0
    x=sub_string[0]
    for i in range(len(string)-a+1):
        if string[i]==x:
            d=string[i:i+a]
            if d==sub_string:
                count=count+1
    return count





if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)