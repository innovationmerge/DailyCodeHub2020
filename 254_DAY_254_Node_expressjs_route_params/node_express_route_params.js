// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to add endpoints with routes

const express = require('express');
const app = express();
app.get('/product/:productId', (req, res) => {
  res.send(req.params);
});
app.listen(3000, () => console.log('Server app listening on port 3000!'));



