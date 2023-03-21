import math

de = 0.000001 #델타값, 0에 가까울수록 정확도 상승
def f(x):
    return math.e**(-x)*math.sin(x) #극값위치 계산할 함수 입력
def d(x):
    return (f(de + x)-f(x))/de #미분계수의 정의
ls = []
for c in range(-10,10): #미분값 조사 범위
    checksum1 = 0
    checksum2 = 0
    checksum3 = 0
    checksum4 = 0
    trysum = 0
    while(abs(d(c))>0.000001):
        if abs(d(c+de))>=abs(d(c-de)): #미분값 작은곳으로 가기
            if checksum3 == c-de*100000: #반복당할때 탈출
                break
            print(c)
            c -= de*100000
            checksum3 = c
        else:
            if checksum4 == c+de*100000:
                break
            print(c)
            c += de*100000
            checksum4 = c

    while(abs(d(c))>0.000001):
        if abs(d(c+de))>abs(d(c-de)):
            if checksum1 == c-de:
                break
            print(c)
            c -= de
            checksum1 = c
            trysum += 1
            if trysum > 200000: #기울기 감소+수렴 시에 탈출
                break
        else:
            if checksum1 == c+de:
                break
            print(c)
            c += de
            checksum2 = c
            trysum += 1
            if trysum > 200000:
                break
    if trysum < 200000:
        ls.append(round(c,3))
print(list(set(ls))) #set으로 중복값 제거
