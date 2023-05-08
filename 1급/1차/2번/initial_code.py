def addZeroFirst(binaryAB, cnt):
  for i in range(cnt):
    binaryAB = '0' + binaryAB
  return binaryAB

def hammingDistance(binaryA, binaryB):
  lenA = len(binaryA)
  lenB = len(binaryB)
  if lenA > lenB:
    len_diff = lenA - lenB
    addZeroFirst(lenB, len_diff)
  elif lenA < lenB:
    len_diff = lenB - lenA
    addZeroFirst(lenA, len_diff)
  
  cnt = 0
  for i in range(lenA):
    if binaryA[i] != binaryB[i]:
      cnt = cnt + 1
  return cnt      
      
def solution(binaryA, binaryB):
  hammingDistance(binaryA, binaryB)
