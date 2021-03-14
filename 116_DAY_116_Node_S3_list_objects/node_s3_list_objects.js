// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to List Objects in an Amazon S3 Bucket

/* **************** Prerequisites ****************
        Refer to DAY 112 Post */
// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');

// Create S3 service object
s3 = new AWS.S3();

// Create the parameters for calling listObjects
var bucketParams = {
  Bucket : 'nnm-test3',
};

// Call S3 to obtain a list of the objects in the bucket
s3.listObjects(bucketParams, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});


/* ******** Output *********
Success {
  IsTruncated: false,
  Marker: '',
  Contents: [
    {
    File MetaData
    }
  ],
  Name: 'nnm-test3',
  Prefix: '',
  MaxKeys: 1000,
  CommonPrefixes: []
}
*/



