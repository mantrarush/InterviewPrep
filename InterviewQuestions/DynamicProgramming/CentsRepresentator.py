#calculate the number of ways to get n cents (25,10,5,1)
def representCents(remainingCents: int, moves: str, ways: {int: int}) -> int:
    if remainingCents == 0:
        return 1

    if remainingCents < 0:
        return 0
    try:
        return ways[remainingCents]
    except:
        ways[remainingCents] = representCents(remainingCents - 1, moves + "1 ", ways) + representCents(remainingCents - 5, moves + "5 ", ways) + representCents(remainingCents - 10, moves + "10 ",  ways) + representCents(remainingCents - 25,  moves + "25 ", ways)
    return ways[remainingCents]

def representCentsMain(cents: int) -> int:
    return representCents(remainingCents = cents , moves = "", ways = {})

print(representCentsMain(101))
