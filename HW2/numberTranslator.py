
def pr(pho):
   for i in range(0,len(pho)):
     print(str(dic(pho[i])),end="")
def dic(a):
    if a=='A' or a=='B' or a=='C':
        return 2
    if a=='D' or a=='F' or a=='E':
        return 3
    if a=='G' or a=='H' or a=='I':
        return 4
    if a=='J' or a=='K' or a=='L':
        return 5
    if a=='M' or a=='N' or a=='O':
        return 6
    if a=='P' or a=='Q 'or a=='R' or a=='S':
        return 7
    if a=='T' or a=='U' or a=='V':
        return 8
    if a=='W' or a=='X' or a=='Y' or a=='Z':
        return 9
    else:
        return a


def containDash(date):
    return date.find("-")

if __name__=='__main__':

     num=str(input("enter phone number XXX-XXX-XXXX:"))
     if containDash!=-1 and len(num)==12:
       pr(num)
     else:
         print("it's not a valid phonenumber")

