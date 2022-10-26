from os import path
import matplotlib.colors
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from statistics import mode, median, mean
from string import punctuation as punctuations
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download("stopwords", quiet=True)

def removeStopWords(wordList: list) -> list:
    """
    Purpose:
        To return stop word removed version of given string array.

    Params
        :param wordList: List to remove stop words from

    Returns
        :returns: List of the strings which aren't stop words

    Examples:
        removeStopWords(["Hello", ",", "my" , "name" , "is", "Yusuf" , "."])
        output : ['Hello', ',', 'name', 'Yusuf', '.']

        removeStopWords(["What" , "'s" , "your" , "name", "my" , "friend" , "?"])
        output : ['name', 'friend', '?']

    """
    stopWordSet = set(stopwords.words('english'))
    stopWordSet.add("'s")
    stopWordSet.add("'m")
    stopWordSet.add("'re")
    processedWordList = [word for word in wordList if word.casefold() not in stopWordSet]
    return processedWordList


def removePunctuations(wordList: list) -> list:
    """
    Purpose:
        To return punctuation removed version of given string array.

    Params
        :param wordList: List to remove punctuations from

    Returns
        :returns: List of the strings which aren't punctuations

    Examples:
        removePunctuations(["Hello", ",", "my" , "name" , "is", "Yusuf" , "."])
        output : ['Hello', 'my', 'name', 'is', 'Yusuf']

        removePunctuations(["What" , "'s" , "your" , "name", "my" , "friend" , "?"])
        output : ['What', "'s", 'your', 'name', 'my', 'friend']
    """

    punctuationSet = set(punctuations)
    processedWordArray = []

    for word in wordList:
        for char in word:
            if char not in punctuationSet:
                processedWordArray.append(word)
                break

    return processedWordArray


def getFrequencyDistribution(wordList: list) -> dict:
    """
        Purpose:
            To find frequencies of given strings.

        Params
            :param wordList: List of strings to find frequencies

        Returns
            :returns: Frequencies of words in a dict with keys as strings and values as frequencies

        Examples:
            getFrequencyDistribution(["Hello" , "Hello" ,"Hello" , "is" ,"is" ,"is" ,"is" ,"is" ,"my","my","my"])
            output : ""{'Hello': 3, 'is': 5, 'my': 3}

            getFrequencyDistribution(["Hello" ,"my", "name", "is", "Yusuf", ".", "I", "'m", "a", "computer", "engineering", "student", "."])
            output : {'Hello': 1, 'my': 1, 'name': 1, 'is': 1, 'Yusuf': 1, '.': 2, 'I': 1, "'m": 1, 'a': 1, 'computer': 1, 'engineering': 1, 'student': 1}

        """
    wordList = [word for word in wordList if type(word) is str]
    frequencyDistribution = FreqDist(wordList)
    return dict(frequencyDistribution)


def getStatistics(frequencyDistribution: dict) -> dict:
    """
        Purpose:
            To find mean, mode and median from given dict of frequencies.

        Params
            :param frequencyDistribution: Dict of frequencies of values

        Returns
            :returns: A dict contains mean, mode and median of given frequencies

        Examples:
            getStatistics({ "the" : 1234, "my" : 546 , "your" : 430 , "film" :42 , "data": 1 , "hello": 1 })
            output : {'mean': 375.6666666666667, 'mode': 1, 'median': 236.0}

            getStatistics({ "1" : 45 , "hello" : 75 , "my": 75 })
            output:{'mean': 65, 'mode': 75, 'median': 75}
        """
    frequencyList = list(frequencyDistribution.values())

    medianOfList = median(frequencyList)
    meanOfList = mean(frequencyList)
    modesOfList = mode(frequencyList)

    return {"mean": meanOfList,
            "mode": modesOfList,
            "median": medianOfList
            }


def createWordCloud(frequencyDistribution: dict, width=800, height=800, minFontSize=10) -> WordCloud:
    """
        Purpose:
            To create a wordcloud with given word and frequency values

        Params:
            :param frequencyDistribution: Dict of frequencies of values
            :param width: Width of word cloud to create (optional, 800 default)
            :param height: Width of word cloud to create (optional, 800 default)
            :param minFontSize: Smallest strings text size (optional, 10 default)

        Returns:
            :returns: A WordCloud object created  from wordcloud module

        Example Usage:
            createWordCloud({ "the" : 1234, "my" : 546 , "your" : 430 , "film" :42 , "data": 1 , "hello": 1 }, 400, 400, 20)

            createWordCloud({ "1" : 45 , "hello" : 75 , "my": 75 })
        """

    return WordCloud(width=width, height=height,
                     background_color='white',
                     colormap=matplotlib.colormaps["plasma"],
                     min_font_size=minFontSize).fit_words(frequencyDistribution)


