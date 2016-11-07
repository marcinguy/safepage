import pprint
import numpy as np


read_dictionary = np.load('safebrowsingscan.npy').item()

my_list = []

for key in read_dictionary:
    if read_dictionary[key] == 'MALWARE':
        my_list.append(key)


malware=len(my_list)

print("Malware count:"+str(malware))
