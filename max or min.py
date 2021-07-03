n = int(input())
rem = 0
max = 0
min = 9
while(n!=0):
    rem = n%10
    if(rem>max):
        max=rem
    if(rem<min):
        min=rem
    n=n//10
print(max,'= maximum')
print(min,'= minimum')
    
