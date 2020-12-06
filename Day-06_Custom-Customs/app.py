import os
dirname = os.path.dirname(os.path.realpath(__file__))

answers = set()
answers_count = 0
empty = True
f = open(dirname + "/input.txt", "r")
for l in f.readlines():
    line = l.strip()
    if len(line) == 0:
        empty = True
        answers_count += len(answers)
        continue

    if empty:
        answers = set(line)
        empty = False
    else:
        answers = answers & set(line)

answers_count += len(answers)

print("Total questions to which everyone answered 'yes'", answers_count)
