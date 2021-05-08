# using generators to find the longest name

def separate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


def getLongest(namelistFile):
    full_name = (name.strip() for name in open(namelistFile))
    names = separate_names(full_name)
    lengths = ((name, len(name)) for name in full_name)
    longest = max(lengths, key=lambda x: x[1])


print(getLongest('names.txt'))
