import math
import re

def pWordIn(word, wordClass, wordCountForClass):
    wc = wordClass[word]
    return wc/wordCountForClass
    
def initWordCounts:
    
    infilename = "collection/"
    
    classes = []
    totals = []
    
    #create a different count for each class
    for i in range(0..5):
        cs = "class=" + str(i)
        f=open(infilename + cs,'r')
        total = 0
        
        for line in f:
            arr = re.split('\s+', line)
            classes[i][arr[0]] = int(arr[1])
            total = total + int(arr[1])
            
        totals.append(total)
            
    return classes, totals
        
def initWordCountsForUser(uid):
    
    infilename = "userProfiles/uid/"
    
    classes = []
    totals = []
    
    #create a different count for each class
    for i in range(0..5):
        cs = "_class" + str(i)
        f=open(infilename + cs,'r')
        total = 0
        
        for line in f:
            arr = re.split('\s+', line)
            classes[i][arr[0]] = int(arr[1])
            total = total + int(arr[1])
            
        totals.append(total)
            
    return classes, totals

def pClassFor(classNum, review, wordClass, wordCountForClass):
    
    p = 1
    
    wordCounts = []
    
    for word in review:
        p = p + math.log(pWordIn(word, wordClass, wordCountForClass))
        
    return p
    
    
#take in a location id, and return a semantic class!
def naiveBayes(review, locationId, reviewerId):
    
    wordClasses, totalCounts = initWordCounts()
    
    userWordClasses, userTotalCounts = initWordCountsForUser(reviewerId)
    
    alpha = .5
    
    classProbabilities = []
    
    #Go through each class to determine the best fit
    for i in range(1..6):
    
        d = pClassFor(i, review, wordClasses[i-1], totalCounts[i-1])
        u = pClassFor(i, review, userWordClasses[i-1], userTotalCounts[i-1])
        
        p = alpha * d + (1-alpha) * u
        
        classProbabilites.append(p)
        
        
    maxIndex = 0
    max = classProbabilities[0]
    i = 0
    for c in classProbabilites:
        if c > max:
            maxIndex = i
            max = c
        i+=1
        
    return maxIndex + 1
        
        
        
        
        