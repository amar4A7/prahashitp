n = int(input())
a = n
rev = 0
while n:
    rem = n%10
    rev = rev*10+rem
    n=n//10
if(rev==a):
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')
    
