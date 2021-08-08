// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to add endpoints with routes

const express = require('express');
const app = express();
app.get('/main', (req, res) => {
    res.send('Main Page');
  });
app.get('/product', (req, res) => {
    res.send('Product page');
});
app.listen(3000, () => console.log('Server app listening on port 3000!'));



