def getInput():
   i= input("enter a num:")
   return i

def search(arr, char):
    for i in range(0,len(arr)):
        if arr[i]==char:
            return i



if __name__=='__main__':
    a=[]
    count=0
    m=int(input("enter number of element in arr:"))
    while(count<m):
      i= input("enter a num:")
      if i.isnumeric() and count !=m:
            a.append(i)
            count+=1
      else:
          print("it's not integer")

    s=input("enter number that you wanna search:")
    print("it's possition: ",search(a,s))
    print(a,s)