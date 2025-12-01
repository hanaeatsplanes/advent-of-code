import re
import sys; args = sys.argv[1:]

instructions = open(args[0]).readlines()
for inst in instructions:
    for i in re.match(r"mul(\d{1-3},\d{1-3})"):
        x, y = re.match("mul\((\d{1,3}),(\d{1,3})\)", i).groups()
