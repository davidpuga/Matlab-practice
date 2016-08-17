#!/usr/bin/env python

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_305519.txt" 
handle = open(name)
num = list()
for line in handle:
	num_str = re.findall("\d+", line)
	if len(num_str) <= 0:continue 
	for strings in num_str:
		number = int(strings)
		num.append(number)
total = sum(num)
print total
print hello
