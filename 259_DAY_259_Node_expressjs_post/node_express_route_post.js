// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to handle HTTP POST request using Express

const express = require('express');
const app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());

app.post('/submit-name', function (req, res) {
  var name = req.body.firstName + ' ' + req.body.lastName;
  
  res.send(name + ' Submitted Successfully!');
});;

app.listen(3000, () => 
  console.log('Server app listening on port 3000!'));