def saveWordCloud(wordCloud: WordCloud, fileName:str) :
    """
        Purpose:
            To save given wordcloud

        Params:
            :param wordCloud: WordCloud object from wordcloud module

        Returns:
            :returns: A png file of given wordcloud

        Example Usage:
            #saveWordCloud(createWordCloud({ "the" : 1234, "my" : 546 , "your" : 430 , "film" :42 , "data": 1 , "hello": 1 }),fileName="wordcloud")

            #saveWordCloud(createWordCloud({ "1" : 45 , "hello" : 75 , "my": 75 }),fileName="wordcloud")
        """
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordCloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(fileName+".png")

def plotFrequencyGraph(frequencyDistribution: dict, fileName: str, itemCount=0, isPowerGraph=False, drawStats=True, showWords=False):
    """
        Purpose:
        To plot and save frequency graph from given word frequency dict

        Params:
            :param frequencyDistribution: Dict of word and frequencies to plot the graph
            :param isPowerGraph: Bool for specifying type of graph (True for power graph and False for normal scale graph) (Optional, False default)
            :param itemCount: Number of words to plot (Optional, all by default)
            :param drawStats: Bool to determine whether stats should be drawn (Optional, True by default)
            :param showWords: Bool to determine whether words should be drawn (Optional, False by default)
            :param fileName: File name to save graph

        Returns:
            :returns: An image of the graph

        Example Usage:
            plotFrequencyGraph({ "the" : 1234, "my" : 546 , "your" : 430 , "film" :42 , "data": 1 , "hello": 1}, isPowerGraph=True,fileName="graph" )

            plotFrequencyGraph({ "1" : 45 , "hello" : 75 , "my": 75 },fileName="graph")
        """

    height = 8 if showWords else 7
    plt.figure(figsize=(7, height))

    dictSize = len(frequencyDistribution)
    itemCount = dictSize if (itemCount == 0 or itemCount > dictSize) else itemCount

    sortedDict = dict(sorted(frequencyDistribution.items(), key=lambda x: x[1], reverse=True))

    frequencyList = list(sortedDict.values())
    wordList = list(sortedDict.keys())
    plt.plot(wordList[:itemCount], frequencyList[:itemCount])

    if isPowerGraph:
        plt.xscale("symlog")
        plt.yscale("symlog")

    if not showWords:
        plt.xticks([])
        plt.xlabel('Word', fontsize=20)

    plt.xticks(rotation=90)
    plt.ylabel('Frequency', fontsize=20)

    if drawStats:
        stats = getStatistics(frequencyDistribution)
        plt.axhline(y=stats["median"], linestyle='--', linewidth=2.5, label='median', c='blue')
        plt.axhline(y=stats["mean"], linestyle='--', linewidth=2.5, label='mean', c='orange')
        plt.axhline(y=stats["mode"], linestyle='--', linewidth=2.5, label='mode', c='lightgreen')
        plt.legend()

    plt.title("Frequency Distribution", fontdict={'fontsize': 35})
    plt.savefig(fname=""+fileName+".png")


def takeInputsFromUser(inputsToBeTaken : list) -> dict:
    """
    Purpose:
        To get given inputs from user in order

    Input Types:
        "TRUE_FALSE" : This input type asks yes no questions and returns true and false
        "RAW_STRING" : This input type asks any question and returns the string entered by user
        "FILE_NAME" :  This input type asks any question and returns valid file paths

    Params:
        :param inputsToBeTaken:a list of dictionaries in form of {inputName: string(name of the input) ,inputType: one of the types declared above,inputQuestion: string(question to ask for taking input}

    Returns:
        :returns: A dictionary with given inputName strings as keys and taken inputs as values ({inputName1: value1, inputName1:value2})

    Example Usage:
        getInputsFromUser([{inputName: "userName",inputType:"RAW_STRING",inputQuestion: "What's your name"}])

        getInputsFromUser([{inputName: "userAge",inputType:"RAW_STRING",inputQuestion: "How old are you"}])

        getInputsFromUser([{inputName: "isRetired",inputType:"TRUE_FALSE",inputQuestion: "Are you retired"}])
    """
    takenInputs = {}
    for inputToBeTaken in inputsToBeTaken:

        match inputToBeTaken["inputType"]:

            case "TRUE_FALSE":
                takenInputs[inputToBeTaken["inputName"]] = takeTFInput(inputToBeTaken["inputQuestion"])

            case "RAW_STRING":
                takenInputs[inputToBeTaken["inputName"]] = takeRawStringInput(inputToBeTaken["inputQuestion"])

            case "FILE_NAME":
                takenInputs[inputToBeTaken["inputName"]] = takeFilePathInput(inputToBeTaken["inputQuestion"])

    return takenInputs


