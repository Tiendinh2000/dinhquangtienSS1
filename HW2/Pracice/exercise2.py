
def toText(num):
    if num =='0':
       return ""
    if num=='1':
        return ' mot'
    if num=='2':
        return ' hai'
    if num=='3':
        return ' ba'
    if num=='4':
        return ' bon'
    if num=='5':
        return  ' nam'
    if num=='6':
        return ' sau'
    if num=='7':
        return ' bay'
    if num=='8':
        return ' tam'
    if num=='9':
        return ' chin'


def classify(n,c):
    if n=='0' :
        return"chuc"
    if n=='1' :
        return'tram'
    if n=='2':
        return cate(c)
def cate(c):
    if c=='1':
        return ' dong'
    if c=='2':
        return' ngan'
    if c=='3':
        return' trieu'
    if c=='4':
        return' ti'


def form(string):
    print(format({},))

def print(len,mon):

    if len >=9:
       print(toText(mon[1][2]) + "tram" + toText(mon[3][1]) + 'chuc' + toText(mon[3][0]) + cate(3))
       print(toText(mon[2][2])+"tram"+toText(mon[2][1])+'chuc'+toText(mon[2][0])+cate(2))
       print(toText(mon[1][2])+"tram"+toText(mon[1][1])+'chuc'+toText(mon[1][0])+cate(1))
       print(toText(mon[0][2] + "tram" + toText(mon[0][1]) + "chuc" + toText(mon[0][0]) + cate(0)))

if __name__=='__main__':
    i = str(input('ENter money:')) ## 012,345,678
    i.reverse()
    mon= i.strip().split(',') # mon =['876','543','210'}









