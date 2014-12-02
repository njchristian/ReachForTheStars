one_star_words = [];
two_star_words = [];
three_star_words = [];
four_star_words = [];
five_star_words = [];

var allText = []; // this will be what you want to access

function loadFile(givenID){
    f1Text = [];
    var oFrame = document.getElementById(givenID);
    var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
    var lines = strRawContents.split("\n");
    for(i = 0; i < lines.length; i++) {
        content = lines[i].split(" ");
        f1Text.push([content[0], content[1]]);
    }
    allText.push(f1Text);
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

function get_semantic_score() {    
    return Math.floor(Math.random() * 5) + 1
}

function update_profile(review_text, semantic_score) {
    var words = review_text.split(/\W+/);
    
    var found = 0;

    for(i = 0; i < words.length; i++) {
        if(semantic_score == 1) {
            for(j = 0; j < one_star_words.length; j++) {
                if(one_star_words[j][0] == words[i]) {
                    one_star_words[j][1] = one_star_words[j][1] + 1;
                    found = 1;
                }
            }
            if(found < 1 && words[i] != "") {
                one_star_words.push([words[i], 1]);
            }
        }
        if(semantic_score == 2) {
            for(j = 0; j < two_star_words.length; j++) {
                if(two_star_words[j][0] == words[i]) {
                    two_star_words[j][1] = two_star_words[j][1] + 1;
                    found = 1;
                }
            }
            if(found < 1 && words[i] != "") {
                two_star_words.push([words[i], 1]);
            }
        }
        if(semantic_score == 3) {
            for(j = 0; j < three_star_words.length; j++) {
                if(three_star_words[j][0] == words[i]) {
                    three_star_words[j][1] = three_star_words[j][1] + 1;
                    found = 1;
                }
            }
            if(found < 1 && words[i] != "") {
                three_star_words.push([words[i], 1]);
            }
        }
        if(semantic_score == 4) {
            for(j = 0; j < four_star_words.length; j++) {
                if(four_star_words[j][0] == words[i]) {
                    four_star_words[j][1] = four_star_words[j][1] + 1;
                    found = 1;
                }
            }
            if(found < 1 && words[i] != "") {
                four_star_words.push([words[i], 1]);
            }
        }
        if(semantic_score == 5) {
            for(j = 0; j < five_star_words.length; j++) {
                if(five_star_words[j][0] == words[i]) {
                    five_star_words[j][1] = five_star_words[j][1] + 1;
                    found = 1;
                }
            }
            if(found < 1 && words[i] != "") {
                five_star_words.push([words[i], 1]);
            }
        }
    }
}

function populate_reviews(review_text, yelp_score, semantic_score) {
    document.getElementById('review_text').value='';
    var content = document.getElementById('user_reviews').innerHTML;
    if(content == "User Profile Currently Empty") {
        content = '<table id="review_content">';
    }
    else {
        content = content.substring(0, content.length - 8);
    }
           
    content += '<tr><td width=50% style="text-align:center">' + review_text + '</td>';
    content += '<td width=25% style="text-align:center">Yelp Score: ' + yelp_score + '</td>';
    content += '<td width=25% style="text-align:center">Semantic Score: ' + semantic_score + '</td></tr>';              

    content += '</table>';

    document.getElementById('user_reviews').innerHTML=content;
    
    update_profile(review_text, semantic_score);
}