#! /bin/bash

mkdir -p external

O=external/jquery-3.6.0.min.js
if [ ! -s $O ]; then
  wget -O $O 'https://code.jquery.com/jquery-3.6.0.min.js'
fi
O=external/live.js
if [ ! -s $O ]; then
  wget -O $O https://livejs.com/live.js
fi
