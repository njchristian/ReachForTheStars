var wordClasses = [{},{},{},{},{}];
var totalCounts = [0,0,0,0,0];

var starDistribution = [.1, .09, .15, .3, .36];

var userWordClasses = [{},{},{},{},{}];
var userTotalCounts = [0,0,0,0,0];

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
                callback(allText);
            }
        }
    }
    rawFile.send();
}

NaiveBayes = function(){

}

NaiveBayes.pWordIn = function(word, wordClass, wordCountForClass){

    if( wordClass[word] != null ){
        var wc = wordClass[word];
        return wc/wordCountForClass;
    }
    return 0;
}  


NaiveBayes.pClassFor = function(classNum, review, wordClass, wordCountForClass){
    
    var p = 0
    
    var wordCounts = []
    
    var words = review.toLowerCase().split(' ');
    
    for( var i = 0; i < words.length; i++ ){
        
        var word = words[i];
        
        var wp = NaiveBayes.pWordIn(word, wordClass, wordCountForClass);
        
        if( wp != 0 ){
            p = p + Math.log(wp);
        }
            
    }
        
    return p + Math.log(starDistribution[classNum-1]);
}
    
NaiveBayes.naiveBayes = function(review){
    
    //wordClasses, totalCounts = CoreNaiveBayes.initWordCounts()
    
    //userWordClasses, userTotalCounts = CoreNaiveBayes.initWordCountsForUser(reviewerId)
    
    var alpha = .5;
    
    var classProbabilities = [];
    
    for( var i = 1; i < 6; ++i ){
    
        var d = NaiveBayes.pClassFor(i, review, wordClasses[i-1], totalCounts[i-1])
        var u = NaiveBayes.pClassFor(i, review, userWordClasses[i-1], userTotalCounts[i-1])
        
        
        var p = alpha * Math.exp(d) + (1-alpha) * Math.exp(u);
        
        classProbabilities.push(p);
        
    }
        
    var maxIndex = 0;
    var max = classProbabilities[0];
    var i = 0;
    for( var i = 0; i < classProbabilities.length; ++i ){
        var c = classProbabilities[i];
        if (c > max){
            maxIndex = i;
            max = c;
        }
    }
        
    var ele = document.getElementById('w_count');
    ele.value = maxIndex + 1;   
    
    return maxIndex + 1;
}
        
        
        
        