def takeTFInput(question: str) -> bool:
    """
    Purpose:
        To ask yes no question and take yes or no input from user

    Params:
        :param question: Question to ask for taking input

    Returns:
        :returns: bool(True for yes input, False for no)

    Example Usage:
        takeTFInput("Are you retired")
    """
    isInputValid = False
    while not isInputValid:
        inp = input(question + " (y or n): ")
        match inp.casefold():
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Please enter y or n")


def takeRawStringInput(question: str) -> str:
    """
    Purpose:
        To ask question and take input from user

    Params:
        :param question: Question to ask for taking input

    Returns:
        :returns: string (user input)

    Example Usage:
        takeRawStringInput("How old are you")
    """
    return input(question + " : ")


def takeFilePathInput(question: str) -> str:
    """
    Purpose:
        To ask question and take valid file path from user

    Params:
        :param question: Question to ask for taking input

    Returns:
        :returns: string (validated file path)

    Example Usage:
        takeFilePathInput("How old are you")
    """
    isFilePathValid = False
    while not isFilePathValid:
        filePath = takeRawStringInput(question)
        if path.exists(filePath):
            return filePath
        else:
            print("Please enter a valid file path!")

def tokenizeWordsInFile(filePath: str) -> list:
    """
    Purpose:
        To tokenize words in text file

    Params:
        :param filePath: File path for text file to tokenize words

    Returns:
        :returns: list of strings from text file or false if file isn't text file

    Example Usage:
        tokenizeWordsInFile("/home/usr/Documents/text.txt")
        output: ["Hello" ,"," ,"my" , "name" , "is" , "yusuf" , "."]
    """
    # Getting data from text file and tokenizing it
    try:
        file = open(filePath, "r")
        rawText = file.read()
        return nltk.word_tokenize(rawText)
    except:
        # Handling errors caused by invalid inputs
        return False


isTextAnalyzed = False
analyzeCount = 0
inputsToBeTaken = [{"inputName" :    "filePath",
                    "inputType" :    "FILE_NAME",
                    "inputQuestion": "Please enter path of the file you want to process"},

                   {"inputName" :    "doRemovePunctuations",
                    "inputType" :    "TRUE_FALSE",
                    "inputQuestion": "Do you want to remove punctuations"},

                   {"inputName" :    "doRemoveStopWords",
                    "inputType" :    "TRUE_FALSE",
                    "inputQuestion": "Do you want to remove stop words"}]

while not isTextAnalyzed:
    inputs = takeInputsFromUser(inputsToBeTaken)
    wordList = tokenizeWordsInFile(inputs["filePath"])
    print("Processing...")

    if not wordList:
        print("Error: Cannot read file !")
        continue

    if inputs["doRemovePunctuations"]:
        wordList = removePunctuations(wordList)

    if inputs["doRemoveStopWords"]:
        wordList = removeStopWords(wordList)

    frequencyDist = getFrequencyDistribution(wordList)

    wordCloud = createWordCloud(frequencyDistribution=frequencyDist)
    saveWordCloud(wordCloud, fileName="wordcloud"+str(analyzeCount))

    plotFrequencyGraph(frequencyDistribution=frequencyDist, itemCount=len(frequencyDist), fileName="frequency-graph"+str(analyzeCount))
    plotFrequencyGraph(frequencyDistribution=frequencyDist, itemCount=len(frequencyDist), isPowerGraph=True, fileName="frequency-power-graph"+str(analyzeCount))
    plotFrequencyGraph(frequencyDistribution=frequencyDist, itemCount=15, drawStats=False, showWords=True, fileName="top-15-frequency-graph"+str(analyzeCount))

    print("Saved graphs and wordcloud succesfully !")

    if takeTFInput("Do you want to continue"):
        analyzeCount += 1
        continue

    print("See you later !")
    isTextAnalyzed = True
