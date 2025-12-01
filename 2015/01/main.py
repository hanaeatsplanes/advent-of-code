import sys; args = sys.argv[1:]
inst = open(args[0]).read()
print(sum(1 if i == "(" else -1 for i in inst))