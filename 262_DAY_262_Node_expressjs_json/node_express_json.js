// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to respond with JSON Data using Express

const express = require('express');
const app = express();

app.get('/get-json',function(req,res){
  res.json({'firstName' : 'iNNovation', 'lastName': 'Merge'});
});

app.listen(3000, () => 
  console.log('Server app listening on port 3000!'));



