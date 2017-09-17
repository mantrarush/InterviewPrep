"""
Given an array of n distinct non-empty strings,
you need to generate minimal possible abbreviations
for every word following rules below.

Begin with the first character and then the number of
characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share
the same abbreviation, a longer prefix is used instead of only
the first character until making the map from word to abbreviation
become unique. In other words, a final abbreviation cannot
map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep
it as original.
Example:
arr: ["like", "god", "internal", "me", "lake", "interval", "lime", "face", "intrusion"]
ans: ["l2e","god","internal","me","l2e","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.

internal, god, like, interval, intebrzl, ...

in5l, god, like, in5l, in5l
"""

class Solution(object):
    def wordsAbbreviation(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        ans = []
        prefixes = []

        for word in arr:
            abbreviation = self.makeAbbreviation(word, 1)
            prefixes.append(1)
            ans.append(abbreviation)

        index = 0
        while index < len(arr):
            needsToComplete = True
            while needsToComplete:
                integer_set = set([index])
                internal_index = index + 1
                while internal_index < len(arr):
                    if ans[internal_index] == ans[index]:
                        integer_set.add(internal_index)
                    internal_index += 1

                if len(integer_set) > 1:
                    needsToComplete = True
                    for integer in integer_set:
                        ans[integer] = self.makeAbbreviation(arr[integer], prefixes[integer] + 1)
                        prefixes[integer] += 1
                else:
                    needsToComplete = False

            index = index + 1
        return ans


    def makeAbbreviation(self, word: str, size: int) -> str:
        if size >= len(word) - 2:
            return word
        retString = ""
        retString += word[0:size]
        retString += str(len(word) - 1 - size)
        retString += word[-1]
        return retString

print(Solution().wordsAbbreviation(["internal", "interval", "god", "like", "intebrzl", "intebtzl"]))
