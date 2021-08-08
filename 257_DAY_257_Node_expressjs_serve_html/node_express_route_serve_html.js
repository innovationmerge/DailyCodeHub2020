// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to Render HTML file using Express

const express = require('express');
const path = require('path');
const app = express();
app.use(express.static('public'));
app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, '/index.html'));
});
app.listen(3000, () => console.log('Server app listening on port 3000!'));




