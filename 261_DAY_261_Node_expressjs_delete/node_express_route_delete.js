// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to handle HTTP DELETE request using Express

const express = require('express');
const app = express();

app.delete('/delete-data', function (req, res) {
  res.send('DELETE Request');
});

app.listen(3000, () => 
  console.log('Server app listening on port 3000!'));



