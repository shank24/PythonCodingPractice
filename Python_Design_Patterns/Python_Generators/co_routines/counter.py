def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No Match')
            else:
                print('Not a String')
    except GeneratorExit:
        print(count)


c = counter('California')
c.next()
c.send('Cali')
