# read file as a dictinay
def dic(String):
        d={}#dictionary
        tem={} #template
        with open("dic.txt") as f:
            for line in f:
              tem = line.split() # eachline is a tuple
              d[tem[0]] = tem[1]# assign to the dictionary

        return (d[String])

if __name__=='__main__':
    S = str(input())
    print(dic(S))

