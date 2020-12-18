import re
import string



def start():
    print("What would you like to do? /n")
    print("1: Get the score of a word")
    print("2: Get the average score of words in a file ")
    print("3")
    print("4")

    i=int(input())
    return i


# read file and return frequency of each word in that file
def frequency(object):
    fre = {}
    document_text = open(object, 'r')
    #set all word to lower case
    text_string = document_text.read().lower()

    match = re.findall(r'\b[a-z]{3,15}\b', text_string)

    for word in match:
        count = fre.get(word, 0)
        fre[word] = count + 1

    fre_list = fre.keys()
    dictionary={}


    for words in fre_list:
        #set key, value to dictionary
        dictionary.update({words: fre[words]})
    return dictionary



def get_score(object,fre_dictionary):
    file =object
    dic =fre_dictionary
    new_dic={}

    num=[]
    with open(file) as f:
        for line in f:
            #num =  int in 1st line divide for frequency

           num.append(int(line[0]))

    mark=[]
    pos=0
    for k,v in dic.items():
            mark=int(num[pos])
            new_dic.update({k:(num[pos])})
            pos+=1
    return new_dic

def tmp_main():
   i=start()
   if i==1:

       fre=frequency("training.txt")
       print(get_score("training.txt",fre))
   elif i==2:
       print(":))")

tmp_main()


