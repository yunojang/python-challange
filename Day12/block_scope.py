arr = [1, 2, 3]

if len(arr) > 2:
    new_item = arr[0]

print(new_item)

# 사용한 결과, 함수 범위 스코프 & 가장 가까운 곳 부터 탐색한다.


def printT():
    print(t == None)

    t = 10


printT()
