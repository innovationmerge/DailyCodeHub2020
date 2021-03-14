// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to Delete an Amazon S3 Bucket

/* **************** Prerequisites ****************
        Refer to DAY 112 Post */
// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');

// Create S3 service object
s3 = new AWS.S3();

// Create params for S3.deleteBucket
var bucketParams = {
  Bucket : 'nnm-test2'
};

// Call S3 to delete the bucket
s3.deleteBucket(bucketParams, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});


/* ******** Output *********
Success {}
*/



