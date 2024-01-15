def gcd(a,b):
    if a%b==0: return b
    else: return gcd(b, a%b)

a,b=sorted(map(int, input().split()))
gc=gcd(a,b)
print(gc)
print(a*b//gc)