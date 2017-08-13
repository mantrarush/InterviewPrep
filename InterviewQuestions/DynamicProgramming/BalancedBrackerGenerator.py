# Given an integer: n generate all possible combinations of balanced brackets containing n pairs of brackets.

def generate(pairs: int, stream: str, stack: str, answers: [str]):
    if pairs == 0 and len(stack) == 0 and stream not in answers:
        answers.append(stream)
        return

    if len(stack) > pairs:
        return

    # Open
    generate(pairs = pairs, stream = stream + "{", stack = stack+"{", answers=answers)

    # Close
    if len(stack) > 0:
        generate(pairs=pairs - 1, stream=stream + "}", stack = stack[:-1], answers=answers)


def generateMain(pairs: int) -> [str]:
    answers = []
    generate(pairs=pairs, stream = "{", stack = "{", answers = answers)
    return answers

print(generateMain(5))


'''
genMain(2):
    generate(2, "{", "{", [])
        generate(2, "{{", "{{", [])
            generate(2, "{{{", "{{{", [])
                END
            generate(1, "{{}", {, [])
                generate(1, "{{}{", "{{", [])
                    END
                generate(0, "{{}}", "", [])
                    APPENDED "{{}}
                    END
        generate(1, "{{}", "{", ["{{}}"]
            MEMO 35
            END
    generate(1, "{}", "", ["{{}}"]
        generate(1, "{}{", "{", ["{{}}"]
            generate(1, "{}{{", "{{", ["{{}}"]
                END
            generate(0, "{}{}", "", ["{{}}"]
                APPENDED "{}{}"
                END
'''