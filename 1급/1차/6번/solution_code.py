def solution(pos):
    answer = 0
    
    list_ = [[1,1,1,1], [1,1,1,1]]
    x = ord(pos[0]) - ord('A')
    y = int(pos[1]) -1
    
    if x-2 < 0:
      list_[0,0] = 0
      list_[1,0] = 0
      if x-1 < 0:
        list_[0,1] = 0
        list_[1,1] = 0
    
    if x+2 > 7:
      list_[0,3] = 0
      list_[1,3] = 0
      if x+1 > 7:
        list_[0,2] = 0
        list_[1,2] = 0
    
    if y-2 < 0:
      list_[1,1] = 0
      list_[1,2] = 0
      if y-1 < 0:
        list_[1,0] = 0
        list_[1,3] = 0
        
    if y+2 > 7:
      list_[0,1] = 0
      list_[0,2] = 0
      if y+1 > 7:
        list_[0,0] = 0
        list_[0,3] = 0
    
    for i in list_:
      for j in i:
        if j == 1:
          answer = answer + 1
       
    return answer
