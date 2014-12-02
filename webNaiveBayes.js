
window.onload = function(){
    NaiveBayes.initWordCounts();
}

var wordClasses = [];
var totalCounts = [];

var starDistribution = [.1, .09, .15, .3, .36];

function readTextFile(file, callback)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                callback(allText)l
            }
        }
    }
    rawFile.send();
}

NaiveBayes.pWordIn = function(word, wordClass, wordCountForClass){

    if( wordClass[word] != null ){
        var wc = wordClass[word];
        return wc/wordCountForClass;
    }
    return 0;
}  

NaiveBayes.initWordCounts = function(){
    
    var infilename = "collection/";
    
    var classes = [];
    var totals = [];
    
    #create a different count for each class
    for( var i = 0; i < 5; ++i ){
    
        cs = "class=" + str(i+1)
        f=open(infilename + cs,'r')
        
        var total = 0;
        classes.push({});
        
        for line in f
        {
            var arr = line.split('\s+');
            classes[i][arr[0]] = parseInt(arr[1]);
            total = total + parseInt(arr[1]);
        }
            
        totals.push(total);
    }
}


NaiveBayes.pClassFor = function(classNum, review, wordClass, wordCountForClass){
    
    var p = 0
    
    var wordCounts = []
    
    var words = review.toLowerCase().split('\w+');
    
    for( var i = 0; i < words.length; i++ ){
        
        var word = words[i];
        
        var wp = CoreNaiveBayes.pWordIn(word, wordClass, wordCountForClass);
        
        if( wp != 0 ){
            p = p + log(wp);
        }
            
    }
        
    return p + log(starDistribution[classNum-1]);
}
    
NaiveBayes.naiveBayes = function(review){
    
    //wordClasses, totalCounts = CoreNaiveBayes.initWordCounts()
    
    //userWordClasses, userTotalCounts = CoreNaiveBayes.initWordCountsForUser(reviewerId)
    
    var alpha = .5;
    
    var classProbabilities = [];
    
    for( var i = 1; i < 6; ++i ){
    
        var d = CoreNaiveBayes.pClassFor(i, review, wordClasses[i-1], totalCounts[i-1])
        var u = CoreNaiveBayes.pClassFor(i, review, userWordClasses[i-1], userTotalCounts[i-1])
        
        
        var p = alpha * d + (1-alpha) * u;
        
        classProbabilities.push(p);
        
    }
        
    var maxIndex = 0;
    var max = classProbabilities[0];
    var i = 0;
    for( var i = 0; i < classProbabilities.length; ++i ){
        var c = classProbabalities[i];
        if (c > max){
            maxIndex = i;
            max = c;
        }
    }
        
    return maxIndex + 1;
}
        
        
        
        