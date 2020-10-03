def Ans():

    d = {}  # dictionary
    tem = {}  # template
    with open("Answer.txt") as f:
        for line in f:
            tem = line.split()  # eachline is a tuple
            d[tem[0]] = tem[1]  # assign to the dictionary

    #return value of the answer as array
    arr = list(d.values())
    return (arr)


#  Mark : detemine the incorrect answer
#
def Mark(StdAns,A):
    mark=0
    trace = [] # arr contains position of incorrect ans and number of correct ans in last element
               # arr=[incorrect ans,...., mark]

    for i in range(0,20):
        if str(StdAns[i].upper())==A[i]: # check ans
            mark+=1
        else:
            trace.append(i+1)

    trace.append(mark)
    return trace


def getStdAns():

    StdAns=[]
    with open("Exam.txt") as f:
        for line in f:
            print('')
            print(line) # display question
            a=input("your answer: ") # get input
            StdAns.append(a)
    return StdAns

def Pass(m):
    if (m>= 15):
        print("congratulation! you Passed")
    else:
        print("you Failed!")

if __name__=="__main__":

  arr= getStdAns()
  Trace=Mark(arr, Ans())
  mark=Trace[len(Trace)-1]

  Pass(mark)

         #print result:
  print('your score: ',mark)
  print("incorrect: ",end='')
  for i in range(0,len(Trace)-1):
      print(Trace[i],end=', ')




