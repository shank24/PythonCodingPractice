DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4'
}


def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion Executed! x = {x}")
    except (KeyError, TypeError):
        pass
    return x



var = convert("one two three".split())
wer = convert("threee".split())
print(var, wer)
