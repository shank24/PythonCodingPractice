import re

def put_Space(input):

    words = re.findall('[A-Z][a-z]*',input)

    for i in range(0,len(words)):
        words[i] = words[i][0].lower()+words[i][1:]
    print(' '.join(words))


input = 'BruceWayneIsBatman'
put_Space(input)