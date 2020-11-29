// iNNovationMerge
// English Linter using Node

//npm install write-good

var writeGood = require('write-good');
var suggestions = writeGood('So the cat was stolen.');
resultString = ""
for(k=0;k<suggestions.length;k++){
    position = suggestions[k]['index']+suggestions[k]['offset']
    resultString = resultString + "Position: "+ position + "\n" + 
    "Reason: "+ suggestions[k]['reason'] + "\n\n"
    console.log(resultString)
}
/*
Position: 2
Reason: "So" adds no meaning

Position: 2
Reason: "So" adds no meaning

Position: 21
Reason: "was stolen" may be passive voice
*/