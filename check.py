#!/usr/bin/python
""" Check Top 1 Million Alexa websites against Malware  """
__author__ = "Marcin Kozlowski <marcinguy@gmail.com>"


import requests
import json
import csv
import pprint
import numpy as np



data1={
    "threatInfo": {
        "threatEntries": [
        ]
    }
}

headers1 = {'Content-Type': 'application/json'}

result=list()

def showstatus():
    final = dict()

    for item in result:
        try:
            key = item['matches'][0]['threat']['url']
            value = item['matches'][0]['threatType']
            final[key] = value
        except:
            continue

    pprint.pprint(final)

    length = len(final)
    print "Found: "+str(length)
    # Save
    np.save('safebrowsingscan.npy', final)



def sendoff():
    r = requests.post("http://localhost:8080/v4/threatMatches:find", data=json.dumps(data1), headers=headers1)
    #print r.status_code
    jsonstr = r.content
    try:
      result.append(json.loads(jsonstr))
    except ValueError:
      sleep(10);
    else:
      pass
i=0
j=0
with open('top-1m.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        #print row[1]
        data1["threatInfo"]["threatEntries"].append({"url":row[1]})
        if(i==500):
           print "Analyzed: "+str(j)
           sendoff()
           data1={
            "threatInfo": {
                "threatEntries": [
                ]
             }
           }
           showstatus()
           i=0
        i=i+1
        j=j+1

final=dict()

for item in result:
    try:
        key = item['matches'][0]['threat']['url']
        value = item['matches'][0]['threatType']
        final[key]=value
    except:
        continue

#pprint.pprint(final)

lenght=len(final)
print "Found: "+str(lenght)

# Save
np.save('safebrowsingscan.npy', final)


