import os
from validators import validate

dirname = os.path.dirname(os.path.realpath(__file__))
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
required_fields = fields[:-1]


def count_valid_fields(line):
    counter = 0
    data = line.split(' ')
    for d in data:
        parts = d.rstrip('\r\n\t').strip().split(':')
        if parts[0] in required_fields:
            res = validate(parts[0], parts[1])
            if res:
                counter += 1
    return counter


f = open(dirname + "/input.txt", "r")
valid_passports = 0
valid_fields_counter = 0
for l in f.readlines():
    line = l.rstrip('\r\n\t').strip()
    if len(line) == 0:
        if valid_fields_counter >= len(required_fields):
            valid_passports += 1
        valid_fields_counter = 0
        continue
    valid_fields_counter += count_valid_fields(line)

print("Valid passports:", valid_passports)
