import os
import re

profiles = ["Xly4Bgx-ABt2MDEUXgEcXg", "MQ_HhZWWoPyPP1J5qWlypg", "0Zv9HyEs4IMyMW2AspJDYg", "2ecLeSa--N70YeKtQGWsug",
            "wDmXREigSPJX5iHa0PQygg", "_D1zyYMjll4almoGZjBmkA", "9LIZHEHMw2fmwOL25aVw6w", "CKSxuoWOqiZmXR6EAAKgEA", 
            "zdPRXhhJNCiCOgWQwoPlpg", "h3g-GaEFQFzczJiXzIOdaw", "3G34yhhtqed2ASeGfiqS1A", "Ft3BBqjm_ZRcQQ9UAtoJ_g", 
            "YLDNoMCv5lyWKJFqvHfEbA", "69_O4PnPowyjNYlT9BgWZA", "w9FobM_vIS2TH0xU7NPPJA", "uLyqe-WdvTR3eaM3mgoqpw", 
            "airuooZt5UTkFBsVAnMlkQ", "xTWoTGTmm6DUB7bKfOrW9g", "-PS9rTYQPl4R1OceVXfoWQ", "sM3gqadLq4KtCd7BR35nQQ", 
            "nnnV7CGk72vpGLNvaBvvrA", "YVyzM5JuquEGmSxWrlXzeg", "iAUOGnPA0tZJ0SZdbT7q_g", "ONu4VpPJ0P_ZmAP7oOaybA", 
            "mD1uXKXoCgxfpf9wz_1utA", "o7W3M6obikoL9pG81L1J6A", "LYcklDWjV4J5laAQMzakcg" ]
            
f=open('userProfilesFinal.txt','r')

outputFiles = {}
for profile in profiles:
    outputFiles[profile] = []
    for i in range(1,6):
        filename = "userProfiles/" + profile + "/class=" + str(i)
        outputFiles[profile].append(open(filename, 'w+'))
        
for line in f:
    times = []
    arr = re.split('\s+', line)
    word = arr[0][2:-2]
    uid = arr[1][1:-2]
    one = int(arr[2][1:-1])
    two = int(arr[3][:-1])
    three = int(arr[4][:-1])
    four = int(arr[5][:-1])
    five = int(arr[6][:-1])
    times.append(one)
    times.append(two)
    times.append(three)
    times.append(four)
    times.append(five)
    
    for i in range(0,5):
        if times[i]>0:
            outputFiles[uid][i].write(word + ' ' + str(times[i]) + '\n')
    
    
    
    
    
    
    
    