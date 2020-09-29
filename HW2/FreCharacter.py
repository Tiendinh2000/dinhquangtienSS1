

def countFrequent(cha,str):
     count=0
     for i in range(0,len(str)):
       if char==str[i]:
           count+=0
     return count



if __name__=='__main__':
    max=0
    posOfMax=0
    String=input("enter number of element in arr:")
    for y in range(0,len(String)):
        if countFrequent(String[y],String)>max:
            max=countFrequent(String[y],String)
            posOfMax=y
    print(posOfMax)