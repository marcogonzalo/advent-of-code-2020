import input

def _indexes(word, character):
    return [i for i, x in enumerate(word) if x == character]

def get_matches(policy, indexes):
    matches = []
    for p in policy:
        pos = int(p)
        if pos -1 in indexes:
            matches.append(pos)
    return matches

def validate_password(row):
    row_parts = row.split(':')
    policy = row_parts[0]
    password = row_parts[1].strip()
    policy_parts = policy.split(' ')
    positions = policy_parts[0].split('-')
    indexes = _indexes(password, policy_parts[1])
    matches = get_matches(positions, indexes)

    return len(matches) == 1

counter = 0
for v in input.values:
    if validate_password(v):
        counter = counter + 1

print("Valid passwords:", counter)
