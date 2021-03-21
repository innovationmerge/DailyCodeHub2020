// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with JAVA SCRIPT

// Program to explain usage of local storage in JavaScript

// Code             
// Single Variable                           
localStorage.setItem('tech', 'bigdata');
console.log(localStorage.getItem('tech'))            
                        // Output: bigdata

// Object example
localStorage.setItem('user', JSON.stringify({
    username: 'username1',
    api_key: 'axb124dasfasfas'
}));
var user = JSON.parse(localStorage.getItem('user'));
console.log(localStorage.getItem('user'))            
                        /* Output: {"username":"username1",
                           "api_key":"axb124dasfasfas"}  */

