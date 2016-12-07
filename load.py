#!/usr/bin/python
""" Count malware sites  """
__author__ = "Marcin Kozlowski <marcinguy@gmail.com>"

import pprint
import numpy as np


read_dictionary = np.load('safebrowsingscan.npy').item()

my_list = []

for key in read_dictionary:
    if read_dictionary[key] == 'MALWARE':
        my_list.append(key)


malware=len(my_list)

print("Malware count:"+str(malware))

file = open("results.txt","w")

for item in my_list:
  file.write(item+"\n")

file.close()

