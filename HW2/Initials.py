

n = str(input("enter your full name:"))
def spl(s1):
    Name= s1.split()
    for each in Name:
        print(each[0].upper(),end=" ")
spl(n)
