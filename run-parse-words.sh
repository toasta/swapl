#! /bin/bash


mkdir -p dyn


cat /usr/share/dict/ngerman | \
  python3 parse-words.py > dyn/wlist.json
