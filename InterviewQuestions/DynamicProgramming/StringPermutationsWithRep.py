def permute(input: str) -> [str]:
    if len(input) == 2:
        return [input, input[::-1]]
    characters = list(input)
    answers = set()
    charHash = {}
    for charIndex in range(len(characters)):
        if characters[charIndex] not in charHash:
            charHash[characters[charIndex]] = True
            prefix = input[:charIndex] if charIndex > 0 else ""
            suffix = input[charIndex + 1: ] if charIndex < len(characters) - 1 else ""
            permutations = permute(prefix + suffix)
            answers = answers.union(set([characters[charIndex] + permutation for permutation in permutations]))

    return list(answers)

permutations = permute("anatx")
print(permutations)
for permutation in permutations:
    permutations.remove(permutation)
    if permutation in permutations:
        print("Found duplicate of " + permutation)

