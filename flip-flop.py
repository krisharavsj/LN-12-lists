def palindrome(r):
    e=len(r)-1
    s=0
    while (s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(3,2,3,3,2,1)
if (palindrome(r)):
    print("it is a palindrome")
else:
    print("it is not a palindrome")