import sys; args = sys.argv[1:]

search = open(args[0]).readlines()
lineLen = len(search[0])
search = '\n'.join(search)
sum = search.count("XMAS") + search.count("SAMX")

