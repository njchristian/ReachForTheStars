
function loadFile(givenID){
    var f1Text = {};
    var total = 0;
    var oFrame = document.getElementById(givenID);
    var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
    var lines = strRawContents.split("\n");
    for(i = 0; i < lines.length; i++) {
        content = lines[i].split(" ");
        if( content.length < 2 ) continue;
        f1Text[content[0]] = parseInt(content[1]);
        total = total + parseInt(content[1]);
    }
    var index = 0;
    switch( givenID ){
        case "f1":
            index = 0;
            break;
        case "f2":
            index = 1;
            break;
        case "f3":
            index = 2;
            break;
        case "f4":
            index = 3;
            break;
        case "f5":
            index = 4;
            break;
    }
    wordClasses[index] = f1Text;
    totalCounts[index] = total;
    
    console.log("Finished loading " + givenID);
}

function LoadFile1() {
    loadFile("f1");
}
function LoadFile2() {
    loadFile("f2");
}
function LoadFile3() {
    loadFile("f3");
}
function LoadFile4() {
    loadFile("f4");
}
function LoadFile5() {
    loadFile("f5");
}

function LoadPositive() {
    var oFrame = document.getElementById("f6");
    var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
    var lines = strRawContents.split("\n");
    for(i = 0; i < lines.length; i++) {
        positiveWords.push(lines[i]);
    }
}

function LoadNegative() {
    var oFrame = document.getElementById("f7");
    var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
    var lines = strRawContents.split("\n");
    for(i = 0; i < lines.length; i++) {
        negativeWords.push(lines[i]);
    }
}


function get_star_count() {
    if(document.getElementById('group-1-0').checked)
        return 5;
    if(document.getElementById('group-1-1').checked)
        return 4;
    if(document.getElementById('group-1-2').checked)
        return 3;
    if(document.getElementById('group-1-3').checked)
        return 2;
    if(document.getElementById('group-1-4').checked)
        return 1;
}

function get_semantic_score(text) {  

    var filtered_text = "";
    words = text.split(' ');

    for(i = 0; i < words.length; i++) {
        if(positiveWords.indexOf(words[i]) != -1) {
            filtered_text = filtered_text.concat(String(words[i]));
            filtered_text = filtered_text.concat(" ");

        }
        if(negativeWords.indexOf(words[i]) != -1) {
            filtered_text = filtered_text.concat(String(words[i]));
            filtered_text = filtered_text.concat(" ");
        }
    }
    
    return NaiveBayes.naiveBayes(filtered_text);
}

function update_profile(review_text, semantic_score) {
    var words = review_text.split(' ');
    
    var found = 0;

    for(i = 0; i < words.length; i++) {
        if( userWordClasses[semantic_score - 1][words[i]] != null ){
            userWordClasses[semantic_score - 1][words[i]] = userWordClasses[semantic_score - 1][words[i]] + 1;
        }else{
            userWordClasses[semantic_score - 1][words[i]] = 1;
        }
    }
    
    userReviewCount[semantic_score-1] = userReviewCount[semantic_score-1] + 1;
    userTotalCounts[semantic_score-1] = userTotalCounts[semantic_score-1] + words.length;
}

function populate_reviews(review_text, yelp_score) {
    var semantic_score = get_semantic_score(review_text);
    document.getElementById('review_text').value='';
    var content = document.getElementById('user_reviews').innerHTML;
    if(content == "User Profile Currently Empty") {
        content = '<table id="review_content">';
    }
    else {
        content = content.substring(0, content.length - 8);
    }
           
    content += '<tr><td width=50% style="text-align:center">' + review_text + '</td>';
    content += '<td width=25% style="text-align:center">My Score: ' + yelp_score + '</td>';
    content += '<td width=25% style="text-align:center">Predicted Score: ' + semantic_score + '</td></tr>';              

    content += '</table>';

    document.getElementById('user_reviews').innerHTML=content;
    
    update_profile(review_text, yelp_score);
}