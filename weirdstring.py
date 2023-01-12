def solution(s):
    answer=[]
    
    '''
    s=s.split()
    
    for j in range(len(s)):
        s[j]=[i for i in s[j]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if i%2==0:
                s[j][i]=s[j][i].upper()
    for j in range(len(s)):
        s[j]=''.join(s[j])
    answer=' '.join(s)
    '''
    s= [ i for i in s]
    cnt=0
    for i in range(len(s)):
        if s[i]==' ':
            cnt=0
            answer.append(s[i])
        else:
            if cnt%2==0:
                answer.append(s[i].upper())
            else:
                answer.append(s[i].lower())
            cnt+=1
    answer=''.join(answer)
    print(answer)
    return answer
solution("      dfvvvvvvvv  hello   world   ")