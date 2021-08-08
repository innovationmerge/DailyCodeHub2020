// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with ExpressJS

// Node program to build a server using Express

const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello iNNovationMerge!'));

app.listen(3000, () => console.log('Server app listening on port 3000!'));



