import math
import re

class CoreNaiveBayes(object):
    @staticmethod
    def pWordIn(word, wordClass, wordCountForClass):
        if word in wordClass.keys():
            wc = wordClass[word]
            return float(wc)/float(wordCountForClass)
        else:
            return 0
        
    @staticmethod
    def initWordCounts():
        
        infilename = "collection/"
        
        classes = []
        totals = []
        
        #create a different count for each class
        for i in range(0,5):
            cs = "class=" + str(i+1)
            f=open(infilename + cs,'r')
            total = 0
            classes.append({})
            for line in f:
                arr = re.split('\s+', line)
                classes[i][arr[0]] = int(arr[1])
                total = total + int(arr[1])
                
            totals.append(total)
                
        return classes, totals
            
    @staticmethod
    def initWordCountsForUser(uid):
        
        infilename = "userProfiles/"+uid+"/"
        
        classes = []
        totals = []
        
        #create a different count for each class
        for i in range(0,5):
            cs = "class=" + str(i+1)
            f=open(infilename + cs,'r')
            total = 0
            classes.append({})
            for line in f:
                arr = re.split('\s+', line)
                if len(arr) < 2:
                    continue
                classes[i][arr[0]] = int(arr[1])
                total = total + int(arr[1])
                
            totals.append(total)
                
        return classes, totals
        
    @staticmethod
    def pClassFor(classNum, review, wordClass, wordCountForClass):
        
        p = 0
        
        wordCounts = []
        
        for word in re.findall(r'\w+',review.lower()):
            
            wp = CoreNaiveBayes.pWordIn(word, wordClass, wordCountForClass)
            #print wp
            if wp != 0:
                p = p + math.log(wp)
            
        return p
        
        
    #take in a review and reviewer, and return a semantic class!
    @staticmethod
    def naiveBayes(review, reviewerId):
        
        wordClasses, totalCounts = CoreNaiveBayes.initWordCounts()
        
        userWordClasses, userTotalCounts = CoreNaiveBayes.initWordCountsForUser(reviewerId)
        
        alpha = .5
        
        classProbabilities = []
        
        #Go through each class to determine the best fit
        for i in range(1,6):
        
            d = CoreNaiveBayes.pClassFor(i, review, wordClasses[i-1], totalCounts[i-1])
            u = CoreNaiveBayes.pClassFor(i, review, userWordClasses[i-1], userTotalCounts[i-1])
            
            #print d
            #print u
            
            p = alpha * d + (1-alpha) * u
            
            classProbabilities.append(p)
            
            #print p
            
            
        maxIndex = 0
        max = classProbabilities[0]
        i = 0
        for c in classProbabilities:
            if c > max:
                maxIndex = i
                max = c
            i+=1
            
        return maxIndex + 1
        
        
        
        
        