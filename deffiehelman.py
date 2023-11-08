P=23
G=9
x1=4
x2=3
y1, y2 = pow(G, x1) % P, pow(G, x2) % P
 
# Generate Secret Keys
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P
 
print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")
 
if k1 == k2:
    print("Keys Have Been Exchanged Successfully")
else:
    print("Keys Have Not Been Exchanged Successfully")