import sys; args = sys.argv[1:]

reports = open(args[0]).readlines()
safeCount = 0
def validCheck(r):
    if r != sorted(r) and r != sorted(r, reverse=True):
        return False
    for i in range(len(r) - 1):
        if not 1 <= abs(r[i] - r[i + 1]) <= 3:
            return False
    return True

for rStr in reports:
    r = [int(i) for i in rStr.split()]
    nbrs = [r[:i] + r[i+1:]  for i in range(len(r))]
    valid = False
    for nbr in nbrs:
        print(nbr)
        if validCheck(nbr):
            valid = True
            break
    safeCount += valid
print(safeCount)
