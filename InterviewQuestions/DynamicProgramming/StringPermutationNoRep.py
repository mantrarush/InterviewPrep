def permuteV2(input: str) -> [str]:
    if len(input) == 2:
        return [input, input[::-1]]
    characters = list(input)
    answers = []
    for char in characters:
        stringToPermuteNext = "".join(input.split(char))
        permutations = permuteV2(stringToPermuteNext)
        answers = answers + [char + permutation for permutation in permutations]

    return answers

print(permuteV2("antx"))
