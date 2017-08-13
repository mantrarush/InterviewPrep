def permute(input: str) -> [str]:
    if len(input) == 2:
        return [input, input[::-1]]
    characters = list(input)
    answers = []
    for character in characters:
        permutations = permute("".join(input.split(character)))
        answers = answers + [character + permutation for permutation in permutations]

    return answers

print(permute("antx"))
