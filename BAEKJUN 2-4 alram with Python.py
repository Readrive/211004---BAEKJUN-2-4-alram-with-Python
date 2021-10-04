H, M = map(int, input().split())

if 0 > H or H > 23:
    print("시간은 0 ~ 23 사이여야합니다.")
    H = int(input("원하는 시간을 입력하세요: "))
    
if 0 > M or M > 59:
    print("분은 0 ~ 59 사이여야합니다.")
    M = int(input("원하는 분을 입력하세요: "))
    
if M < 45:
    aH = int(H - 1)
    aM = int(M - 45 + 60)
    if aH == -1:
        aH = 23
    print(aH, aM)

else:
    aH = H
    aM = int(M - 45)
    print(aH, aM)
