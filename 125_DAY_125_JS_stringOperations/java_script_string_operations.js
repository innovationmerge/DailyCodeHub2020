// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with JAVA SCRIPT

// Program to explain usage strings in JavaScript

// check if a string starts with another string       
const string = 'iNNovation Merge';
const toCheckString = 'iN';
if(string.startsWith(toCheckString)) {
    console.warn('The string starts with "iN".');
}
else {
    console.warn(`The string does not starts with "iN".`);
}
// Output: The string starts with "iN"

// Convert an object to a string
const tech = {
    bigdata: 'hadoop',
    programming: 'python'
}
const result =  JSON.stringify(tech);
console.log(result);
// Output: {"bigdata":"hadoop","programming":"python"}
console.log(typeof result);
// Output: string



