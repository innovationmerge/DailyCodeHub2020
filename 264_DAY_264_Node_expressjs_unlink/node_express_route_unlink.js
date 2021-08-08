// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to handle HTTP LINK request using Express

const express = require('express');
const app = express();

app.unlink('/unlink-data', function (req, res) {
  res.send('UNLINK Request');
});

app.listen(3000, () => 
  console.log('Server app listening on port 3000!'));



