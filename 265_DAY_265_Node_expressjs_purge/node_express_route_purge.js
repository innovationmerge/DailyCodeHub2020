// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to handle HTTP PURGE request using Express

const express = require('express');
const app = express();

app.purge('/purge-data', function (req, res) {
  res.send('PURGE Request');
});

app.listen(3000, () => 
  console.log('Server app listening on port 3000!'));



