def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Asian Tigers")

banner("Sun and Moon", border="*")
