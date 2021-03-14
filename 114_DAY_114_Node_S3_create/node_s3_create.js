// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to Create an Amazon S3 Bucket

/* **************** Prerequisites ****************
        Refer to DAY 112 Post */

// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');

// Create S3 service object
s3 = new AWS.S3();

// Create the parameters for calling createBucket
var bucketParams = {
  Bucket : "nnm-test3"
};

// call S3 to create the bucket
s3.createBucket(bucketParams, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data.Location);
  }
});

/* **************** Output ****************
Success /nnm-test3
*/



