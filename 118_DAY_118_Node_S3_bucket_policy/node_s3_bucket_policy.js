// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to Retrieve the Current Bucket Access Control List

/* **************** Prerequisites ****************
        Refer to DAY 112 Post */
// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');

// Create S3 service object
s3 = new AWS.S3();

var bucketName = "nnm-test1"
var bucketParams = {Bucket: bucketName};

// call S3 to retrieve policy for selected bucket
s3.getBucketAcl(bucketParams, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else if (data) {
    console.log("Success", data.Grants);
  }
});


/* ******** Output *********
Success [
  {
    Grantee: {
      ID: '***************************************',
      Type: 'CanonicalUser'
    },
    Permission: 'FULL_CONTROL'
  }
]
*/



