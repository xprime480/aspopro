#!/bin/bash

echo "" >> a.txt
echo "" >> b.txt
paste -d '\n' a.txt b.txt | grep -v "^$" > c.txt
python3 ./mpl.py a.txt b.txt c.txt
