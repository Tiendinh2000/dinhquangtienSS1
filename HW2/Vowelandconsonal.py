#check whether a character is a vowel or not
def Vow(ch):
    if ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u':
          return True
    else :
        return False


#find the number of vowel in String, except special characters such as: "?,!,@..."
def vow(S):
    count=0
    for i in range(0,len(S)):
        if S[i].isalpha() and Vow(S[i])==True :
            count+=1
    return count

#number of consonal
def Cons(S,vow):
    count=0
    for i in range(0,len(S)):
        if S[i].isalpha():
            count+=1
    return count-vow


#main...
if __name__=='__main__':
     d=input("enter a string:")
     print("vowel: ",vow(d))
     print("consonal: ",Cons(d,vow(d)))