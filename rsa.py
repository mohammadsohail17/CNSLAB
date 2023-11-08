import math

def gcd(a,h):
    temp=0
    while(1):
        temp=a%h
        if temp==0:
            return h
        a=h
        h=temp

p=3
q=7
n=p*q
phi=(p-1)*(q-1)
e=2
while (e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e+=1
k=2
j=0
while True:
    if (j*e)%phi==1:
        d=j
        break
    else:
        j+=1
msg=12
#encryption
c=(msg**e)%n

print(c)
#decryption
print((c**d)%n)