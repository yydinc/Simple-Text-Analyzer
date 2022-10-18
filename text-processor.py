import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from statistics import mode , median , mean
from string import punctuation as punctuations
nltk.download("stopwords")

#Defining functions

def removeStopWords(wordArray):
    stopWordSet = set(stopwords.words('english'))
    processedWordArray = [word for word in wordArray if word.casefold() not in stopWordSet]
    return processedWordArray


def removePunctuations(wordArray):
    punctuationSet = set(punctuations)
    processedWordArray = []

    for word in wordArray:
        for char in word:
            if char not in punctuationSet:
                processedWordArray.append(word)
                break

    return processedWordArray


def getFrequencyDistribution(wordArray):
    frequencyDistribution = FreqDist(wordArray)
    return frequencyDistribution


def getStatistics(frequencyDist):
    frequencySet = list(frequencyDist.values())

    medianOfSet = median(frequencySet)
    meanOfSet = mean(frequencySet)
    modesOfSet = mode(frequencySet)

    return {"mean": meanOfSet,
            "mode": modesOfSet,
            "median": medianOfSet
            }


#Declaring variables

isProgramRunning = True
isFileFound = False

while isProgramRunning:

    while not isFileFound:

        fileName = input("Please enter path of the file you want to process: ")

        #Closing program if user input is quit (case-insensitive)
        if fileName.casefold() == "quit":
            quit()

        #Getting data from text file and tokenizing it
        try:
            file = open(fileName , "r")
            rawText = file.read()
            tokenizedText = nltk.word_tokenize(rawText)
            isFileFound = True

        #Handling errors caused by invalid inputs
        except :
            print("Please enter a valid file path (or type quit to close the program) !")

    print("1.Remove Stop Words")
    print("2.Remove Punctuations")
    print("3.Get Frequency Distribution Graph")
    print("4.Get Statistics (mean , mode , median)")
    print("0.Exit\n")
    operations = input("Enter code of the operations you want with 1 space between each operation (example: 1 2): ")
    textToProcess = tokenizedText

    #Processing user input and running functions that user requested
    for operation in operations.split(" "):

        match operation:

            case "0":

                print("See u :)")
                isProgramRunning = False

            case "1":

                textToProcess = removeStopWords(textToProcess)

            case "2":

                textToProcess = removePunctuations(textToProcess)

            case "3":

                getFrequencyDistribution(textToProcess).plot(10)

            case "4":

                print(getStatistics(getFrequencyDistribution(textToProcess)))

            case _:

                print("Code you entered ({}) is invalid".format(operation))
                break
