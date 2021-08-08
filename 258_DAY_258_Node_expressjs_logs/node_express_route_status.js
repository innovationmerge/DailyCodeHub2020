// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to respond with HTTP Status

const express = require('express');
const app = express();
app.get('*', (req, res) => {
  res.status(404).send('404! Link not found');
});
app.listen(3000, () => console.log('Server app listening on port 3000!'));



