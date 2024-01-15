####################################
# 에라토스테네스의 체를 이용한 소수 판별
####################################
import math
def prime(n):
    if n==1: return False
    for i in range(2,int(math.sqrt(n)+1)):
                if n%i==0: return False
    return True

a=int(input())
b=list(map(int,input().split()))
count=0
for j in b:
    if prime(j): count+=1
print(count)