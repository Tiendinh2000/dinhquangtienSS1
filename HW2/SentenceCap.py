if __name__ == '__main__':
    string = input("enter a paragraph:")

    S = string.split()
    # l=['toi',"ten.","tien",'ba?','jhad.']
    firstWord = S[0].capitalize()
    S[0] = firstWord
    for i in range(0, len(S) - 1):
        newS = ''
        if S[i][len(S[i]) - 1] == '.' or S[i][len(S[i]) - 1] == '!' or S[i][len(S[i]) - 1] == '?':
            newS = S[i + 1].capitalize()
            S[i + 1] = newS

    for i in range(0, len(S)):
        print(S[i], end=' ')