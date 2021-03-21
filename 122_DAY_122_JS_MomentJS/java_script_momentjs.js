// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with JAVA SCRIPT

// Program to managing dates in JavaScript using Moment.js
// npm install moment

// Code                                          | Output
const moment = require('moment')
const date = moment()
console.log(moment('2018-13-23').isValid())         
                                            //false
console.log(moment('2019-11-23').fromNow())         

                                            //a year ago
console.log(moment('2018-11-23').fromNow(true))    
                                             // 2 years
console.log(moment('2020-11-23').add(1, 'years')
                              .toLocaleString())   
                                            // Tue Nov 23 2021 00:00:00 GMT+0530
console.log(moment('2020-11-23').subtract(1, 'years')
                              .toLocaleString())   
                                            // Sat Nov 23 2019 00:00:00 GMT+0530


