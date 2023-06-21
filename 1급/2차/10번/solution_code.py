def solution(s):
    s += '#'
    answer = ""
    for i in range(len(s)):
        if s[i] == '0' and s[i + 1] != '0':
            answer += '0'
        else if s[i] == '1':
            answer += '1'
    return answer
