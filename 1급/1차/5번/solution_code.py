def solution(n):
    answer = 0
    j = 0
    cnt = 2*n
    for i in range(n):
      if j == 0:
        answer = 1
        continue
      else:
        if j%2 ==0:
          answer += cnt
          cnt = cnt - 4
        else:
          answer += cnt
    
    return answer
