import os
import re
            
f=open('collectionClassesFinal.txt','r')

outputFiles = []

for i in range(1,6):
    filename = "collection/class=" + str(i)
    outputFiles.append(open(filename, 'w+'))
        
for line in f:
    times = []
    arr = re.split('\s+', line)
    word = arr[0][2:-2]
    one = int(arr[1][1:-1])
    two = int(arr[2][:-1])
    three = int(arr[3][:-1])
    four = int(arr[4][:-1])
    five = int(arr[5][:-1])
    times.append(one)
    times.append(two)
    times.append(three)
    times.append(four)
    times.append(five)
    
    for i in range(0,5):
        if times[i]>0:
            outputFiles[i].write(word + ' ' + str(times[i]) + '\n')
    
    
    
    
    
    
    
    