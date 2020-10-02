

def Ans():

    d = {}  # dictionary
    tem = {}  # template
    with open("Practice2_answer.txt") as f:
        for line in f:
            tem = line.split()  # eachline is a tuple
            d[tem[0]] = tem[1]  # assign to the dictionary

    return (d)

def Mark(StdAns,A):
    mark=0
    for i in range(0,19):
        if StdAns[i]==A[i]:
            mark+=1
    return mark

def Question():
    d = {}  # dictionary
    tem = {}  # template
    with open("Practice2_Question.txt") as f:
        for line in f:
            tem = line.split()  # eachline is a tuple
            d[tem[0]] = tem[1]  # assign to the dictionary

    return (d)


if __name__=="__main__":
  AnsArr=[]
  Q=[]
  for key,val in Question():
      Q.append(val)


  #for i in range(0,len(Question())):
   #   print(Question()[i],end="")
   #   ans=input(": ")
   #   AnsArr.append(ans)



 # print(Mark(AnsArr,Ans))
