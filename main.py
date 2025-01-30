def main():
     printReport()


def printReport():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            count = getWordCount(file_contents)        
            charCount = getCharacterCount(file_contents)

            print ("--- Begin report of books/frankenstein.txt ---")
            print(f"{count} words found in the document")
            print()
            for item in charCount:
                if item.isalpha():
                    print(f"The '{item}' character was found {charCount[item]} times")

def getWordCount(inputString):
    words = inputString.split()
    count = len(words)
    return count

def getCharacterCount(inputString):
    characterCounts = {}
    for char in inputString:
        lowered = char.lower()

        if lowered in characterCounts:
            characterCounts[lowered] = characterCounts[lowered] +1
        else:
            characterCounts[lowered] = 1
    return characterCounts


main()