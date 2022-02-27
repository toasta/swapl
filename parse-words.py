import fileinput
import re
import json

words = []

cutoff = 10
for line in fileinput.input():
  if len(line) <= cutoff:
    continue
  line = line.rstrip().lower()
  if re.match(r'^[a-z]+$', line):
    words.append(line)
print(json.dumps(words, indent=1))
