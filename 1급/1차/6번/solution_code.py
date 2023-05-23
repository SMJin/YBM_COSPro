def solution(pos):
    answer = 0
    
    # 현재 위치값을 기준으로 이동할 수 있는 곳의 좌표의 방향을 기록한다
    direction_x = [-2, -2, -1, -1, 1, 1, 2, 2]
    direction_y = [1, -1, 2, -2, 2, -2, 1, -1]
    
    # 좌표는 0~7 로 설정한다.
    x = ord(pos[0]) - ord("A")
    y = ord(pos[1]) - ord("0") -1
    
    for i in range(8):
        go_x = x + direction_x[i]
        go_y = y + direction_y[i]
        
        if go_x > -1 && go_x < 8 && go_y > -1 && go_y < 8:
            answer = answer + 1
       
    return answer
