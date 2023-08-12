#!/usr/bin/env python3

import os

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

count = 1

lines = open('Readme.md').read().split("\n")
output = []

for line in lines:
    if line.startswith('### Aula'):
        # remove number after 'Aula' and insert new number
        parts = line.split(' ')
        if is_number(parts[2]):
            del parts[2]
        # format count with 2 digits
        parts.insert(2, str(count).zfill(2))
        count += 1
        line = ' '.join(parts)
        print(line)
    output.append(line)

with open('Readme.md', 'w') as f:
    f.write('\n'.join(output))
