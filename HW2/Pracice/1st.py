p=7
q=11
e=17

def  findZ(p,q):
    return (p-1)*(q-1)
def  findN(p,q):
    return p*q
def PublicKey(p,q):
    arr =[]
    arr[0]= findN(p, q)
    arr[1]= findN(p, q)-findZ #=e
    return arr

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

#Python program for Extended Euclidean algorithm
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)
#gcd, x, y = egcd(26, 15)
#print(y)

#find private 17*d=1(mod 60)
#   div=z=60; dvs = e= PubicKey[1]


