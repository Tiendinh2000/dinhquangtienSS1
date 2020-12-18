import re
import string


def menu_start():
    print("What would you like to do? /n")
    print("1: Get the score of a word")
    print("2: Get the average score of words in a file ")
    print("3: Find the highest / lowest scoring words in a file")
    print("4:Sort the words into positive.txt and negative.txt")
    print("5: Exit")

    i=(input())
    return i

# read file and return frequency of each word in that file
def frequency_dict(object):
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


def get_score(object,fre_dictionary,word):
    file =object
    dic =fre_dictionary

    fre=freq(dic,word)
    temp=0
    mark=0

    with open(file) as f:
            sum=0
            for line in f:
                if word in line:
                    sum=sum+int(line[0])
                    temp+=1
            mark=sum/temp

    return mark

def freq(dic, word):
    f=0
    for k,v in dic.items():
        if k==word:
            return int(v)
            break



def main():
    #1:
    inp=str(menu_start())

    if inp=="1":
      word=str(input())
      fre_dic = frequency_dict("training.txt")

      score= get_score("training.txt", fre_dic, word)
      print("score = {:.2f}".format(score))
    else:
        main()

main()


