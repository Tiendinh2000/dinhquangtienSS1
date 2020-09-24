def month(m):
    if m=="01":
        return "January"
    if m=="02":
        return "February"
    if m=="03":
        return "March"
    if m=="04":
        return "April"
    if m=="05":
        return "May"
    if m=="06":
        return "June"
    if m=="07":
        return "Junly"
    if m=="08":
        return "August"
    if m=="09":
        return "September"
    if m=="10":
        return "October"
    if m=="11":
        return "November"
    if m=="01":
        return "December"

def form(date):
   d= date.strip().split("/")
   print(month(d[1])+ " , "+d[0]+ " "+d[2])

def containSlash(date):
    return date.find("/")

if __name__=='__main__':
     d=input("date in the form mm/dd/yyyy:")
     if(len(d)==10) and containSlash(d)!=-1 :
        form(d)
     else:
         raise ValueError