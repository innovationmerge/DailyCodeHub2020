// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to Serve static files using Express

const express = require('express');
const app = express();
app.use(express.static('public'));
app.get('*', (req, res) => {
  res.send('404! Link not found');
});
app.listen(3000, () => console.log('Server app listening on port 3000!'));



