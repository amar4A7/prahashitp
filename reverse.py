n =  int(input())
rev = 0
while True:
    rem = n%10
    rev = rev*10+rem
    n=n//10
    if n==0:
     break
print(rev)
