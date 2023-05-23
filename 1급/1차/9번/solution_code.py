def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]):
            cnt = cnt + 3
        else:
            # 음수가 될 수는 없기에
            cnt = max(0, cnt - 1)
    return cnt
