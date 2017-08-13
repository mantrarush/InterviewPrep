def permute(input: str) -> [str]:
    if len(input) == 2:
        return [input, input[1]+input[0]]
    charToAdd = input[0]    # "a"
    restString = input[1:]  # "ntx"
    permutations = permute(restString)
    return [charToAdd + permutation for permutation in permutations]

def superPerm(input: str) -> [str]:
    characters = list(input)
    answers = []
    # for char in characters:
    #     restString = input.
    for char in characters:
        permutations = permute(char + "".join(input.split(char)))
        for word in permutations:
            answers.append(word)

    return answers

# a n t
# n a t
# t a n

print(permute("antx"))




