#method to sort array of strings so that all anagrams are next to each other


def groupByAnagram(text: [str]) -> [str]:
    # Keys -> sortedString: values are [strings]
    anagramTable = {}

    for word in text:
        chars = list(word)
        chars.sort()
        sortedString = "".join(chars)
        if sortedString in anagramTable:
            anagramTable[sortedString].append(word)
        else:
            anagramTable[sortedString] = [ word ]

    anagramsGrouped = []
    for anagrams in anagramTable.values():
        anagramsGrouped = anagramsGrouped + anagrams

    return anagramsGrouped

