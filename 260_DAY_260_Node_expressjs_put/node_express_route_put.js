// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to handle HTTP PUT request using Express

const express = require('express');
const app = express();

app.put('/update-data', function (req, res) {
  res.send('PUT Request');
});

app.listen(3000, () => 
  console.log('Server app listening on port 3000!'));



