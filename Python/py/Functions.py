def countWordsFromFile():
    filename = input('enter the filename : ')
    noOfWords = 0
    file=open(filename,"r")
    for line in file:
        word = line.split()
        noOfWords=noOfWords+len(word)
    print("Number Of Words : ")
    print(noOfWords)

countWordsFromFile()