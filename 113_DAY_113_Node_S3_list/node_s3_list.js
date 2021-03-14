// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to Display List of Amazon S3 Buckets

/* **************** Prerequisites ****************
        Refer to DAY 112 Post */

// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');

// Set the Region 
AWS.config.update({region: 'us-west-2'});

// Create S3 service object
s3 = new AWS.S3();

// Call S3 to list the buckets
s3.listBuckets(function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data.Buckets);
  }
});

/* **************** Output ****************
Success [
  { Name: 'nnm-test1', CreationDate: 2021-03-07T15:29:37.000Z },
  { Name: 'nnm-test2', CreationDate: 2021-03-07T15:29:51.000Z }
]
*/



