from coreNaiveBayes import CoreNaiveBayes
import re


def getReviewFromFile(rid):
    
    f = open('targetReviews.txt', 'r')
    
    for line in f:
        #print rid
        #print line[2:24]
        if rid == line[2:24]:
            return int(line[28:29]),line[32:-2]
            
    return ""
    

def main():
    
    
    ifn = 'businessReviewMap.txt'
    f = open(ifn, 'r')
    
    currentOutput = 0
    currentBusiness = "first"
    currentCum = 0
    currentReviews = 0
    
    wordClasses, totals = CoreNaiveBayes.initNB()
    
    for line in f:
        
        arr = re.split('\s+', line)
        bid = arr[0][1:-1]
        rid = arr[1][2:-2]
        uid = arr[2][1:-2]
        
        yelpScore, review = getReviewFromFile(rid)
        
        if bid == currentBusiness:
            currentReviews+=1
            score = CoreNaiveBayes.naiveBayes(review, uid, wordClasses, totals)
            currentCum += score
        
        else:
            if currentBusiness!="first":
                print "Average for " + currentBusiness + " was: " + str(currentCum/currentReviews)
            
            currentOutput = open('businesses/'+bid, 'w')
            currentBusiness = bid
            currentReviews = 1
            score = CoreNaiveBayes.naiveBayes(review, uid, wordClasses, totals)
            currentCum = score
        
        currentOutput.write(review + "\nYelp: " + str(yelpScore) + " Semantic: " + str(score) + '\n')
            
    print "Average for " + currentBusiness + " was: " + str(currentCum/currentReviews)
 
def simpleTest():
    review = "She has 2 yelps read both all negative reviews STAY AWAY FROM THIS place , she does terrible quality clumpy lashes that destroy your natural lashes , uses the cheapest quality products available , pretends to know what she is doing , at the Same time as my eyelash apt I wanted my $500 (just for the hair ) ext removed and redone , she destroyed my hair and my extensions , she cut them behind me so I couldn't see what she was doing , she put a full head of keratin tip ext in that FELL OUT THE NEXT DAY ! All of them. Anyone who knows about these type of ext knows that this is crazy , she already had my credit card info for\nThe lash service and charged me another 450$ to destroy my hair , chunks were broken and destroyed , Aiesha response when I asked her to refund my $ or at least replace the $500 hair she ruined , her response was when you left my salon you had extensions so my job was done . No refund it took me 7 hours to do your hair and I will not give a refund (keep in mind I was only there for the hair part for about 4 hours in rich she took about 7 cigarette breaks and a visit from her boyfriend who brought her a \"blunt \" to smoke to help her relax because she was having a hard time w my hair WTF??!!!!  She went on and on about how she was trained and skilled in this new bonding technology when she clearly didn't even know how to use the tool . She was rude and belligerent and completely unprofessional , anyone can rent a spot throw a chair and a mirror up and pretend they know what there doing . Do your research . Hopefully people will see all the horrible reviews she has gotten and learn from our suffering . She is a terrible business person . I to own my own business and it's always worth it to make the customer happy to keep a good reputation and word of mouth , she Obviously has no concern of her clients . SHADY SHADY SHADY - and her lashes are NOT mink , there cheap plastic and her glue is disgusting . Thank god I now have a real professional to do my lashes . Hopefully help will allow me to post pics for you guys to see the damage and her so called work :( she uses my picture on her fb without my permission . Aliesha Latoyes what ever the hell your name is find another line of work cause this is not ok what you do to\nYour customers . Please see the pictures I post"
    uid = "9LIZHEHMw2fmwOL25aVw6w"
    a, b = CoreNaiveBayse.initNB()
    cl = CoreNaiveBayes.naiveBayes(review, uid, a, b)
    
    print "Semantic Score: " + str(cl)

main()